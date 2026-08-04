#!/usr/bin/env python3
"""Graphical UI for Crip Center."""

import tkinter as tk


def run_center() -> None:
    root = tk.Tk()
    root.title("Crip Center")
    root.geometry("460x360")
    root.configure(bg="#161B22")

    tk.Label(
        root,
        text="Crip Center",
        fg="#F0F6FC",
        bg="#161B22",
        font=("Segoe UI", 16, "bold"),
    ).pack(pady=(20, 10))

    for section in ["Appearance", "Network", "Updates", "Security", "About"]:
        tk.Button(
            root,
            text=section,
            bg="#39D353",
            fg="#0D1117",
            relief="flat",
            padx=10,
            pady=6,
            command=lambda s=section: print(f"Open {s}"),
        ).pack(fill="x", padx=20, pady=4)

    root.mainloop()
