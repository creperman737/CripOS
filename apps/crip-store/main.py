#!/usr/bin/env python3
"""Crip Store entrypoint."""

from install import install_app


if __name__ == "__main__":
    app = input("Enter app name to install: ").strip()
    install_app(app)
