#!/usr/bin/env python3
"""Simple search helper for launcher."""


def search_apps(query: str) -> list[str]:
    apps = [
        "Crip Center",
        "Crip Store",
        "Crip Terminal",
        "Settings",
        "Files",
        "Terminal",
        "Welcome",
    ]
    return [app for app in apps if query.lower() in app.lower()]
