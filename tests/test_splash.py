"""CripOS splash text tests."""
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from branding.splash import get_splash_text, get_all_splash_texts, SPLASH_TEXTS


class SplashTextTests(unittest.TestCase):
    def test_get_splash_text_returns_string(self) -> None:
        text = get_splash_text()
        self.assertIsInstance(text, str)

    def test_splash_text_is_not_empty(self) -> None:
        text = get_splash_text()
        self.assertGreater(len(text), 0)

    def test_splash_text_from_list(self) -> None:
        text = get_splash_text()
        self.assertIn(text, SPLASH_TEXTS)

    def test_get_all_splash_texts(self) -> None:
        texts = get_all_splash_texts()
        self.assertEqual(len(texts), len(SPLASH_TEXTS))

    def test_splash_texts_have_meaningful_content(self) -> None:
        for text in SPLASH_TEXTS:
            self.assertGreater(len(text), 3)


if __name__ == "__main__":
    unittest.main()