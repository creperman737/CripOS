#!/usr/bin/env python3
"""About page for Crip Center."""

from sdk.cripapi import system_info


def show_page() -> None:
    info = system_info()
    print("💚 CripOS System Overview")
    print("=" * 30)
    for key, value in info.items():
        print(f"  {key.capitalize():<14}: {value}")


if __name__ == "__main__":
    show_page()
