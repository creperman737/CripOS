#!/usr/bin/env python3
"""Configuration helpers for Crip Welcome."""

from pathlib import Path
import json

CONFIG_PATH = Path(__file__).resolve().parent / "config.json"


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        return {"language": "uz", "internet": True, "updates": False}
    with CONFIG_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_config(data: dict) -> None:
    with CONFIG_PATH.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)
