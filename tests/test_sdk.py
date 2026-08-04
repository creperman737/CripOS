"""CripOS SDK tests."""
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from sdk.cripapi import system_status, system_info, get_apps, get_version
from sdk.cripui import button, label, input_field, checkbox, dropdown, progress_bar
from sdk.cripwidgets import card, window, dialog, toast, sidebar, toolbar
from sdk.cripthemes import default_theme, light_theme, minecraft_theme, get_theme


class CripAPITests(unittest.TestCase):
    def test_system_status(self) -> None:
        status = system_status()
        self.assertEqual(status["name"], "CripOS")
        self.assertEqual(status["status"], "ready")

    def test_system_info(self) -> None:
        info = system_info()
        self.assertEqual(info["version"], "Alpha 0.1")
        self.assertEqual(info["base"], "Debian 13 (Trixie)")

    def test_get_apps(self) -> None:
        apps = get_apps()
        self.assertIn("Crip Welcome", apps)
        self.assertIn("Crip Launcher", apps)
        self.assertGreater(len(apps), 5)

    def test_get_version(self) -> None:
        self.assertEqual(get_version(), "CripOS 0.1 Alpha")


class CripUITests(unittest.TestCase):
    def test_button(self) -> None:
        self.assertEqual(button("Click"), "[button] Click")

    def test_label(self) -> None:
        self.assertEqual(label("Hello"), "[label] Hello")

    def test_input_field(self) -> None:
        self.assertEqual(input_field("Type here"), "[input] Type here")

    def test_checkbox(self) -> None:
        self.assertEqual(checkbox("Option"), "[checkbox] [ ] Option")
        self.assertEqual(checkbox("Option", True), "[checkbox] [x] Option")

    def test_dropdown(self) -> None:
        self.assertEqual(dropdown(["A", "B"]), "[dropdown] A, B")

    def test_progress_bar(self) -> None:
        bar = progress_bar(50)
        self.assertIn("50%", bar)


class CripWidgetTests(unittest.TestCase):
    def test_card(self) -> None:
        self.assertEqual(card("Title"), "[card] Title")

    def test_window(self) -> None:
        self.assertEqual(window("App"), "[window] App (640x480)")

    def test_dialog(self) -> None:
        self.assertEqual(dialog("Error", "Something"), "[dialog] Error: Something")

    def test_toast(self) -> None:
        self.assertEqual(toast("Done"), "[toast] Done")

    def test_sidebar(self) -> None:
        self.assertEqual(sidebar(["Home", "Files"]), "[sidebar] Home, Files")

    def test_toolbar(self) -> None:
        self.assertEqual(toolbar(["New", "Open"]), "[toolbar] New, Open")


class CripThemeTests(unittest.TestCase):
    def test_default_theme(self) -> None:
        theme = default_theme()
        self.assertEqual(theme["primary"], "#39D353")
        self.assertEqual(theme["background"], "#0D1117")

    def test_light_theme(self) -> None:
        theme = light_theme()
        self.assertEqual(theme["background"], "#FFFFFF")

    def test_minecraft_theme(self) -> None:
        theme = minecraft_theme()
        self.assertEqual(theme["primary"], "#55FF55")

    def test_get_theme(self) -> None:
        self.assertEqual(get_theme("crip-dark"), default_theme())
        self.assertEqual(get_theme("crip-light"), light_theme())
        self.assertEqual(get_theme("minecraft"), minecraft_theme())
        self.assertEqual(get_theme("unknown"), default_theme())


if __name__ == "__main__":
    unittest.main()