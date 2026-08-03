#!/usr/bin/env python3
"""Language support helper for Crip Welcome."""

import json
from pathlib import Path


def load_language(lang: str) -> dict:
    path = Path(__file__).resolve().parent / "locales" / f"{lang}.json"
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def choose_language(choice: str) -> str:
    if choice == "2":
        return "en"
    return "uz"
