#!/usr/bin/env python3
"""Launcher menu and app shortcuts."""

from search import search_apps


def show_menu() -> None:
    print("[Search]")
    print("[Applications]")
    print("[Settings]")
    print("[Store]")
    print("[Terminal]")
    print("[Restart]")
    print("[Shutdown]")

    query = input("Type to search: ").strip()
    if query:
        results = search_apps(query)
        if results:
            print("Results:")
            for item in results:
                print(f"- {item}")
        else:
            print("No apps found")
    else:
        print("\nCripOS shell ready")
