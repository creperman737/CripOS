#!/usr/bin/env python3
"""CripOS Wallpaper Manager - manage wallpapers and background settings."""

import json
import random
from pathlib import Path

WALLPAPERS_DIR = Path(__file__).resolve().parents[1] / "wallpapers"
WALLPAPER_CONFIG = Path.home() / ".config" / "cripos" / "wallpaper.json"

DEFAULT_WALLPAPERS = {
    "default": "crip-default.png",
    "gaming": "crip-gaming.png",
    "nature": "crip-nature.png",
    "dark": "crip-dark.png",
}


def load_wallpaper_config() -> dict:
    """Load the current wallpaper configuration."""
    defaults = {"current": "default", "mode": "fill", "slideshow": False}
    try:
        with WALLPAPER_CONFIG.open("r", encoding="utf-8") as f:
            data = json.load(f)
            defaults.update(data)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return defaults


def save_wallpaper_config(config: dict) -> None:
    """Save the wallpaper configuration."""
    WALLPAPER_CONFIG.parent.mkdir(parents=True, exist_ok=True)
    with WALLPAPER_CONFIG.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)


def get_current_wallpaper() -> str:
    """Return the current wallpaper name."""
    return load_wallpaper_config()["current"]


def set_wallpaper(name: str) -> bool:
    """Set active wallpaper by name or path."""
    config = load_wallpaper_config()
    config["current"] = name
    save_wallpaper_config(config)
    return True


def list_wallpapers() -> list[str]:
    """List available wallpaper presets/files."""
    wallpapers = list(DEFAULT_WALLPAPERS.keys())
    if WALLPAPERS_DIR.exists():
        for f in WALLPAPERS_DIR.glob("*.[pP][nN][gG]"):
            if f.stem not in wallpapers:
                wallpapers.append(f.stem)
    return wallpapers


def get_random_wallpaper() -> str:
    """Pick a random wallpaper."""
    wallpapers = list_wallpapers()
    return random.choice(wallpapers) if wallpapers else "default"


if __name__ == "__main__":
    current = get_current_wallpaper()
    print("💚 CripOS Wallpaper Manager")
    print("=" * 35)
    print(f"  Current Wallpaper : {current}")
    print(f"  Available         : {', '.join(list_wallpapers())}")
