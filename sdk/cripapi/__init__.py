#!/usr/bin/env python3
"""CripAPI package for CripOS applications."""


def system_status() -> dict:
    """Return the current system status."""
    return {"name": "CripOS", "status": "ready"}


def system_info() -> dict:
    """Return detailed system information."""
    return {
        "name": "CripOS",
        "version": "Alpha 0.1",
        "codename": "Creeper",
        "base": "Debian 13 (Trixie)",
        "desktop": "Cinnamon",
        "kernel": "Linux",
        "architecture": "x86_64",
    }


def get_apps() -> list[str]:
    """Return a list of installed CripOS applications."""
    return [
        "Crip Welcome",
        "Crip Launcher",
        "Crip Center",
        "Crip Store",
        "Crip Update",
        "Crip Files",
        "Crip Terminal",
        "Crip Monitor",
        "Crip Installer",
    ]


def get_version() -> str:
    """Return the CripOS version string."""
    return "CripOS 0.1 Alpha"