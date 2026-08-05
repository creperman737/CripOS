#!/bin/bash
set -euo pipefail

echo "================================="
echo "   CripOS QEMU Test Runner"
echo "================================="

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ISO="$REPO_ROOT/build/iso/cripos-alpha.iso"
DISK="$REPO_ROOT/build/iso/cripos-test.qcow2"
RAM="${RAM:-2048}"
CORES="${CORES:-2}"

# Check for required tools
for tool in qemu-system-x86_64; do
  if ! command -v "$tool" &>/dev/null; then
    echo "ERROR: $tool is not installed. Install qemu-system-x86."
    exit 1
  fi
done

if [ ! -f "$ISO" ]; then
  echo "ERROR: ISO not found. Run scripts/build-iso.sh first."
  exit 1
fi

echo "Creating test disk (8GB)..."
if [ ! -f "$DISK" ]; then
  qemu-img create -f qcow2 "$DISK" 8G
fi

echo "Booting CripOS in QEMU..."
echo "  ISO : $ISO"
echo "  RAM : ${RAM}MB"
echo "  CPU : $CORES cores"
echo "  Disk: $DISK"
echo ""
echo "Press Ctrl+Alt+G to release mouse."
echo "================================="

qemu-system-x86_64 \
  -m "$RAM" \
  -smp "$CORES" \
  -cdrom "$ISO" \
  -hda "$DISK" \
  -boot d \
  -enable-kvm \
  -cpu host \
  -vga virtio \
  -display gtk \
  -netdev user,id=net0 \
  -device e1000,netdev=net0 \
  -usb \
  -device usb-tablet