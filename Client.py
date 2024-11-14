import socket

host = '0.0.0.0'
port = 12345

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    print("> Successful connect")
except ConnectionRefusedError:
    print("> Error connect")