import socket

server = socket.socket()  # создаём объект сокета сервера
hostname = '0.0.0.0'
# hostname = socket.gethostname()  # получаем имя хоста локальной машины
print(hostname)
port = 5000  # устанавливаем порт сервера
server.bind((hostname, port))  # привязываем сокет сервера к хосту и порту
print(server)
server.listen(5)  # начинаем прослушивание входящих подключений [2](https://metanit.com/python/network/1.2.php)