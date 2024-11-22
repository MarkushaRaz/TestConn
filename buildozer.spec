[app]
# Имя вашего приложения
title = Beta: Anti-Totality

# Пакетное имя (должно быть уникальным)
package.name = test
package.domain = org.example

# Главный файл приложения
source.dir = .
source.include_exts = py,kv,atlas,All/*.mp3
source.exclude_exts = Main.py,Client.py,spec

# Версия вашего приложения
version = 1.0


# Replace text after the build.gradle file is generated
p4a.replacements = "s/jcenter()/mavenCentral()/g"


# Требования (зависимости, которые необходимо включить)
requirements = kivy

# Минимальная версия Android API
android.api = 31

# Минимальная версия NDK
android.ndk = 25b

# Минимальная версия SDK
android.sdk = 31

# Платформы для сборки
android.archs = arm64-v8a, armeabi-v7a

# Архив ресурсов
android.include_exts = mp3,ogg,wav,ttf,png,jpg

# Название файла APK
android.debug_keystore = %(source.dir)s/debug.keystore
android.debug_keystore_passwd = android
android.debug_key_alias = androiddebugkey

[buildozer]
# Логи
log_level = 2
warn_on_root = 1

# Целевая платформа
target = android

# Custom build.gradle
android.gradle_dependencies = com.android.tools.build:gradle:8.1.1
android.gradle_settings_path = ./custom_build.gradle