#!/usr/bin/env python3
"""CripOS startup applications manager."""

import json
import os
from pathlib import Path

STARTUP_CONFIG = Path.home() / ".config" / "cripos" / "startup.json"

DEFAULT_STARTUP = {
    "crip-launcher": True,
    "crip-welcome": False,
    "crip-network": True,
    "crip-notify": True,
}


def load_startup_config() -> dict:
    """Load startup applications configuration."""
    try:
        with STARTUP_CONFIG.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_STARTUP.copy()


def save_startup_config(config: dict) -> None:
    """Save startup applications configuration."""
    STARTUP_CONFIG.parent.mkdir(parents=True, exist_ok=True)
    with STARTUP_CONFIG.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)


def set_startup_enabled(app_name: str, enabled: bool) -> None:
    """Enable or disable an app at startup."""
    config = load_startup_config()
    config[app_name] = enabled
    save_startup_config(config)


def get_startup_apps() -> list[str]:
    """Return a list of apps that should start."""
    config = load_startup_config()
    return [app for app, enabled in config.items() if enabled]


if __name__ == "__main__":
    print("CripOS Startup Apps")
    print("===================")
    for app in get_startup_apps():
        print(f"- {app}")