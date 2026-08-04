#!/usr/bin/env python3
"""CripOS security manager."""

import json
import os
import subprocess
from pathlib import Path

SECURITY_CONFIG = Path("/etc/cripos/security.json")
FIREWALL_RULES = Path("/etc/cripos/firewall.json")

DEFAULT_SECURITY = {
    "firewall": True,
    "auto_updates": True,
    "secure_boot": True,
    "sudo_required": True,
}


def load_security_config() -> dict:
    """Load security configuration."""
    try:
        with SECURITY_CONFIG.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_SECURITY.copy()


def save_security_config(config: dict) -> None:
    """Save security configuration."""
    SECURITY_CONFIG.parent.mkdir(parents=True, exist_ok=True)
    with SECURITY_CONFIG.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)


def enable_firewall() -> bool:
    """Enable the system firewall."""
    try:
        subprocess.run(["ufw", "enable"], check=True, capture_output=True)
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        return False


def check_firewall_status() -> bool:
    """Check if the firewall is enabled."""
    try:
        result = subprocess.run(
            ["ufw", "status"],
            check=False,
            capture_output=True,
            text=True,
        )
        return "Status: active" in result.stdout
    except FileNotFoundError:
        return False


def run_security_check() -> dict:
    """Run a security check and return results."""
    config = load_security_config()
    results = {
        "firewall": check_firewall_status() if config["firewall"] else False,
        "auto_updates": config["auto_updates"],
        "secure_boot": config["secure_boot"],
        "sudo_required": config["sudo_required"],
    }
    return results


if __name__ == "__main__":
    results = run_security_check()
    print("CripOS Security Check")
    print("=====================")
    for key, value in results.items():
        status = "✅" if value else "❌"
        print(f"{status} {key}: {value}")