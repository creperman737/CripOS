#!/usr/bin/env python3
"""Shared helper utilities for CripOS applications."""

from pathlib import Path
import json


class CripCore:
    def __init__(self, root: str | None = None) -> None:
        self.root = Path(root or "/opt/cripos")

    def read_json(self, path: str) -> dict:
        with (self.root / path).open("r", encoding="utf-8") as handle:
            return json.load(handle)

    def write_json(self, path: str, data: dict) -> None:
        with (self.root / path).open("w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2)
