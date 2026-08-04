#!/usr/bin/env python3
"""CripOS update manager."""

import json
import os
import subprocess
from pathlib import Path

UPDATE_CONFIG = Path("/etc/cripos/updates.json")

DEFAULT_CONFIG = {
    "channel": "alpha",
    "auto_check": True,
    "auto_install": False,
}


def load_update_config() -> dict:
    """Load update configuration."""
    try:
        with UPDATE_CONFIG.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_CONFIG.copy()


def save_update_config(config: dict) -> None:
    """Save update configuration."""
    UPDATE_CONFIG.parent.mkdir(parents=True, exist_ok=True)
    with UPDATE_CONFIG.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)


def check_updates() -> dict:
    """Check for available updates."""
    try:
        result = subprocess.run(
            ["apt-get", "list", "--upgradable"],
            check=False,
            capture_output=True,
            text=True,
        )
        lines = [line for line in result.stdout.splitlines() if line.strip()]
        return {
            "available": len(lines),
            "installed": True,
            "channel": load_update_config()["channel"],
        }
    except FileNotFoundError:
        return {
            "available": 0,
            "installed": True,
            "channel": load_update_config()["channel"],
        }


def install_updates() -> bool:
    """Install all available updates."""
    config = load_update_config()
    if not config["auto_install"]:
        print("Auto-install is disabled.")
        return False

    try:
        subprocess.run(
            ["apt-get", "upgrade", "-y"],
            check=True,
            capture_output=True,
        )
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        return False


def set_channel(channel: str) -> None:
    """Set the update channel."""
    config = load_update_config()
    config["channel"] = channel
    save_update_config(config)


if __name__ == "__main__":
    print("CripOS Updates")
    print("==============")
    status = check_updates()
    print(f"Available updates: {status['available']}")
    print(f"Channel: {status['channel']}")