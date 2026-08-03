#!/usr/bin/env python3
"""Simple package installer scaffold for Crip Store."""

import json
import os
from pathlib import Path


def load_database(path: str = "store/database.json") -> dict:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def install_app(app_name: str) -> None:
    data = load_database()
    app = next((item for item in data.get("apps", []) if item["name"].lower() == app_name.lower()), None)
    if not app:
        print(f"App '{app_name}' not found.")
        return

    print(f"Installing {app['name']}...")
    print(f"Package: {app['package']}")
    print("Installation completed (scaffold).")


if __name__ == "__main__":
    target = input("Enter app name to install: ").strip()
    install_app(target)
