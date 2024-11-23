[app]
# Название приложения
title = YourAppName

# Уникальное название пакета
package.name = yourapp
package.domain = org.example

# Главный файл приложения
source.dir = .
source.include_exts = py,mp3
source.exclude_exts = spec
source.exclude_dirs = tests

# Версия приложения
version = 1.0

# Требования (зависимости)
requirements = kivy

# Минимальная версия Android API
android.api = 31

# Минимальная версия NDK
android.ndk = 25

# Ресурсы
android.include_exts = mp3
android.allow_backup = 1

# Ориентация приложения
orientation = portrait

# Включить поддержку AndroidX
android.enable_androidx = True

[buildozer]
# Логи
log_level = 2
warn_on_root = 1

# Целевая платформа
target = android
