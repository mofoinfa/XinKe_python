import socket

ip_port = ('127.0.0.1', 9000)
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# udp_server.bind(ip_port)
while True:
    data = input('>>:').strip()
    if data == '退出':
        break
    # 发送消息
    udp_server.sendto(data.encode(), ip_port)
    # 接收消息
    data, addr = udp_server.recvfrom(1024)
    print('接收信息:', data.decode('utf-8'))
