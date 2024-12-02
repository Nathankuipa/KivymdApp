[app]
# (str) Title of your application
title = MyApp

# (str) Package name
package.name = myapp

# (str) Package domain
package.domain = org.myapp

# (str) Source code where the main.py file is located
source.dir = .

# (str) Application versioning (method 1)
version = 0.1

# (str) Supported screen orientations: landscape, portrait or all
orientation = portrait

# (list) Permissions
# For example, if you need Internet, add 'INTERNET'
android.permissions = INTERNET

# (str) The name of the entry point .py file
# e.g., main.py
source.include_exts = py,png,jpg,kv,atlas

# (list) Include any additional files (like a README)
# Add file paths here (separate by a comma)
source.include_patterns = assets/*,data/*

# (list) Include any additional directories to package (like libs)
# Example:
# source.include_dirs = path/to/your/directory

# (str) Path to the icon of your app (used in the APK)
icon.filename = %(source.dir)s/data/icon.png

# (str) Path to the landscape mode icon of your app
# If not set, the main icon will be used
# icon.filename.landscape = 

# (list) Supported platforms
# Add "android" to build APK
osx.python_version = 3.10

[buildozer]
# (str) The Android SDK directory
android.sdk_path = $HOME/android-sdk

# (str) The Android NDK directory
android.ndk_path = $HOME/.buildozer/android/platform/android-ndk-r21e

# (int) Minimum API level for your application
android.minapi = 21

# (int) Target API level
android.api = 33

# (str) Build tools version
android.build_tools_version = 33.0.0

# (str) The Android bootstrap to use
# 'sdl2' is the default
android.bootstrap = sdl2

# (list) Requirements for this app
# Include any Python packages or Kivy libraries your app needs
requirements = python3,kivy

# (str) The package to use as the main entry point for the app
android.entrypoint = org.kivy.android.PythonActivity

# (str) Extra Java jars
# e.g., custom Java code
android.add_jars = 

# (str) Extra source files
android.add_src = 

# (str) Extra compile options
android.add_compile_options = 

# (list) Additional libraries
android.add_libraries = 

# (list) Additional assets
android.add_assets = 

# (str) Java heap size
# Larger applications may require this to prevent memory issues
android.java_opts = -Xmx1024m

# (bool) Copy external libraries into the APK
# Default is True
android.copy_libs = 1

# (bool) Add the whole NDK directory to PATH when building
# Default is True
android.add_ndk_to_path = 1 
