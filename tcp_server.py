from socket import *

# 1. 创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

# 2. 绑定服务端地址
sockfd.bind(('0.0.0.0',8888)) # 元组

# 3. 设置监听套接字
sockfd.listen(5)

while True:
    # 4. 等待处理客户端连接请求（等待接受连接）
    print('Waiting for connect...')
    connfd,addr = sockfd.accept() # 为每个客户端创建了一个新的套接字
    print('Connect from',addr)
    # 返回值： connfd  客户端连接套接字
    #         addr    连接的客户端地址

    while True:
        # 5. 消息收发之接收
        data = connfd.recv(1024).decode() # 如果没有消息则会阻塞
        if not data:
            break
        print(data)
        # 5. 消息收发之发送 
        send_data = 'Received your message!'
        n = connfd.send(send_data.encode())#这个括号里若用b'...'的形式只能发送ascii字符
        print('发送了%d字节'%n)
    # 6. 关闭客户端连接套接字,关闭套接字
    connfd.close()

sockfd.close()