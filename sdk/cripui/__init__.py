#!/usr/bin/env python3
"""CripUI package for CripOS applications."""


def button(text: str) -> str:
    """Render a button element."""
    return f"[button] {text}"


def label(text: str) -> str:
    """Render a label element."""
    return f"[label] {text}"


def input_field(placeholder: str = "") -> str:
    """Render an input field element."""
    return f"[input] {placeholder}"


def checkbox(text: str, checked: bool = False) -> str:
    """Render a checkbox element."""
    mark = "x" if checked else " "
    return f"[checkbox] [{mark}] {text}"


def dropdown(options: list[str]) -> str:
    """Render a dropdown element."""
    return f"[dropdown] {', '.join(options)}"


def progress_bar(value: int, maximum: int = 100) -> str:
    """Render a progress bar element."""
    percent = int((value / maximum) * 100) if maximum > 0 else 0
    filled = "█" * (percent // 10)
    empty = "░" * (10 - percent // 10)
    return f"[progress] {filled}{empty} {percent}%"