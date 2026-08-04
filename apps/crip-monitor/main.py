#!/usr/bin/env python3
"""Crip Monitor - lightweight system monitoring panel."""

import tkinter as tk


class MonitorWindow:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Crip Monitor")
        self.root.geometry("480x360")
        self.root.configure(bg="#161B22")

        tk.Label(
            root,
            text="Crip Monitor",
            fg="#F0F6FC",
            bg="#161B22",
            font=("Segoe UI", 16, "bold"),
        ).pack(pady=(20, 10))

        metrics = ["CPU Usage", "RAM Usage", "GPU Usage", "Disk Usage", "Network", "Processes", "Temperature"]
        for metric in metrics:
            tk.Label(
                root,
                text=metric,
                fg="#39D353",
                bg="#161B22",
                font=("Segoe UI", 11),
            ).pack(anchor="w", padx=24, pady=3)


def run_monitor() -> None:
    root = tk.Tk()
    MonitorWindow(root)
    root.mainloop()


if __name__ == "__main__":
    run_monitor()
