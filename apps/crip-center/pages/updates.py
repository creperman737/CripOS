#!/usr/bin/env python3
"""Updates settings page for Crip Center."""

from api.updates import get_update_status


def show_page() -> None:
    status = get_update_status()
    print("🔄 System Updates")
    print("=" * 30)
    print(f"Channel     : {status.get('channel', 'alpha')}")
    print(f"Last Check  : {status.get('last_check', 'Never')}")
    print(f"Available   : {status.get('available', 0)} update(s)")


if __name__ == "__main__":
    show_page()
