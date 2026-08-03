#!/usr/bin/env python3
"""Simple locale loader for Crip Launcher."""

import json
from pathlib import Path


def load_strings(lang: str = "uz") -> dict:
    path = Path(__file__).resolve().parents[1] / "locales" / lang / "launcher.json"
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def show_locale_demo(lang: str = "uz") -> None:
    strings = load_strings(lang)
    print("CripOS Language Demo")
    print("====================")
    print(strings["search"])
    print(strings["settings"])
    print(strings["shutdown"])
    print(strings["restart"])
    print(strings["logout"])
