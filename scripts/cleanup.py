import pathlib

# Remove duplicate package list
dup = pathlib.Path("build/iso/live-build/config/package-lists/crip-desktop.list.chroot")
if dup.exists():
    dup.unlink()
    print("Deleted: crip-desktop.list.chroot (duplicate)")
else:
    print("Already clean: crip-desktop.list.chroot not found")

# Verify remaining files
pkg_dir = pathlib.Path("build/iso/live-build/config/package-lists")
for f in pkg_dir.iterdir():
    print(f"  Package list: {f.name}")

# Check for XML artifacts (avoid literal XML in source)
artifact = chr(60) + "/arg" + chr(62) + chr(125) + chr(41)
artifact2 = chr(60) + "task_progress"
for f in [
    "scripts/build-iso.sh",
    "build/iso/live-build/config/hooks/normal/01-cripos.chroot",
    "build/iso/live-build/config/package-lists/cripos-desktop.list.chroot",
    "build/iso/live-build/config/includes.chroot/etc/lightdm/lightdm.conf.d/50-cripos.conf",
]:
    content = pathlib.Path(f).read_text()
    if artifact in content or artifact2 in content:
        print(f"  BAD: {f} has XML artifact")
    else:
        print(f"  OK: {f}")
</arg_value></tool_call>