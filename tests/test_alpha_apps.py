import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "apps" / "crip-launcher"))
sys.path.insert(0, str(REPO_ROOT / "apps" / "crip-center"))

from launcher import get_launcher_apps
from ui import get_center_sections


class CripAlphaAppTests(unittest.TestCase):
    def test_launcher_has_core_apps(self) -> None:
        apps = get_launcher_apps()
        self.assertIn("Files", apps)
        self.assertIn("Terminal", apps)
        self.assertIn("Settings", apps)

    def test_center_has_core_sections(self) -> None:
        sections = get_center_sections()
        self.assertIn("Appearance", sections)
        self.assertIn("Updates", sections)
        self.assertIn("About", sections)


if __name__ == "__main__":
    unittest.main()
