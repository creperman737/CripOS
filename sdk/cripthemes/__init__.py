#!/usr/bin/env python3
"""Theme helpers for the CripOS SDK."""


def default_theme() -> dict:
    """Return the default CripOS dark theme."""
    return {
        "primary": "#39D353",
        "secondary": "#2EA043",
        "background": "#0D1117",
        "surface": "#161B22",
        "border": "#30363D",
        "text": "#F0F6FC",
        "muted": "#8B949E",
        "danger": "#F85149",
    }


def light_theme() -> dict:
    """Return the CripOS light theme."""
    return {
        "primary": "#1F883D",
        "secondary": "#2EA043",
        "background": "#FFFFFF",
        "surface": "#F6F8FA",
        "border": "#D0D7DE",
        "text": "#1F2328",
        "muted": "#656D76",
        "danger": "#CF222E",
    }


def minecraft_theme() -> dict:
    """Return the Minecraft-inspired theme."""
    return {
        "primary": "#55FF55",
        "secondary": "#00AA00",
        "background": "#1D1D1D",
        "surface": "#2D2D2D",
        "border": "#3D3D3D",
        "text": "#FFFFFF",
        "muted": "#AAAAAA",
        "danger": "#FF5555",
    }


def get_theme(name: str = "crip-dark") -> dict:
    """Return a theme by name."""
    themes = {
        "crip-dark": default_theme(),
        "crip-light": light_theme(),
        "minecraft": minecraft_theme(),
    }
    return themes.get(name, default_theme())