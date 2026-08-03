#!/usr/bin/env python3
"""Terminal-based welcome UI for CripOS."""

from config import load_config, save_config
from language import choose_language, load_language
from internet import check_internet


def show_screen(title: str, body: list[str], action: str = "") -> None:
    print("\n" + title)
    for line in body:
        print(line)
    if action:
        print("\n" + action)


def run_welcome() -> None:
    config = load_config()

    show_screen(
        "💚 CripOS",
        ["Never Gives Up", "", "Welcome to CripOS"],
        "[ Get Started ]",
    )
    input("Press Enter to continue...")

    show_screen(
        "Select Language",
        ["[1] O'zbekcha", "[2] English"],
        "[ Continue ]",
    )
    choice = input("Select: ").strip()
    lang_code = choose_language(choice)
    config["language"] = lang_code
    save_config(config)

    strings = load_language(lang_code)
    show_screen(
        strings["internet_title"],
        [strings["internet_connected"]],
        "[ Continue ]",
    )
    input("Press Enter to continue...")

    show_screen(
        strings["updates_title"],
        [strings["updates_version"], "", strings["skip"], strings["install_updates"]],
        "[ Continue ]",
    )
    input("Press Enter to continue...")

    show_screen(
        strings["finish_title"],
        [strings["finish_message"], strings["finish_subtitle"]],
        "[ Start ]",
    )
