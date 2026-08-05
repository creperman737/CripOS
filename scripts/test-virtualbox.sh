#!/bin/bash
set -euo pipefail

echo "================================="
echo " CripOS VirtualBox Test Runner"
echo "================================="

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ISO="$REPO_ROOT/build/iso/cripos-alpha.iso"
VM_NAME="CripOS-Alpha"
RAM="${RAM:-2048}"
VRAM="${VRAM:-128}"
DISK_SIZE="${DISK_SIZE:-8192}"

# Check for required tools
for tool in VBoxManage; do
  if ! command -v "$tool" &>/dev/null; then
    echo "ERROR: $tool is not installed. Install VirtualBox."
    exit 1
  fi
done

if [ ! -f "$ISO" ]; then
  echo "ERROR: ISO not found. Run scripts/build-iso.sh first."
  exit 1
fi

echo "Creating VirtualBox VM: $VM_NAME"

# Remove existing VM if present
if VBoxManage showvminfo "$VM_NAME" &>/dev/null; then
  echo "Removing existing VM..."
  VBoxManage unregistervm "$VM_NAME" --delete
fi

VBoxManage createvm --name "$VM_NAME" --ostype Debian_64 --register

VBoxManage modifyvm "$VM_NAME" \
  --memory "$RAM" \
  --vram "$VRAM" \
  --cpus 2 \
  --nic1 nat \
  --graphicscontroller vmsvga \
  --audio-enabled on \
  --audio-driver default

VBoxManage createmedium disk \
  --filename "$REPO_ROOT/build/iso/$VM_NAME.vdi" \
  --size "$DISK_SIZE" \
  --format VDI

VBoxManage storagectl "$VM_NAME" \
  --name "SATA" \
  --add sata \
  --controller IntelAhci

VBoxManage storageattach "$VM_NAME" \
  --storagectl "SATA" \
  --port 0 \
  --device 0 \
  --type hdd \
  --medium "$REPO_ROOT/build/iso/$VM_NAME.vdi"

VBoxManage storagectl "$VM_NAME" \
  --name "IDE" \
  --add ide

VBoxManage storageattach "$VM_NAME" \
  --storagectl "IDE" \
  --port 0 \
  --device 0 \
  --type dvddrive \
  --medium "$ISO"

VBoxManage modifyvm "$VM_NAME" --boot1 dvd --boot2 disk

echo "Starting VM: $VM_NAME"
echo "  ISO : $ISO"
echo "  RAM : ${RAM}MB"
echo "  Disk: ${DISK_SIZE}MB"
echo "================================="

VBoxManage startvm "$VM_NAME"