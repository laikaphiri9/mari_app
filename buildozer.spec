[app]
title = Mari App
package.name = mariapp
package.domain = com.mari.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
source.main = main.py
requirements = python3,kivy
version = 0.1
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 0

[app:requirements]

[app:android]
android.accept_sdk_license_agreements = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.permissions = INTERNET
android.archs = armeabi-v7a
p4a.bootstrap = sdl2
