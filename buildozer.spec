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

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to include all the files)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to include all the files)
source.exclude_dirs = tests, bin, .venv, .git, .buildozer

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Comma-separated dependencies. Add python3, kivy, and any other libraries your app uses (e.g., requests, pillow)
requirements = python3,kivy

# (str) Custom source folders for requirements
# requirements.source.kivy = ../kivy

# (list) Supported orientations (portrait, landscape, sensorPortrait, sensorLandscape)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
# Common options: INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, CAMERA
# android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API required to install the app
android.minapi = 21

# (int) Android NDK version to use
# android.ndk = 25b

# (bool) If true, accept all Android SDK licenses automatically
android.accept_sdk_license = True

# (str) Android NDK architecture to build for (e.g. armeabi-v7a, arm64-v8a, x86, x86_64)
android.archs = arm64-v8a, armeabi-v7a

# (bool) Automatically keep PyGTK / PySide / Kivy app awake during run
# android.wakelock = False

# (list) List of Java .jar files to add to the libs so that Pyobjus can access them
# android.add_jars = foo.jar,bar.jar

# (list) List of Java files to add to the android project
# android.add_src =

# (list) Android AAR archives to add
# android.add_aars =

# (str) The Android entry point, default is ok for Kivy
# android.entrypoint = org.kivy.android.PythonActivity

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = ignore, 1 = warn)
warn_on_root = 1
