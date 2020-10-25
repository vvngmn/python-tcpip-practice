
#coding:utf-8
# https://github.com/land-pack/jtt808/blob/master/simulate/terminal.py
# python D:\python-scripts\rescope-808client.py

from socket import *
import binascii, struct
import tongue

# 查询时间 '7E 00 04 40 00 01 00 00 00 00 01 55 55 55 55 55 00 24 35 7E'
# 模拟器返回 [RECV] 7E 80 01 00 05 01 00 00 00 00 01 36 81 00 10 01 00 00 FF FF 01 02 00 21 7E
# 服务器端log 通过模拟器=脚本 = 8001000501000000000136810010010000ffff01020021
# 代码返回 7E 80 01 00 05 01 00 00 00 00 01 36 81 00 10 01 00 00 FF FF 01 02 00 21 7E
class TcpClient:
	HOST = '127.0.0.1'
	PORT = 8866
	BUFSIZ = 1024
	ADDR = (HOST, PORT)

	def __init__(self):
		self.client = socket(AF_INET, SOCK_STREAM)
		self.client.connect(self.ADDR)

	# 首位标识符
	def __cmd_unit(self, default='7E'):
		return default


	def init_test_data(self):
		header = self.__cmd_unit()

		register_data = self.__cmd_unit() + '010240910100000000013681001001ffff6d2052324b617a39704c4e4b566b77736d6b57306278585958692b664d51386351766b4f507533772f6d71736b576e3479764a6b516c764f4a7864704e4432566d65487a57697152414d546a59667a70666651464c4c6458686a7773576b7542464b656964424b666934704b553d3132333435363738393031323334350000000000000000000000000000332e372e313565' + self.__cmd_unit()
		


		packed_data = binascii.unhexlify(register_data)

		print('\n packed_data: ')
		print(type(packed_data))
		print(packed_data)
		return packed_data


	def connect_and_send_data(self):

		packed_data = self.init_test_data()
		self.client.send(packed_data)


	def receive_data(self):
		recv_data = self.client.recv(self.BUFSIZ)
		print('\n recv_data: ')
		print(recv_data) 


		recv_decoded_data = tongue.Decode(recv_data)
		print('\n tongue decoded: ') 
		print(recv_decoded_data.dst) 
		#recv_decoded_data.dst : 十六进制用十进制表示 (126, 128, 1, 0, 5, 1, 0, 0, 0, 0, 1, 54, 129, 0, 16, 1, 0, 0, 255, 255, 1, 2, 0, 33, 126)
		l = [hex(i) for i in recv_decoded_data.dst] # 还原十六进制
		r = []
		for i in l:
			if len(i) == 3: r.append(i.replace('x','').upper())
			if len(i) == 4: r.append(i.replace('0x','').upper())
		result = ' '.join(r)
		
		return result


if __name__ == '__main__':
	client1 = TcpClient()
	client1.connect_and_send_data()
	decoded_result = client1.receive_data()
	print(decoded_result)