#!/usr/bin/env python3
"""Simple internal API layer for CripOS services."""

from libs.cripcore import CripCore


class SystemAPI:
    def __init__(self, root: str | None = None) -> None:
        self.core = CripCore(root)

    def get_status(self) -> dict:
        return {
            "name": "CripOS",
            "version": "Alpha 0.1",
            "status": "running",
        }
