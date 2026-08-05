#!/usr/bin/env python3
"""Wallpaper settings page for Crip Center."""

from system.wallpaper_manager import get_current_wallpaper, list_wallpapers, set_wallpaper


def show_page() -> None:
    current = get_current_wallpaper()
    print("🖼 Wallpaper Settings")
    print("=" * 30)
    print(f"Current Wallpaper: {current}")
    print("Available Wallpapers:")
    for wp in list_wallpapers():
        marker = "●" if wp == current else "○"
        print(f"  {marker} {wp}")


if __name__ == "__main__":
    show_page()
