# https://blog.csdn.net/sinat_29214327/article/details/80574955?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param
# coding=UTF-8
import socket

# 1、买手机
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #SOCK_STREAM==流式协议：指的就是TCP协议

# 2、插卡
client.connect(('127.0.0.1',8080))   #这里的IP和端口都是服务端的

for i in range(10):
    print('encode then send...')
    client.send(('10000'+str(i)).encode('utf-8'))
    print('receiv then decode...')
    data=client.recv(1024)     #接受服务端的消息  #recv里的1024指的是从操作系统的缓存里一次拿出1024个字节的数据
    # client.recv 这里的接收指的是：应用程序(并不是从服务端直接接收数据)而是从自己的操作系统的内存池里面获取从服务端发送过来的数据。
    print(data.decode('utf-8'))   #这里接受的是普通的字符集所以指定字符集'utf-8'，如果接收的是系统命令那么就要使用(windows：'gbk'，linux：'utf-8')
    print('\n')

while True:
    msg=input('>>:').strip()
    print('#####')
    print(msg)
    if msg == '': 
        print('terminating')
        break

    # 3、发消息
    print('encode then send...')
    print(msg.encode('utf-8'))

    client.send(msg.encode('utf-8'))   #在网络中发送信息需要通过字节(二进制的方式发送),所以需要encode('utf-8')制定字符集的方式发送
    # client.send 这里的发送指的是：应用程序把数据传给操作系统，由操作系统(经过层层封装)把数据发给服务端，而不是应用程序本身直接发送数据到服务端。
    

    # 4、收消息
    print('receiv then decode...')
    data=client.recv(1024)     #接受服务端的消息  #recv里的1024指的是从操作系统的缓存里一次拿出1024个字节的数据
    # client.recv 这里的接收指的是：应用程序(并不是从服务端直接接收数据)而是从自己的操作系统的内存池里面获取从服务端发送过来的数据。
    print(data.decode('utf-8'))   #这里接受的是普通的字符集所以指定字符集'utf-8'，如果接收的是系统命令那么就要使用(windows：'gbk'，linux：'utf-8')

# 5、挂电话
client.close()   #关闭客户端
