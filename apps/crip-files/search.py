#!/usr/bin/env python3
"""Search helpers for Crip Files."""


def search_items(query: str) -> list[str]:
    return [f"match: {query}"] if query else []
