#!/usr/bin/env python3
"""Appearance settings page for Crip Center."""

from system.theme_manager import get_current_theme, list_themes, set_theme, get_theme_colors


def show_page() -> None:
    current = get_current_theme()
    print("🎨 Appearance Settings")
    print("=" * 30)
    print(f"Current Theme: {current}")
    print("Available Themes:")
    for theme in list_themes():
        marker = "●" if theme == current else "○"
        print(f"  {marker} {theme}")


if __name__ == "__main__":
    show_page()
