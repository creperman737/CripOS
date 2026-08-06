#!/usr/bin/env python3
"""CripOS Theme Manager - switch and manage themes."""

import json
import shutil
from pathlib import Path

THEMES_DIR = Path("/usr/share/themes")
CRIP_THEMES = Path(__file__).resolve().parents[1] / "themes"
THEME_CONFIG = Path("/etc/cripos/theme.json")

AVAILABLE_THEMES = ["crip-dark", "crip-light", "cripgreen", "minecraft"]


def load_theme_config() -> dict:
    """Load the current theme configuration."""
    defaults = {"current": "crip-dark", "accent": "#39D353"}
    try:
        with THEME_CONFIG.open("r", encoding="utf-8") as f:
            data = json.load(f)
            defaults.update(data)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return defaults


def save_theme_config(config: dict) -> None:
    """Save the theme configuration."""
    THEME_CONFIG.parent.mkdir(parents=True, exist_ok=True)
    with THEME_CONFIG.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)


def get_current_theme() -> str:
    """Return the current theme name."""
    return load_theme_config()["current"]


def set_theme(name: str) -> bool:
    """Set the active theme."""
    if name not in AVAILABLE_THEMES:
        return False
    config = load_theme_config()
    config["current"] = name
    save_theme_config(config)

    # Copy GTK CSS to the system themes directory if writable
    src = CRIP_THEMES / name / "gtk.css"
    if src.exists():
        try:
            dest = THEMES_DIR / name
            dest.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest / "gtk.css")
        except OSError:
            pass
    return True


def set_accent_color(color: str) -> bool:
    """Set the accent color."""
    config = load_theme_config()
    config["accent"] = color
    save_theme_config(config)
    return True


def get_theme_colors(name: str | None = None) -> dict:
    """Get the color palette for a theme."""
    theme = name or get_current_theme()
    themes = {
        "crip-dark": {
            "bg": "#0D1117",
            "surface": "#161B22",
            "border": "#30363D",
            "text": "#F0F6FC",
            "muted": "#8B949E",
            "primary": "#39D353",
            "secondary": "#2EA043",
            "danger": "#F85149",
        },
        "crip-light": {
            "bg": "#FFFFFF",
            "surface": "#F6F8FA",
            "border": "#D0D7DE",
            "text": "#1F2328",
            "muted": "#656D76",
            "primary": "#1F883D",
            "secondary": "#2EA043",
            "danger": "#CF222E",
        },
        "cripgreen": {
            "bg": "#0A1F0A",
            "surface": "#122A12",
            "border": "#1E3A1E",
            "text": "#E8F5E9",
            "muted": "#81C784",
            "primary": "#4CAF50",
            "secondary": "#2E7D32",
            "danger": "#F44336",
        },
        "minecraft": {
            "bg": "#1D1D1D",
            "surface": "#2D2D2D",
            "border": "#3D3D3D",
            "text": "#FFFFFF",
            "muted": "#AAAAAA",
            "primary": "#55FF55",
            "secondary": "#00AA00",
            "danger": "#FF5555",
        },
    }
    return themes.get(theme, themes["crip-dark"])


def list_themes() -> list[str]:
    """List all available themes."""
    return AVAILABLE_THEMES.copy()


if __name__ == "__main__":
    current = get_current_theme()
    print("💚 CripOS Theme Manager")
    print("=" * 35)
    print(f"  Current: {current}")
    print("  Available:")
    for theme in list_themes():
        marker = "●" if theme == current else "○"
        print(f"    {marker} {theme}")
    print("  Use: python -m system.theme_manager set <theme>")