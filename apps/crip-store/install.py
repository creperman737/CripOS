#!/usr/bin/env python3
"""Installer for Crip Store apps."""

import json
from pathlib import Path
from system.package_manager import install_package


def install_app(app_name: str) -> bool:
    data_path = Path(__file__).with_name("database.json")
    with data_path.open("r", encoding="utf-8") as handle:
        apps = json.load(handle)["apps"]

    match = next((item for item in apps if item["name"].lower() == app_name.lower()), None)
    if not match:
        print(f"App '{app_name}' not found.")
        return False

    package = match.get("package", app_name.lower())
    print(f"Installing {match['name']} ({package})...")
    result = install_package(package)
    print("Installation completed.")
    return result
