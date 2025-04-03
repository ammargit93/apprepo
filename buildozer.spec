[app]
title = Hello World
package.name = helloworld
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,ttf  # Add common asset extensions
version = 0.1
requirements = python3==3.8.9, kivy==2.2.1, kivymd==1.1.1, openssl  # Explicit Python 3.8.9
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.arch = arm64-v8a  # Poco C31 uses ARM64
android.api = 31
android.minapi = 21
android.ndk = 23b  # NDK 23b is more stable for Kivy
android.sdk = 33
android.accept_sdk_license = True

# Improve build speed & reduce APK size
android.no_compress = lib/*.so, *.py  # Skip recompression (faster builds)
p4a.branch = develop  # Use latest python-for-android fixes

# (Optional) Enable OpenGL ES 2 for better performance
osx.kivy_version = 2.2.1
fullscreen = 0
log_level = 2
warn_on_root = 1
