[app]
title = Hello World
package.name = helloworld
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,ttf
version = 0.1
requirements = python3==3.8.9,kivy==2.2.1,kivymd==1.1.1,openssl
orientation = portrait
fullscreen = 0  # Only one instance of this parameter
android.permissions = INTERNET
android.arch = arm64-v8a
android.api = 31
android.minapi = 21
android.ndk = 23b
android.sdk = 33
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
