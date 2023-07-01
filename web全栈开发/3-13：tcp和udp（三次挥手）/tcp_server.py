import socket
import threading

ip = ('127.0.0.1', 9000)
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(ip)
tcp_server.listen(5)


def reve_user(conn, addr):
    while True:
        data = conn.recv(1024)  # 接收数据
        print(f"用户（{addr}）：{data.decode()}")
        data = input('>>:').strip()
        conn.send(data.encode('utf-8'))


while True:
    conn, addr = tcp_server.accept()
    if addr != []:
        threading.Thread(target=reve_user, args=(conn, addr)).start()
