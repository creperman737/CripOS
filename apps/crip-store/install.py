#!/usr/bin/env python3
"""Installer for Crip Store apps."""

import json
from pathlib import Path


def install_app(app_name: str) -> None:
    data_path = Path(__file__).with_name("database.json")
    with data_path.open("r", encoding="utf-8") as handle:
        apps = json.load(handle)["apps"]

    match = next((item for item in apps if item["name"].lower() == app_name.lower()), None)
    if not match:
        print(f"App '{app_name}' not found.")
        return

    print(f"Installing {match['name']} ({match['package']})...")
    print("Installation completed (scaffold).")
