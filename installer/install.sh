#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INSTALL_ROOT="/opt/cripos"
CONFIG_DIR="/etc/cripos"
DESKTOP_ENTRY="/usr/share/applications/crip-welcome.desktop"
AUTOSTART_ENTRY="/etc/xdg/autostart/crip-welcome.desktop"

if [[ ${EUID:-$(id -u)} -ne 0 ]]; then
  echo "Please run this installer as root or with sudo."
  exit 1
fi

echo "================================="
echo "      Welcome to CripOS"
echo "================================="

echo "Updating package index..."
apt-get update

echo "Installing base system packages..."
apt-get install -y \
  python3 \
  python3-tk \
  ca-certificates \
  git \
  curl \
  wget \
  vim \
  htop \
  neofetch \
  xdg-utils

echo "Installing a lightweight desktop stack..."
apt-get install -y task-cinnamon-desktop lightdm

echo "Installing CripOS files..."
mkdir -p "$INSTALL_ROOT" "$CONFIG_DIR"
rm -rf "$INSTALL_ROOT"
mkdir -p "$INSTALL_ROOT"
cp -a "$REPO_ROOT"/. "$INSTALL_ROOT"/

cat > "$CONFIG_DIR/config.json" <<'EOF'
{
  "language": "uz",
  "completed": false,
  "internet": true,
  "updates": false
}
EOF

cat > "$DESKTOP_ENTRY" <<EOF
[Desktop Entry]
Name=Crip Welcome
Comment=First-run experience for CripOS
Exec=/usr/local/bin/crip-welcome
Icon=/opt/cripos/apps/crip-welcome/assets/logo.png
Terminal=false
Type=Application
Categories=System;Utility;
EOF

mkdir -p "$(dirname "$AUTOSTART_ENTRY")"
cp "$DESKTOP_ENTRY" "$AUTOSTART_ENTRY"

ln -sf "$INSTALL_ROOT/apps/crip-welcome/main.py" /usr/local/bin/crip-welcome
chmod +x /usr/local/bin/crip-welcome "$INSTALL_ROOT/apps/crip-welcome/main.py"

echo "Installation complete."
echo "Run 'crip-welcome' to start the first boot experience."
