#!/usr/bin/env python3
"""Language support helpers for Crip Welcome."""

from __future__ import annotations

import json
from pathlib import Path


LOCALES_DIR = Path(__file__).resolve().parent / "locales"
DEFAULT_LANGUAGE = "uz"
SUPPORTED_LANGUAGES = ("uz", "en")


def normalize_language(lang: str | None) -> str:
    """Return a supported language code, defaulting to Uzbek."""
    return lang if lang in SUPPORTED_LANGUAGES else DEFAULT_LANGUAGE


def load_language(lang: str | None) -> dict[str, str]:
    """Load one locale safely so a missing custom locale cannot stop setup."""
    language = normalize_language(lang)
    path = LOCALES_DIR / f"{language}.json"

    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        if language != DEFAULT_LANGUAGE:
            return load_language(DEFAULT_LANGUAGE)
        return {}

    return {key: value for key, value in data.items() if isinstance(value, str)}


def choose_language(choice: str) -> str:
    """Keep the original terminal-choice convention for simple callers."""
    return "en" if choice in {"2", "en"} else "uz"
