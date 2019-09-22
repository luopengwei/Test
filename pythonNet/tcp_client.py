# tcp_client.py
from socket import *

# 创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

# 发起连接
sockfd.connect(('127.0.0.1',8888))# 地址元组

while True:
    data = input('发送>>')
    sockfd.send(data.encode()) # 编码
    # 因为只要连接服务器就OK,用原来这个套接字sockfd即可
    if not data:
        break
    data = sockfd.recv(1024)
    print('接收到:',data.decode())

# 关闭套接字
sockfd.close()