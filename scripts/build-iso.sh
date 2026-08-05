#!/bin/bash
set -euo pipefail

echo "================================="
echo "      CripOS ISO Builder"
echo "================================="

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_DIR="$REPO_ROOT/build/iso"
WORK_DIR="$BUILD_DIR/work"
OUTPUT_ISO="$BUILD_DIR/cripos-alpha.iso"
VERSION="0.1-alpha"
CODENAME="Creeper"

# Check for required tools
for tool in mkisofs xorriso; do
  if ! command -v "$tool" &>/dev/null; then
    echo "ERROR: $tool is not installed. Please install it first."
    exit 1
  fi
done

echo "Creating build directories..."
rm -rf "$WORK_DIR"
mkdir -p "$WORK_DIR"

echo "Copying CripOS files..."
cp -a "$REPO_ROOT"/. "$WORK_DIR"/

echo "Setting up boot structure..."
mkdir -p "$WORK_DIR/boot/grub"
mkdir -p "$WORK_DIR/boot/plymouth"

# Plymouth theme
cat > "$WORK_DIR/boot/plymouth/cripos.plymouth" <<'EOF'
[Plymouth Theme]
Name=CripOS
Description=CripOS Boot Splash
ModuleName=script
[script]
ImageDir=/usr/share/plymouth/themes/cripos
ScriptFile=/usr/share/plymouth/themes/cripos/cripos.script
EOF

cat > "$WORK_DIR/boot/plymouth/cripos.script" <<'EOF'
# CripOS Plymouth boot script
fun = 0;
window.SetBackgroundColor (0.05, 0.07, 0.09);
logo = Image ("cripos-logo.png");
logo_sprite = Sprite (logo);
logo_sprite.SetX (Window.GetWidth () / 2 - logo.GetWidth () / 2);
logo_sprite.SetY (Window.GetHeight () / 2 - logo.GetHeight () / 2);
EOF

# GRUB config with branding
cat > "$WORK_DIR/boot/grub/grub.cfg" <<EOF
set timeout=5
set default=0
set menu_color_normal=cyan/blue
set menu_color_highlight=white/blue

menuentry "CripOS $VERSION ($CODENAME)" {
    linux /boot/vmlinuz root=/dev/sda1 ro quiet splash
    initrd /boot/initrd.img
}

menuentry "CripOS Recovery Mode" {
    linux /boot/vmlinuz root=/dev/sda1 ro single
    initrd /boot/initrd.img
}

menuentry "Memory Test" {
    linux /boot/memtest86+
}
EOF

# OS release branding
cat > "$WORK_DIR/etc/os-release" <<EOF
PRETTY_NAME="CripOS $VERSION ($CODENAME)"
NAME="CripOS"
VERSION_ID="$VERSION"
VERSION_CODENAME="$CODENAME"
ID=cripos
ID_LIKE=debian
HOME_URL="https://github.com/creperman737/CripOS"
SUPPORT_URL="https://github.com/creperman737/CripOS/issues"
BUG_REPORT_URL="https://github.com/creperman737/CripOS/issues"
EOF

echo "Building ISO image..."
xorriso -as mkisofs \
  -o "$OUTPUT_ISO" \
  -V "CripOS $VERSION" \
  -J -R \
  -b boot/grub/grub.cfg \
  -no-emul-boot \
  -boot-load-size 4 \
  -boot-info-table \
  "$WORK_DIR"

echo "Generating SHA256 checksum..."
(cd "$BUILD_DIR" && sha256sum cripos-alpha.iso > cripos-alpha.iso.sha256)

echo "================================="
echo "ISO built successfully:"
echo "  $OUTPUT_ISO"
echo "  SHA256: $(cat "$BUILD_DIR/cripos-alpha.iso.sha256" | awk '{print $1}')"
echo "================================="