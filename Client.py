# import socket

# client = socket.socket()  # создаём сокет клиента
# hostname = 'codespaces-37fc1a'
# # hostname = socket.gethostname()  # получаем хост сервера
# print(hostname)
# port = 65134  # устанавливаем порт сервера
# client.connect((hostname, port))  # подключаемся к серверу
# data = client.recv(1024)  # получаем данные с сервера
# print("Server sent: ", data.decode())  # выводим данные на консоль
# client.close()  # закрываем подключение [2](https://metanit.com/python/network/1.2.php)

import socket

client = socket.socket()  # создаём сокет клиента
hostname = '127.0.0.1'  # получаем хост сервера
print("Connecting to server:", hostname)
port = 65134  # устанавливаем порт сервера

try:
    client.connect((hostname, port))  # подключаемся к серверу
    # print(client)
    data = client.recv(5000)  # получаем данные с сервера
    print("Server sent:", data.decode())  # выводим данные на консоль
except ConnectionRefusedError:
    print("Connection failed: server is not available on this port.")
except Exception as e:
    print("An error occurred:", e)
finally:
    client.close()  # закрываем подключение
