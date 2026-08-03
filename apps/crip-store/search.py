#!/usr/bin/env python3
"""Search helper for Crip Store."""

import json
from pathlib import Path


def search_apps(query: str) -> list[dict]:
    data_path = Path(__file__).with_name("database.json")
    with data_path.open("r", encoding="utf-8") as handle:
        apps = json.load(handle)["apps"]

    return [app for app in apps if query.lower() in app["name"].lower()]
