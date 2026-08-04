#!/usr/bin/env python3
"""CripOS splash text - Minecraft-inspired random messages."""

import random

SPLASH_TEXTS = [
    "Never Gives Up!",
    "Gaming Ready!",
    "Powered by Debian!",
    "Crafted with ❤️",
    "Hello, Criperman!",
    "Let's Build Something!",
    "Time to Play!",
    "Creeper approved!",
    "Ready to mine!",
    "Diamonds not included.",
    "Welcome back!",
    "Code. Build. Play.",
    "Powered by Open Source.",
    "Loading creativity...",
    "Keep building!",
    "Don't dig straight down!",
    "Today is a good day to code!",
    "Never Give Up. Never Surrender.",
    "Built with Python!",
    "Alpha 0.1 - Creeper Edition!",
    "Mining for innovation!",
    "Craft your future!",
    "Redstone powered!",
    "Spawn point: CripOS!",
    "More than just a mod!",
]


def get_splash_text() -> str:
    """Return a random CripOS splash text."""
    return random.choice(SPLASH_TEXTS)


def get_all_splash_texts() -> list[str]:
    """Return all splash texts."""
    return SPLASH_TEXTS.copy()


if __name__ == "__main__":
    print(get_splash_text())