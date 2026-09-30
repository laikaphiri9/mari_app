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
requirements = python3,kivy

# (list) Supported orientations (portrait, landscape, sensorPortrait, sensorLandscape)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (int) Target Android API
android.api = 33

# (int) Minimum API required to install the app
android.minapi = 21

# (str) Pin Android NDK version to r25b to prevent NDK r28c build failures
android.ndk = 25b

# (bool) Automatically accept SDK license
android.accept_sdk_license = True

# (str) Android NDK architecture to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Automatically keep app awake during run
android.wakelock = False

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
