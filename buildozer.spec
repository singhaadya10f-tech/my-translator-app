[app]
title = MyTranslator
package.name = mytranslator
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,googletrans==4.0.0-rc1,gtts,legacy-cgi
orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk_api = 21
android.private_storage = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
