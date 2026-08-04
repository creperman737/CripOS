#!/bin/bash
set -euo pipefail

echo "================================="
echo "      CripOS ISO Builder"
echo "================================="

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_DIR="$REPO_ROOT/build/iso"
WORK_DIR="$BUILD_DIR/work"
OUTPUT_ISO="$BUILD_DIR/cripos-alpha.iso"

# Check for required tools
for tool in mkisofs xorriso; do
  if ! command -v "$tool" &>/dev/null; then
    echo "ERROR: $tool is not installed. Please install it first."
    exit 1
  fi
done

echo "Creating build directories..."
mkdir -p "$WORK_DIR"

echo "Copying CripOS files..."
cp -a "$REPO_ROOT"/. "$WORK_DIR"/

echo "Setting up boot structure..."
mkdir -p "$WORK_DIR/boot/grub"

cat > "$WORK_DIR/boot/grub/grub.cfg" <<'EOF'
set timeout=5
set default=0

menuentry "CripOS Alpha" {
    linux /boot/vmlinuz root=/dev/sda1 ro quiet splash
    initrd /boot/initrd.img
}

menuentry "CripOS Recovery Mode" {
    linux /boot/vmlinuz root=/dev/sda1 ro single
    initrd /boot/initrd.img
}
EOF

echo "Building ISO image..."
xorriso -as mkisofs \
  -o "$OUTPUT_ISO" \
  -V "CripOS Alpha" \
  -J -R \
  -b boot/grub/grub.cfg \
  -no-emul-boot \
  -boot-load-size 4 \
  -boot-info-table \
  "$WORK_DIR"

echo "================================="
echo "ISO built successfully:"
echo "  $OUTPUT_ISO"
echo "================================="