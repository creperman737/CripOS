"""CripOS CLI tools tests."""
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "tools"))

import importlib.util


def _load_tool(name: str):
    """Load a CLI tool module by its filename."""
    path = REPO_ROOT / "tools" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


crip_info = _load_tool("crip-info")
crip_update = _load_tool("crip-update")
crip_store = _load_tool("crip-store")
crip_welcome = _load_tool("crip-welcome")
crip_about = _load_tool("crip-about")
crip_doctor = _load_tool("crip-doctor")

crip_info_main = crip_info.main
crip_update_main = crip_update.main
crip_store_main = crip_store.main
crip_welcome_main = crip_welcome.main
crip_about_main = crip_about.main
check_structure = crip_doctor.check_structure


class CripInfoTests(unittest.TestCase):
    def test_info_outputs(self) -> None:
        # Should not raise
        crip_info_main()

    def test_info_has_cripos(self) -> None:
        import io
        import contextlib

        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            crip_info_main()
        self.assertIn("CripOS", buffer.getvalue())


class CripUpdateTests(unittest.TestCase):
    def test_update_outputs(self) -> None:
        import io
        import contextlib

        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            crip_update_main()
        self.assertIn("CripOS", buffer.getvalue())


class CripStoreTests(unittest.TestCase):
    def test_store_outputs(self) -> None:
        import io
        import contextlib

        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            crip_store_main()
        self.assertIn("Crip Store", buffer.getvalue())


class CripWelcomeTests(unittest.TestCase):
    def test_welcome_outputs(self) -> None:
        import io
        import contextlib

        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            crip_welcome_main()
        self.assertIn("Welcome", buffer.getvalue())


class CripAboutTests(unittest.TestCase):
    def test_about_outputs(self) -> None:
        import io
        import contextlib

        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            crip_about_main()
        self.assertIn("CripOS", buffer.getvalue())


class CripDoctorTests(unittest.TestCase):
    def test_check_structure(self) -> None:
        results = check_structure()
        self.assertGreater(len(results), 0)

    def test_structure_has_expected_dirs(self) -> None:
        results = dict(check_structure())
        self.assertIn("Directory 'apps'", results)
        self.assertTrue(results["Directory 'apps'"])
        self.assertIn("Directory 'sdk'", results)
        self.assertTrue(results["Directory 'sdk'"])


if __name__ == "__main__":
    unittest.main()