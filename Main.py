import socket
import threading
from playsound import playsound

playsound("All/Zvezda.mp3")

host = '0.0.0.0'
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print("> Successful new server")

# def SendComm(client):
#     command = "adb shell stagefright -a -o Zvezda.mp3"
#     try:
#         subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
#     except subprocess.CalledProcessError:
#         print("Error")

def InData():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                break
        except ConnectionResetError:
            print("> Client disconnect")

    client.close()

while True:
    client, address = server.accept()

    client_thread = threading.Thread(target=InData)
    client_thread.start()
    print(f"> Successful connections: {threading.active_count() - 1}")

    command = input("|| ")