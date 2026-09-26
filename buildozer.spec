[app]

# App name
title = Mari App

# Package name
package.name = mariapp

# Package domain
package.domain = com.mari.app

# Source code dir
source.dir =.

# Source files
source.include_exts = py,png,jpg,kv,atlas,json

# Main file
source.main = main.py

# Requirements
requirements = python3,kivy

# Version
version = 0.1

# Orientation - portrait or landscape or sensor
orientation = portrait

# Fullscreen
fullscreen = 0

[buildozer]

# Log level 2 = debug
log_level = 2

# Allow root
warn_on_root = 0

[app:requirements]

[app:android]

# Accept licenses
android.accept_sdk_license_agreements = True

# API levels
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33

# Permissions
android.permissions = INTERNET

# Arch - use armeabi-v7a for fast build
android.archs = armeabi-v7a

# Build type
p4a.bootstrap = sdl2
