#!/usr/bin/env python3
"""CripOS service manager."""

import subprocess
from pathlib import Path

SERVICES = [
    "crip-network.service",
    "crip-notify.service",
    "crip-power.service",
    "crip-update.service",
    "crip-wallpaper.service",
    "crip-ai.service",
]


def get_service_status(service: str) -> str:
    """Get the status of a service."""
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service],
            check=False,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()
    except FileNotFoundError:
        return "unknown"


def list_services() -> list[dict]:
    """List all CripOS services and their status."""
    services = []
    for service in SERVICES:
        services.append({
            "name": service,
            "status": get_service_status(service),
        })
    return services


def start_service(service: str) -> bool:
    """Start a service."""
    try:
        subprocess.run(
            ["systemctl", "start", service],
            check=False,
            capture_output=True,
        )
        return True
    except FileNotFoundError:
        return False


def stop_service(service: str) -> bool:
    """Stop a service."""
    try:
        subprocess.run(
            ["systemctl", "stop", service],
            check=False,
            capture_output=True,
        )
        return True
    except FileNotFoundError:
        return False


def restart_service(service: str) -> bool:
    """Restart a service."""
    try:
        subprocess.run(
            ["systemctl", "restart", service],
            check=False,
            capture_output=True,
        )
        return True
    except FileNotFoundError:
        return False


if __name__ == "__main__":
    print("CripOS Services")
    print("===============")
    for svc in list_services():
        status = svc["status"]
        print(f"{svc['name']}: {status}")