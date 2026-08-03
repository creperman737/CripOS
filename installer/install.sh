#!/bin/bash

echo "CripOS Installer"
echo "================"

echo "Starting installation..."

if command -v sudo >/dev/null 2>&1; then
  echo "Sudo detected."
else
  echo "Sudo is required for installation."
  exit 1
fi

bash ../packages/cripos-base.sh

echo "Installation completed."
