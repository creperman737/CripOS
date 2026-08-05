#!/usr/bin/env python3
"""Gaming settings page for Crip Center."""


def get_gaming_status() -> dict:
    return {
        "gamemode": True,
        "proton": "Proton Experimental",
        "steam": "Installed",
        "wine": "Available",
        "heroic": "Available",
    }


def show_page() -> None:
    status = get_gaming_status()
    print("🎮 Gaming Mode Settings")
    print("=" * 30)
    for key, val in status.items():
        print(f"  {key.capitalize():<12}: {val}")


if __name__ == "__main__":
    show_page()
