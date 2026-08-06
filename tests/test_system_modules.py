"""CripOS system module tests."""
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from system.boot.boot import check_disk_space, check_memory
from system.login.login import hash_password, create_user, authenticate
from system.security.security import load_security_config, DEFAULT_SECURITY
from system.updates.updates import load_update_config, DEFAULT_CONFIG
from system.startup.startup import load_startup_config, DEFAULT_STARTUP
from system.wallpaper_manager import get_current_wallpaper, list_wallpapers, set_wallpaper, get_random_wallpaper
from system.theme_manager import get_current_theme, list_themes, set_theme, get_theme_colors
from system.package_manager import list_installed, search_packages
from system.language_manager import (
    get_current_language,
    get_language_name,
    list_languages,
    set_language,
)


class BootTests(unittest.TestCase):
    def test_check_disk_space_returns_bool(self) -> None:
        result = check_disk_space()
        self.assertIsInstance(result, bool)

    def test_check_memory_returns_bool(self) -> None:
        result = check_memory()
        self.assertIsInstance(result, bool)


class LoginTests(unittest.TestCase):
    def test_hash_password_is_deterministic(self) -> None:
        h1 = hash_password("test123")
        h2 = hash_password("test123")
        self.assertEqual(h1, h2)
        self.assertEqual(len(h1), 64)  # SHA-256 hex digest

    def test_hash_password_different_inputs(self) -> None:
        h1 = hash_password("test123")
        h2 = hash_password("test456")
        self.assertNotEqual(h1, h2)


class SecurityTests(unittest.TestCase):
    def test_default_security_config(self) -> None:
        config = load_security_config()
        self.assertIn("firewall", config)
        self.assertIn("auto_updates", config)
        self.assertIn("secure_boot", config)
        self.assertIn("sudo_required", config)

    def test_defaults_are_sane(self) -> None:
        self.assertTrue(DEFAULT_SECURITY["firewall"])
        self.assertTrue(DEFAULT_SECURITY["auto_updates"])


class UpdateTests(unittest.TestCase):
    def test_default_update_config(self) -> None:
        config = load_update_config()
        self.assertIn("channel", config)
        self.assertIn("auto_check", config)
        self.assertIn("auto_install", config)

    def test_default_channel_is_alpha(self) -> None:
        self.assertEqual(DEFAULT_CONFIG["channel"], "alpha")


class StartupTests(unittest.TestCase):
    def test_default_startup_config(self) -> None:
        config = load_startup_config()
        self.assertIn("crip-launcher", config)
        self.assertIn("crip-network", config)

    def test_launcher_starts_by_default(self) -> None:
        self.assertTrue(DEFAULT_STARTUP["crip-launcher"])


class WallpaperTests(unittest.TestCase):
    def test_get_current_wallpaper(self) -> None:
        self.assertIsInstance(get_current_wallpaper(), str)

    def test_list_wallpapers(self) -> None:
        wps = list_wallpapers()
        self.assertGreater(len(wps), 0)

    def test_set_wallpaper(self) -> None:
        # Pick the first available wallpaper (the preset list may change)
        available = list_wallpapers()
        self.assertTrue(available, "Expected at least one wallpaper")
        self.assertTrue(set_wallpaper(available[0]))
        self.assertEqual(get_current_wallpaper(), available[0])

    def test_set_wallpaper_invalid(self) -> None:
        self.assertFalse(set_wallpaper("nonexistent-wallpaper-xyz"))

    def test_get_random_wallpaper(self) -> None:
        self.assertIsInstance(get_random_wallpaper(), str)


class ThemeManagerTests(unittest.TestCase):
    def test_get_current_theme(self) -> None:
        self.assertIsInstance(get_current_theme(), str)

    def test_list_themes(self) -> None:
        themes = list_themes()
        self.assertIn("crip-dark", themes)
        self.assertIn("crip-light", themes)

    def test_get_theme_colors(self) -> None:
        colors = get_theme_colors("crip-dark")
        self.assertIn("primary", colors)


class PackageManagerTests(unittest.TestCase):
    def test_list_installed(self) -> None:
        installed = list_installed()
        self.assertIsInstance(installed, list)


class LanguageManagerTests(unittest.TestCase):
    def test_get_current_language(self) -> None:
        self.assertIsInstance(get_current_language(), str)

    def test_list_languages(self) -> None:
        languages = list_languages()
        self.assertIn("en", languages)
        self.assertIn("uz", languages)

    def test_set_language_valid(self) -> None:
        self.assertTrue(set_language("uz"))
        self.assertEqual(get_current_language(), "uz")

    def test_set_language_invalid(self) -> None:
        self.assertFalse(set_language("xx"))

    def test_get_language_name(self) -> None:
        self.assertEqual(get_language_name("en"), "English")
        self.assertEqual(get_language_name("uz"), "O'zbekcha")


if __name__ == "__main__":
    unittest.main()