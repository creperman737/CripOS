#!/usr/bin/env python3
"""CripOS Package Manager - install, remove, search, update packages."""

import json
import subprocess
from pathlib import Path

PACKAGE_DB = Path("/etc/cripos/packages.json")


def load_packages() -> dict:
    """Load the package database."""
    try:
        with PACKAGE_DB.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"installed": [], "available": []}


def save_packages(data: dict) -> None:
    """Save the package database."""
    PACKAGE_DB.parent.mkdir(parents=True, exist_ok=True)
    with PACKAGE_DB.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def install_package(name: str) -> bool:
    """Install a package."""
    try:
        subprocess.run(
            ["apt-get", "install", "-y", name],
            check=False,
            capture_output=True,
        )
        data = load_packages()
        if name not in data["installed"]:
            data["installed"].append(name)
        save_packages(data)
        return True
    except FileNotFoundError:
        # Fallback: just record the package
        data = load_packages()
        if name not in data["installed"]:
            data["installed"].append(name)
        save_packages(data)
        return True


def remove_package(name: str) -> bool:
    """Remove a package."""
    try:
        subprocess.run(
            ["apt-get", "remove", "-y", name],
            check=False,
            capture_output=True,
        )
        data = load_packages()
        if name in data["installed"]:
            data["installed"].remove(name)
        save_packages(data)
        return True
    except FileNotFoundError:
        data = load_packages()
        if name in data["installed"]:
            data["installed"].remove(name)
        save_packages(data)
        return True


def search_packages(query: str) -> list[str]:
    """Search for packages."""
    try:
        result = subprocess.run(
            ["apt-cache", "search", query],
            check=False,
            capture_output=True,
            text=True,
        )
        lines = [line.split(" - ")[0] for line in result.stdout.splitlines() if line.strip()]
        return lines[:20]
    except FileNotFoundError:
        return []


def update_packages() -> bool:
    """Update package lists."""
    try:
        result = subprocess.run(["apt-get", "update"], check=False, capture_output=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False


def upgrade_packages() -> bool:
    """Upgrade all installed packages."""
    try:
        result = subprocess.run(
            ["apt-get", "upgrade", "-y"], check=False, capture_output=True
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def clean_packages() -> bool:
    """Clean package cache."""
    try:
        result = subprocess.run(
            ["apt-get", "clean"], check=False, capture_output=True
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def get_package_info(name: str) -> dict:
    """Get information about a package."""
    try:
        result = subprocess.run(
            ["apt-cache", "show", name],
            check=False,
            capture_output=True,
            text=True,
        )
        info = {}
        for line in result.stdout.splitlines():
            if ":" in line:
                key, _, value = line.partition(":")
                info[key.strip()] = value.strip()
        return info
    except FileNotFoundError:
        return {"Package": name, "Status": "unknown"}


def list_installed() -> list[str]:
    """List installed packages."""
    data = load_packages()
    return data["installed"]


if __name__ == "__main__":
    print("💚 CripOS Package Manager")
    print("=" * 35)
    print(f"  Installed: {len(list_installed())} packages")
    print("  Use: python -m system.package_manager install <name>")