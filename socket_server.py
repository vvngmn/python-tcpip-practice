# https://blog.csdn.net/sinat_29214327/article/details/80574955?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param
# coding=UTF-8
import socket

# 1、买手机                  #AF：address family  INET：internet   合在一起称为"基于网络通信的套接字"   
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #SOCK_STREAM==流式协议：指的就是TCP协议
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,0) #重用服务端的IP和端口 (如果服务端的IP及端口在短时间内释放掉，那么就把之前的IP及端口重用上，就可以解决端口被占用问题)

# 2、插卡
server.bind(('127.0.0.1',8080))   #服务端的IP地址加端口
# 3、开机
server.listen(5)   #backlog：半连接池(客户端发送一次请求(syn请求)到服务端(服务端会接收syn并回复一个ack及syn给客户端)，那么在客户端回ack之前，客户端已服务端都是出于半连接状态)
                   #服务端会接收大量客户端的请求，如此多的请求都会堆积在服务器的内存里,如果不做处理的话,服务端的内存会被撑爆，为了保护服务端,不允许大量的客户端请求到达服务端,那么就要对客户端的syn请求加以限制。此处有了半连接池的概念
#什么是半连接池？
'''
在服务端会有一个队列，如果队列的大小为5，代表服务端最高只能接受5个请求数(这里并不是连接数)
当客户端的连接请求到服务端时，请求会到服务端的半连接池里面(最大请求数为5)，服务端直接从半连接池里面取出连接请求。(出去一个请求，那么办连接池就会在进去一个连接请求)
半连接池的大小根据服务端的服务器性能来调整(半连接池应该尽量大，但不能无限大)
在linux中，内核参数调优：tcp_backlog 指的就是半连接池得大小
'''

# 4、等待电话连接
print('等待连接。。。')
while True:             #等待客户端的SYN请求(也就是客户端的coon操作  ·1)
    coon,client_addr=server.accept()    #accept就是从半连接池里面取出连接请求数，accept对应客户端的connect
    # server.accept() #拿到的就是tcp的连接对象，客户端的ip和端口
    # coon指的是：接受某一个唯一地址的客户端的连接请求

    print(coon)
    # <socket.socket fd=536, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8080), raddr=('127.0.0.1', 54165)>
    #其中：laddr=('127.0.0.1', 8080)    #表示的是服务端的IP和端口
    #其中：raddr=('127.0.0.1', 54165)   #表示的是客户端的IP和端口

    print(client_addr)
    # ('127.0.0.1', 54165)   # 客户端的IP加端口

    # 5、接收消息
    while True:    #通信循环：服务端与客户端的连接需要交互式的操作
        try:       #客户端挂掉，服务端不受任何影响
            data=coon.recv(1024)  # 1024表示1024字节，客户端发送过来的字节,服务端最多只能收1024个
            if not data:break
            # coon指的是：与某个唯一地址的客户端连接请求建立后，返回消息给这个客户端
            print('客户端数据：%s' %data)
            # 6、发消息
            coon.send(data.upper())   #接受到客户端消息后，发送消息给客户端
        except ConnectionResetError:
            break

    # 7、挂电话
    coon.close()   #关闭连接状态  (回收的是操作系统的资源)

# 8、关机
server.close()   #关闭服务端   (回收的是操作系统的资源)

# 关闭python程序时，理论上讲会回收掉python程序和操作系统的资源。但是操作系统对应的端口号回不回收取决于操作系统。而不取决于python应用程序
# 在Linux 可以通过调整内核参数设置。
