#!/usr/bin/env python3
"""Configuration helpers for Crip Welcome.

The application bundle under ``/opt/cripos`` is read-only for regular desktop
users.  Crip Welcome therefore reads bundled/system defaults and writes a
per-user override when setup is completed.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


APP_DIR = Path(__file__).resolve().parent
APP_DEFAULTS_PATH = APP_DIR / "config.json"
SYSTEM_DEFAULTS_PATH = Path("/etc/cripos/config.json")
CONFIG_ENV_VAR = "CRIPOS_WELCOME_CONFIG"

DEFAULT_CONFIG: dict[str, Any] = {
    "language": "uz",
    "completed": False,
    "internet": True,
    "updates": False,
}


def get_user_config_path() -> Path:
    """Return the user-writable state file, honoring a test/developer override."""
    override = os.environ.get(CONFIG_ENV_VAR)
    if override:
        return Path(override).expanduser()

    config_home = os.environ.get("XDG_CONFIG_HOME")
    base_dir = Path(config_home).expanduser() if config_home else Path.home() / ".config"
    return base_dir / "cripos" / "welcome.json"


def _read_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}
    return data if isinstance(data, dict) else {}


def load_config(path: Path | None = None) -> dict[str, Any]:
    """Load defaults plus optional system and user overrides.

    ``path`` is useful for tests and developer tooling: it is loaded on top of
    built-in defaults without consulting machine-specific config files.
    """
    config = DEFAULT_CONFIG.copy()

    if path is not None:
        config.update(_read_json(Path(path)))
        return config

    for candidate in (APP_DEFAULTS_PATH, SYSTEM_DEFAULTS_PATH, get_user_config_path()):
        config.update(_read_json(candidate))
    return config


def save_config(data: dict[str, Any], path: Path | None = None) -> Path:
    """Persist user-specific setup state and return the written file path."""
    destination = Path(path) if path is not None else get_user_config_path()
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    return destination
