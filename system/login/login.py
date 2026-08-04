#!/usr/bin/env python3
"""CripOS login manager."""

import getpass
import hashlib
import json
import os
from pathlib import Path

CONFIG_DIR = Path("/etc/cripos")
USERS_FILE = CONFIG_DIR / "users.json"


def load_users() -> dict:
    """Load user database."""
    try:
        with USERS_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"users": []}


def save_users(users: dict) -> None:
    """Save user database."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with USERS_FILE.open("w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)


def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def create_user(username: str, password: str) -> bool:
    """Create a new user."""
    users = load_users()
    if any(u["username"] == username for u in users["users"]):
        return False
    users["users"].append({
        "username": username,
        "password_hash": hash_password(password),
        "created": True,
    })
    save_users(users)
    return True


def authenticate(username: str, password: str) -> bool:
    """Authenticate a user."""
    users = load_users()
    password_hash = hash_password(password)
    return any(
        u["username"] == username and u["password_hash"] == password_hash
        for u in users["users"]
    )


def run_login() -> bool:
    """Run the login flow."""
    print("CripOS Login")
    print("============")

    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")

    if authenticate(username, password):
        print(f"Welcome, {username}!")
        return True

    print("Invalid username or password.")
    return False


if __name__ == "__main__":
    run_login()