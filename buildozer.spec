[app]

# (str) Title of your application
title = My Pydroid App

# (str) Package name (no spaces or special characters)
package.name = mypydroidapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (add ext extensions if you have audio/fonts)
source.include_exts = py,png,jpg,kv,atlas,ttf,wav,mp3

# (list) Application requirements
# Comma separated e.g. requirements = sqlite3,kivy,requests
requirements = python3,kivy

# (str) Application versioning
version = 0.1

# (list) Permissions
# android.permissions = INTERNET

# (int) Target Android API, should be 33 or 34 for modern builds
android.api = 33

# (int) Minimum API required (21 = Android 5.0)
android.minapi = 21

# (str) Android NDK version (leave blank to let python-for-android select recommended version)
# android.ndk = 25b

# (bool) Automatically accept Android SDK licenses
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) If True, then skip try to update the Android sdk apps
android.skip_update = False

# (bool) If True, then automatically connect to the USB device
android.entrypoint = org.kivy.android.PythonActivity

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (full output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = disable)
warn_on_root = 1
