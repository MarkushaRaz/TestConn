import socket
from kivy.core.audio import SoundLoader

host = '0.0.0.0'
port = 12345

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    print("> Successful connect")
except ConnectionRefusedError:
    print("> Error connect")

sound = SoundLoader.load('Zvezda.mp3')
sound.play()

mess = client.recv(1024).decode('utf-8')
print(mess)