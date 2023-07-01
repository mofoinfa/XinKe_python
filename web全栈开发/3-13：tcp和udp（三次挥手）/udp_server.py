import socket

ip_port = ('127.0.0.1', 9000)
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(ip_port)
while True:
    data, addr = udp_server.recvfrom(1024)
    print(f"用户({addr}):{data.decode('utf-8')}")

    data = input('>>:').strip()
    # 发送消息
    if data == '退出':
        break
    udp_server.sendto(data.encode(), addr)
