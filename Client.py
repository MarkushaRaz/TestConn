import socket

client = socket.socket()  # создаём сокет клиента
hostname = '0.0.0.0'
# hostname = socket.gethostname()  # получаем хост сервера
print(hostname)
port = 5000  # устанавливаем порт сервера
client.connect((hostname, port))  # подключаемся к серверу
data = client.recv(1024)  # получаем данные с сервера
print("Server sent: ", data.decode())  # выводим данные на консоль
client.close()  # закрываем подключение [2](https://metanit.com/python/network/1.2.php)

# import socket

# client = socket.socket()  # создаём сокет клиента
# hostname = '0.0.0.0'  # получаем хост сервера
# print("Connecting to server:", hostname)
# port = 5000  # устанавливаем порт сервера

# try:
#     client.connect((hostname, port))  # подключаемся к серверу
#     print(client)
#     data = client.recv(1024)  # получаем данные с сервера
#     print("Server sent:", data.decode())  # выводим данные на консоль
# except ConnectionRefusedError:
#     print("Connection failed: server is not available on this port.")
# except Exception as e:
#     print("An error occurred:", e)
# # finally:
#     # client.close()  # закрываем подключение
