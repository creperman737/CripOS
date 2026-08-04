#!/usr/bin/env python3
"""Reusable widgets for the CripOS SDK."""


def card(title: str) -> str:
    """Render a card widget."""
    return f"[card] {title}"


def window(title: str, width: int = 640, height: int = 480) -> str:
    """Render a window widget."""
    return f"[window] {title} ({width}x{height})"


def dialog(title: str, message: str) -> str:
    """Render a dialog widget."""
    return f"[dialog] {title}: {message}"


def toast(message: str) -> str:
    """Render a toast notification."""
    return f"[toast] {message}"


def sidebar(items: list[str]) -> str:
    """Render a sidebar widget."""
    return f"[sidebar] {', '.join(items)}"


def toolbar(items: list[str]) -> str:
    """Render a toolbar widget."""
    return f"[toolbar] {', '.join(items)}"