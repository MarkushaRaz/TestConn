[app]
# Имя вашего приложения
title = Beta: Deshit

# Пакетное имя (должно быть уникальным)
package.name = test
package.domain = org.example

# Главный файл приложения
source.dir = .
source.include_exts = main.py,kv,atlas,All/*.mp3
source.exclude_exts = Main.py,Client.py,spec

# Версия вашего приложения
version = 1.0

# Требования (зависимости, которые необходимо включить)
requirements = kivy

# Минимальная версия Android API
android.api = 31

# Минимальная версия NDK
android.ndk = 25

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
