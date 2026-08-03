#!/bin/bash

echo "================================="
echo "      Welcome to CripOS"
echo "================================="

sudo apt update

echo "Installing base packages..."

sudo apt install -y \
git \
curl \
wget \
vim \
htop \
neofetch

echo "Installing Cinnamon..."

sudo apt install -y task-cinnamon-desktop

echo "Installing LightDM..."

sudo apt install -y lightdm

echo "Installation Complete!"
