#!/bin/bash
set -euo pipefail

echo "================================="
echo "      CripOS ISO Builder"
echo "      (live-build based)"
echo "================================="

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_DIR="$REPO_ROOT/build/iso"
LIVE_BUILD_DIR="$BUILD_DIR/live-build"
OUTPUT_ISO="$BUILD_DIR/cripos-alpha.iso"
VERSION="0.1-alpha"
CODENAME="Creeper"

# Check for required tools
for tool in lb rsync; do
  if ! command -v "$tool" &>/dev/null; then
    echo "ERROR: $tool is not installed."
    echo "Install with: sudo apt install live-build rsync"
    exit 1
  fi
done

# Clean old build artifacts
echo "Cleaning old build artifacts..."
rm -rf "$LIVE_BUILD_DIR"
rm -f "$OUTPUT_ISO"
rm -f "$BUILD_DIR/cripos-alpha.iso.sha256"

echo "Setting up live-build config..."
mkdir -p "$LIVE_BUILD_DIR"

# Copy live-build config
cp -a "$REPO_ROOT/build/iso/live-build/config" "$LIVE_BUILD_DIR/config"

# Copy CripOS source code into includes.chroot (exclude build/ and .git/)
echo "Copying CripOS source code..."
mkdir -p "$LIVE_BUILD_DIR/config/includes.chroot/opt/cripos"
rsync -a \
  --exclude='build/' \
  --exclude='.git/' \
  --exclude='__pycache__/' \
  "$REPO_ROOT/" \
  "$LIVE_BUILD_DIR/config/includes.chroot/opt/cripos/"

# Copy themes
mkdir -p "$LIVE_BUILD_DIR/config/includes.chroot/usr/share/themes"
cp -a "$REPO_ROOT/themes/." "$LIVE_BUILD_DIR/config/includes.chroot/usr/share/themes/"

# Copy wallpapers
mkdir -p "$LIVE_BUILD_DIR/config/includes.chroot/usr/share/backgrounds/cripos"
cp -a "$REPO_ROOT/assets/wallpapers/." "$LIVE_BUILD_DIR/config/includes.chroot/usr/share/backgrounds/cripos/"

# Copy icons
mkdir -p "$LIVE_BUILD_DIR/config/includes.chroot/usr/share/icons/cripos"
cp -a "$REPO_ROOT/assets/icons/." "$LIVE_BUILD_DIR/config/includes.chroot/usr/share/icons/cripos/"

# Copy Plymouth theme
mkdir -p "$LIVE_BUILD_DIR/config/includes.chroot/usr/share/plymouth/themes/cripos"
cp -a "$REPO_ROOT/assets/boot/plymouth/crip-plymouth/." "$LIVE_BUILD_DIR/config/includes.chroot/usr/share/plymouth/themes/cripos/"

# Copy sounds
mkdir -p "$LIVE_BUILD_DIR/config/includes.chroot/usr/share/sounds/cripos"
cp -a "$REPO_ROOT/sounds/." "$LIVE_BUILD_DIR/config/includes.chroot/usr/share/sounds/cripos/"

# Copy login theme
mkdir -p "$LIVE_BUILD_DIR/config/includes.chroot/usr/share/lightdm/crip-login"
cp -a "$REPO_ROOT/assets/login/lightdm/crip-login/." "$LIVE_BUILD_DIR/config/includes.chroot/usr/share/lightdm/crip-login/"

# Copy branding
mkdir -p "$LIVE_BUILD_DIR/config/includes.chroot/etc/cripos"
cp "$REPO_ROOT/branding/os-release" "$LIVE_BUILD_DIR/config/includes.chroot/etc/cripos/os-release"
cp "$REPO_ROOT/branding/version.txt" "$LIVE_BUILD_DIR/config/includes.chroot/etc/cripos/version"

# Configure live-build
echo "Configuring live-build..."
cd "$LIVE_BUILD_DIR"

lb config \
  --distribution trixie \
  --debian-installer live \
  --archive-areas "main contrib non-free" \
  --architectures amd64 \
  --binary-images iso-hybrid \
  --bootappend-live "boot=live username=cripos hostname=cripos" \
  --keyring-packages "" \
  --memtest none \
  --security true \
  --updates true \
  --backports true

# Build the ISO
echo "Building ISO image (this may take 10-30 minutes)..."
sudo lb build

# Rename output
if [ -f "live-image-amd64.hybrid.iso" ]; then
  mv "live-image-amd64.hybrid.iso" "$OUTPUT_ISO"
  echo "Generating SHA256 checksum..."
  (cd "$BUILD_DIR" && sha256sum "$(basename "$OUTPUT_ISO")" > "$(basename "$OUTPUT_ISO").sha256")
  echo "================================="
  echo "ISO built successfully:"
  echo "  $OUTPUT_ISO"
  echo "  SHA256: $(cat "$BUILD_DIR/$(basename "$OUTPUT_ISO").sha256" | awk '{print $1}')"
  echo "================================="
else
  echo "ERROR: ISO build failed. Check lb build output above."
  exit 1
fi