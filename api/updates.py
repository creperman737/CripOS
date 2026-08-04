#!/usr/bin/env python3
"""Updates API for CripOS."""


def get_update_status() -> dict:
    return {"available": 0, "installed": 1, "channel": "alpha"}
