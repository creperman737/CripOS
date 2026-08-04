#!/usr/bin/env python3
"""Crip Launcher - a simple start-menu-like interface."""

import tkinter as tk


def launch_launcher() -> None:
    root = tk.Tk()
    root.title("Crip Launcher")
    root.geometry("320x420")
    root.configure(bg="#161B22")

    tk.Label(
        root,
        text="Crip Launcher",
        fg="#F0F6FC",
        bg="#161B22",
        font=("Segoe UI", 16, "bold"),
    ).pack(pady=(20, 10))

    for label in ["Files", "Browser", "Terminal", "Settings", "Store", "Updates", "Games"]:
        tk.Button(
            root,
            text=label,
            bg="#39D353",
            fg="#0D1117",
            relief="flat",
            padx=10,
            pady=6,
            command=lambda lbl=label: print(f"Open {lbl}"),
        ).pack(fill="x", padx=20, pady=4)

    root.mainloop()


if __name__ == "__main__":
    launch_launcher()
