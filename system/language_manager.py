#!/usr/bin/env python3
"""CripOS Language Manager - manage system language settings."""

import json
from pathlib import Path

LOCALES_DIR = Path(__file__).resolve().parents[1] / "locales"
LANG_CONFIG = Path.home() / ".config" / "cripos" / "language.json"

AVAILABLE_LANGUAGES = {
    "en": "English",
    "uz": "O'zbekcha",
}


def load_language_config() -> dict:
    """Load the current language configuration."""
    defaults = {"current": "en"}
    try:
        with LANG_CONFIG.open("r", encoding="utf-8") as f:
            data = json.load(f)
            defaults.update(data)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return defaults


def save_language_config(config: dict) -> None:
    """Save the language configuration."""
    LANG_CONFIG.parent.mkdir(parents=True, exist_ok=True)
    with LANG_CONFIG.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)


def get_current_language() -> str:
    """Return the current language code."""
    return load_language_config()["current"]


def set_language(lang: str) -> bool:
    """Set the active system language."""
    if lang not in AVAILABLE_LANGUAGES:
        return False
    config = load_language_config()
    config["current"] = lang
    save_language_config(config)
    return True


def list_languages() -> dict:
    """Return the mapping of available language codes to names."""
    return AVAILABLE_LANGUAGES.copy()


def get_language_name(lang: str | None = None) -> str:
    """Return the full name of a language code."""
    code = lang or get_current_language()
    return AVAILABLE_LANGUAGES.get(code, code)


if __name__ == "__main__":
    current = get_current_language()
    print("💚 CripOS Language Manager")
    print("=" * 35)
    print(f"  Current : {current} ({get_language_name(current)})")
    print("  Available:")
    for code, name in list_languages().items():
        marker = "●" if code == current else "○"
        print(f"    {marker} {code} - {name}")
    print("  Use: python -m system.language_manager set <lang>")