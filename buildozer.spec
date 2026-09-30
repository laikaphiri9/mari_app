[app]

# (str) Title of your application
title = My Application

# (str) Package name (lowercase alphanumeric, no spaces)
package.name = myapp

# (str) Package domain (needed for Android packaging)
package.domain = org.myapp

# (str) Source code location relative to buildozer.spec
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,ttf

# (list) List of directory to exclude
source.exclude_dirs = tests, bin, .venv, .git, .buildozer

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Comma-separated dependencies. Add python3, kivy, and any extra libraries your main.py uses (e.g., requests, pillow)
requirements = python3,kivy

# (list) Supported orientations (portrait, landscape, sensorPortrait, sensorLandscape)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions (Uncomment if your app needs Internet access)
# android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API required to install the app
android.minapi = 21

# (bool) Automatically accept SDK license
android.accept_sdk_license = True

# (str) Android NDK architecture to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Automatically keep PyGTK / PySide / Kivy app awake during run
android.wakelock = False

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = ignore, 1 = warn)
warn_on_root = 1
