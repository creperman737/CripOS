#!/usr/bin/env python3
"""crip-doctor - diagnose CripOS system health."""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.boot.boot import check_disk_space, check_memory
from system.security.security import run_security_check
from system.updates.updates import check_updates


def check_structure() -> list:
    """Check the repository structure."""
    expected = ["apps", "sdk", "api", "system", "services", "libs", "themes", "docs"]
    results = []
    for folder in expected:
        exists = (REPO_ROOT / folder).exists()
        results.append((f"Directory '{folder}'", exists))
    return results


def run_doctor() -> None:
    """Run all health checks and print results."""
    print("💚 CripOS Doctor")
    print("=" * 35)
    print("  Diagnosing system health...\n")

    issues = []

    # 1. Check structure
    print("Structure:")
    for name, ok in check_structure():
        status = "✅" if ok else "❌"
        print(f"  {status} {name}")
        if not ok:
            issues.append(f"Missing directory: {name}")

    # 2. Check boot requirements
    print("\nBoot Health:")
    disk = check_disk_space()
    memory = check_memory()
    print(f"  {'✅' if disk else '⚠️'} Disk space check")
    print(f"  {'✅' if memory else '⚠️'} Memory check")
    if not disk:
        issues.append("Insufficient disk space")
    if not memory:
        issues.append("Insufficient memory")

    # 3. Check security
    print("\nSecurity:")
    try:
        security = run_security_check()
        for key, value in security.items():
            print(f"  {'✅' if value else '⚠️'} {key}: {'enabled' if value else 'disabled'}")
            if not value:
                issues.append(f"Security feature disabled: {key}")
    except Exception as e:
        print(f"  ⚠️ Security check failed: {e}")

    # 4. Check updates
    print("\nUpdates:")
    try:
        status = check_updates()
        print(f"  ✅ Channel: {status.get('channel', 'alpha')}")
        print(f"  {'✅' if status.get('available', 0) == 0 else '⚠️'} {status.get('available', 0)} updates available")
    except Exception as e:
        print(f"  ⚠️ Update check failed: {e}")

    # 5. Check configs
    print("\nConfigs:")
    for config in ["config", "branding", "build"]:
        ok = (REPO_ROOT / config).exists()
        print(f"  {'✅' if ok else '⚠️'} {config}/")
        if not ok:
            issues.append(f"Missing directory: {config}")

    # Summary
    print("\n" + "=" * 35)
    if issues:
        print(f"  Found {len(issues)} issue(s):")
        for issue in issues:
            print(f"    ⚠️ {issue}")
    else:
        print("  ✅ CripOS system health: PERFECT!")
    print("=" * 35)


if __name__ == "__main__":
    run_doctor()