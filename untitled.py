from socket import *

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

sockfd.bind(('0.0.0.0',8888))

sockfd.listen(5)
while True:
    print('已建立监听,正等待连接中...')
    connfd,addr = sockfd.accept()
    print('connect from',addr)

    while True:        
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b'received your message')
        

connfd.close()
sockfd.close()