#!/usr/bin/env python3
"""Simple terminal UI for Crip Center."""

from settings import get_system_info


def show_main_menu() -> None:
    print("1. Wallpaper")
    print("2. Theme")
    print("3. Performance Mode")
    print("4. Gaming Mode")
    print("5. Updates")
    print("6. System Info")
    print("0. Exit")

    choice = input("Select an option: ").strip()

    if choice == "6":
        print(get_system_info())
    elif choice == "0":
        print("Exiting Crip Center.")
    else:
        print("Feature coming soon.")
