#!/usr/bin/env python3
"""System settings helpers for Crip Center."""

import platform
import socket


def get_system_info() -> str:
    return f"System: {platform.system()}\nVersion: {platform.version()}\nMachine: {platform.machine()}\nHostname: {socket.gethostname()}"
