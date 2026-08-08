#!/usr/bin/env python3
"""Cleanup CripOS build config files: remove duplicate package lists and
strip leaked AI-agent tool-call XML (a recurring Cline artifact)."""

import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]

ARTIFACT_MARKERS = [
    "</arg_value>",
    "<task_progress>",
    "</tool_call>",
]

WATCHED_FILES = [
    "scripts/build-iso.sh",
    "build/iso/live-build/config/hooks/normal/01-cripos.chroot",
    "build/iso/live-build/config/package-lists/crip-desktop.list.chroot",
    "build/iso/live-build/config/package-lists/cripos-desktop.list.chroot",
    "build/iso/live-build/config/includes.chroot/etc/lightdm/lightdm.conf.d/50-cripos.conf",
]


def clean_file(path: pathlib.Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text()
    original = text
    for marker in ARTIFACT_MARKERS:
        idx = text.find(marker)
        if idx != -1:
            text = text[:idx].rstrip("\n") + "\n"
    if text != original:
        path.write_text(text)
        return True
    return False


def main() -> None:
    dup = REPO_ROOT / "build/iso/live-build/config/package-lists/crip-desktop.list.chroot"
    if dup.exists():
        dup.unlink()
        print(f"Deleted duplicate: {dup.relative_to(REPO_ROOT)}")

    any_dirty = False
    for rel in WATCHED_FILES:
        p = REPO_ROOT / rel
        if not p.exists():
            continue
        if clean_file(p):
            print(f"  CLEANED: {rel}")
            any_dirty = True
        else:
            print(f"  OK: {rel}")

    if not any_dirty:
        print("\nHammasi toza edi.")
    else:
        print("\nTozalandi -- endi 'git diff' bilan tekshirib, commit/push qiling.")


if __name__ == "__main__":
    main()