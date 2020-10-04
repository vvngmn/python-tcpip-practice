# https://blog.csdn.net/wang_xiaowang/article/details/105936957
# 九、Python解析网络报文之搭建基本框架
import socket
# print(socket.__doc__)
# 一、实现报文解析任务对象
#        继承第六节的异步任务对象，在异步处理方法process中编写解析逻辑

class ServerProcessTask(AsyncTask):

    def __init__(self, packet, *args, **kwargs):
        """
        定义异步处理任务
        :param packet:
        :param args:
        :param kwargs:
        """
        super(ServerProcessTask, self).__init__(func=self.process, *args, **kwargs)
        self.packet = packet

    def process(self):
        """
        异步处理方法
        :return:
        """
        headers = {
            'network_header': None,
            'transport_header': None
        }
		# to be continued

        return headers

# 二、搭建基本框架
#        创建socket对象，指明工作的协议为IP协议，绑定本机的IP和port，为socket设置为混杂模式–接收所有经过网卡设备的数据，通过之前实现的线程池处理报文解析任务对象，获取异步结果。

class Server:

    def __init__(self):
        # 创建socket 指明工作协议类型(IPv4) 套接字类型 工作具体的协议(IP协议)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

        # 设置自己的主机ip和端口
        self.ip = '127.0.0.1'
        self.port = 8888
        self.sock.bind((self.ip, self.port))

        # 设置混杂模式 接受所有经过网卡设备的数据
        self.sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        # 初始化线程池
        self.pool = ThreadPool(10)
        self.pool.start()

    def loop_server(self):
        """
        循环读取网络数据
        :return:
        """
        while True:
            packet, addr = self.sock.recvfrom(65535)
            task = ServerProcessTask(packet)
            self.pool.put(task)
            result = task.get_result()
            result = json.dumps(result, indent=4)
            print(result)
