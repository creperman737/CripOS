#!/usr/bin/env python3
"""Removal helper for Crip Store apps."""

import json
from pathlib import Path
from system.package_manager import remove_package


def remove_app(app_name: str) -> bool:
    data_path = Path(__file__).with_name("database.json")
    try:
        with data_path.open("r", encoding="utf-8") as handle:
            apps = json.load(handle)["apps"]
        match = next((item for item in apps if item["name"].lower() == app_name.lower()), None)
        package = match.get("package", app_name.lower()) if match else app_name.lower()
    except Exception:
        package = app_name.lower()

    print(f"Removing {app_name} ({package})...")
    result = remove_package(package)
    print("Removal completed.")
    return result
