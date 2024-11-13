import socket

host = '0.0.0.0'
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
    print("> Successful connect")
    break