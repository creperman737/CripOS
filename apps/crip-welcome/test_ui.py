import unittest
from unittest.mock import mock_open, patch
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
import sys

sys.path.insert(0, str(APP_DIR))

import config
import internet
import language
import ui


class FakeResponse:
    status = 204

    def __init__(self) -> None:
        self.closed = False

    def getcode(self) -> int:
        return self.status

    def close(self) -> None:
        self.closed = True


class WelcomeTests(unittest.TestCase):
    def test_get_strings_returns_localized_content(self) -> None:
        uz = ui.get_strings("uz")
        en = ui.get_strings("en")

        self.assertEqual(uz["title"], "CripOS ga xush kelibsiz")
        self.assertEqual(uz["start"], "Boshlash")
        self.assertEqual(uz["continue"], "Davom etish")
        self.assertEqual(uz["done"], "Tayyor!")
        self.assertEqual(en["title"], "Welcome to CripOS")
        self.assertEqual(en["internet"], "Checking Internet...")

    def test_unknown_language_falls_back_to_uzbek(self) -> None:
        self.assertEqual(language.normalize_language("de"), "uz")
        self.assertEqual(language.load_language("de")["start"], "Boshlash")

    def test_config_override_merges_with_defaults(self) -> None:
        override = {"language": "en", "completed": True, "internet": False}
        with patch("config._read_json", return_value=override):
            loaded = config.load_config(APP_DIR / "test-welcome.json")

        self.assertEqual(loaded["language"], "en")
        self.assertTrue(loaded["completed"])
        self.assertFalse(loaded["internet"])
        self.assertFalse(loaded["updates"])

    def test_config_save_targets_an_explicit_user_path(self) -> None:
        config_path = APP_DIR / "test-config" / "welcome.json"
        state = {"language": "en", "completed": True}
        with patch.object(Path, "mkdir") as make_directory, patch.object(Path, "open", mock_open()) as open_file:
            saved_path = config.save_config(state, config_path)

        self.assertEqual(saved_path, config_path)
        make_directory.assert_called_once_with(parents=True, exist_ok=True)
        open_file.assert_called_once_with("w", encoding="utf-8")

    def test_flow_persists_language_then_completion(self) -> None:
        saved_states: list[dict] = []
        flow = ui.WelcomeFlow(
            {"language": "uz", "completed": False},
            save_callback=lambda state: saved_states.append(state),
        )

        self.assertFalse(flow.advance())
        self.assertEqual(flow.step, ui.STEP_LANGUAGE)
        flow.select_language("en")
        self.assertFalse(flow.advance())
        self.assertEqual(saved_states[-1]["language"], "en")
        self.assertEqual(flow.step, ui.STEP_INTERNET)

        self.assertFalse(flow.advance())
        self.assertFalse(flow.advance())
        self.assertEqual(flow.step, ui.STEP_COMPLETE)
        self.assertTrue(flow.advance())
        self.assertTrue(saved_states[-1]["completed"])
        self.assertEqual(saved_states[-1]["language"], "en")

    def test_completed_setup_does_not_open_a_window_again(self) -> None:
        with patch("ui.load_config", return_value={"completed": True}), patch("ui.tk.Tk") as create_root:
            self.assertFalse(ui.run_welcome())

        create_root.assert_not_called()

    def test_internet_check_reports_success_and_closes_response(self) -> None:
        response = FakeResponse()
        status = internet.check_internet(opener=lambda _request, timeout: response)

        self.assertTrue(status.connected)
        self.assertTrue(response.closed)

    def test_internet_check_reports_offline_without_raising(self) -> None:
        def offline(_request, timeout):
            raise OSError("network unavailable")

        status = internet.check_internet(opener=offline)
        self.assertFalse(status.connected)
        self.assertEqual(status.detail, "Offline")

    def test_packaged_assets_are_valid_png_files(self) -> None:
        for filename in ("logo.png", "background.png"):
            with (APP_DIR / "assets" / filename).open("rb") as asset:
                self.assertEqual(asset.read(8), b"\x89PNG\r\n\x1a\n")


if __name__ == "__main__":
    unittest.main()
