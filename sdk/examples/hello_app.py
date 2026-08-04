#!/usr/bin/env python3
"""Example CripOS SDK app."""

from sdk.cripui import button
from sdk.cripapi import system_status


print(button("Hello from CripOS"))
print(system_status())
