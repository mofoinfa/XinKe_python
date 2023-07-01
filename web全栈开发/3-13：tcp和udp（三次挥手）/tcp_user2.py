import socket

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = ('127.0.0.1', 9000)
tcp_server.connect_ex(ip)
while True:
    data = input('>>:').strip()
    tcp_server.send(data.encode('utf-8'))
    print(tcp_server.recv(1024).decode())
