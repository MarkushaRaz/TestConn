import socket
import threading

host = '0.0.0.0'
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

while True:
    client, address = server.accept()

    def InData():
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if not message:
                    break
            except ConnectionResetError:
                print("Successful disconnect")
                break

        client.close()

    client_thread = threading.Thread(target=InData)
    client_thread.start()
    print(f"Successful connections: {threading.active_count() - 1}")