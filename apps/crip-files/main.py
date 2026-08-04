#!/usr/bin/env python3
"""Crip Files - a simple file manager application for CripOS."""

import os
import tkinter as tk
from tkinter import ttk


class CripFilesWindow:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Crip Files")
        self.root.geometry("700x460")
        self.root.configure(bg="#161B22")

        self.current_dir = os.path.expanduser("~")

        toolbar = tk.Frame(root, bg="#161B22")
        toolbar.pack(fill="x", padx=12, pady=(12, 6))

        tk.Label(toolbar, text="Crip Files", fg="#F0F6FC", bg="#161B22", font=("Segoe UI", 14, "bold")).pack(side="left")

        self.path_var = tk.StringVar(value=self.current_dir)
        tk.Entry(toolbar, textvariable=self.path_var, width=60).pack(side="left", padx=8)
        tk.Button(toolbar, text="Open", bg="#39D353", fg="#0D1117", relief="flat", command=self.open_path).pack(side="left")

        self.tree = ttk.Treeview(root, columns=("type", "size"), show="headings")
        self.tree.heading("#0", text="Name")
        self.tree.heading("type", text="Type")
        self.tree.heading("size", text="Size")
        self.tree.column("#0", width=320)
        self.tree.column("type", width=120)
        self.tree.column("size", width=100)
        self.tree.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        self.load_directory(self.current_dir)

    def open_path(self) -> None:
        self.load_directory(self.path_var.get())

    def load_directory(self, path: str) -> None:
        self.tree.delete(*self.tree.get_children())
        self.current_dir = path
        self.path_var.set(path)

        try:
            entries = sorted(os.listdir(path), key=lambda item: item.lower())
        except OSError:
            self.tree.insert("", "end", values=("Permission denied", "", ""))
            return

        for name in entries:
            full_path = os.path.join(path, name)
            if os.path.isdir(full_path):
                self.tree.insert("", "end", text=name, values=("Folder", ""))
            else:
                size = os.path.getsize(full_path)
                self.tree.insert("", "end", text=name, values=("File", str(size)))


def run_files() -> None:
    root = tk.Tk()
    CripFilesWindow(root)
    root.mainloop()


if __name__ == "__main__":
    run_files()
