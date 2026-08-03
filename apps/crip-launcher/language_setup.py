#!/usr/bin/env python3
"""Simple first-run language selection scaffold."""

from locale_helper import show_locale_demo


def show_language_setup() -> None:
    print("Welcome to CripOS")
    print("")
    print("Select Language")
    print("")
    print("[1] O'zbekcha")
    print("[2] English")
    choice = input("Choose: ").strip()

    if choice == "2":
        show_locale_demo("en")
    else:
        show_locale_demo("uz")


if __name__ == "__main__":
    show_language_setup()
