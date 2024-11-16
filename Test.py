import socket
from kivy.core.audio import SoundLoader

sound = SoundLoader.load('Zvezda.mp3')
sound.play()
print("Воспроизведение...")

test = input("Введите v для тестировки создания сервера")

if test == "v":
    host = '0.0.0.0'
    port = 12345

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen()

        print("Успешно!")
    except PermissionError:
        print("Ошибка")