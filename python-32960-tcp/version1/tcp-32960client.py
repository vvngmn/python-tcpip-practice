
#coding:utf-8
# https://github.com/land-pack/jtt808/blob/master/simulate/terminal.py
# python D:\python-scripts\python-32960-tcp\tcp-32960client.py

from socket import *
import binascii, tongue, random
import const



class TcpClient:
	HOST = '127.0.0.1'
	PORT = 8877
	BUFSIZ = 1024
	ADDR = (HOST, PORT)
	SOCK_TIMEOUT = 5


	def __init__(self):
		self.soket_client = socket(AF_INET, SOCK_STREAM)
		# pass

	# 命令单元: 命令标识 + 应答标识 4 bytes
	def __b2b3(self, cmd_b1=b'\x01'):
		cmd_b1 = const.CmdB1.cmdDict['车辆登入']['code']
		return cmd_b1 + b'\x00'
	# 唯一标识码 17 bytes
	def __b4b20(self, str_b4=b'46F7AS4G165F49SD8'):
		return str_b4
		# return ''.join(random.sample('abcdefghijklmnopqrstuvwxyz',17)).encode()
	# 数据单元加密方式 1 byte
	def __b21(self, encrpt=b'\x01'):
		return encrpt
	# 数据单元长度 2 bytes
	def __b22(self, leng=b'\x00\xe6'):
		return leng
	# 数据单元 (动态长度)
	def _b24(self):
		# eg. 车辆登入数据单元
		# 数据采集时间
		# time = b'\x15\n\x10\x10\x02' +b'!' ### why？？？？ 21 10 16 16 2 33 ['0x15', '0xa', '0x10', '0x10', '0x2', '0x21']
		time_b6 = b'\x15\n\x10\x10\x02' +b'!' ### why？？？？ ['0x15', '0xa', '0x10', '0x10', '0x2', '0x21']
		# 登入流水号
		serialNo_b2 = b'\x00\x01'
		iccid_b20 = b'89860023030970003726'
		# 可充电储能系统数
		batterySystemCnt_b1  = b'\x14'
		# 可充电储能系统编码长度
		batterySystemCodeLen_b1 = b'\x0a'
		# 可充电储能系统编码
		batterySystemCode = b'HJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOF'

		data = time_b6 \
		+ serialNo_b2 \
		+ iccid_b20 \
		+ batterySystemCnt_b1 \
		+ batterySystemCodeLen_b1 \
		+ batterySystemCode 
		return data

	# 校验码 1 byte
	def _last_b(self):
		return b'\x82'


	def get_register_and_packet_data(self):
		packed_data = b'##' \
		+ self.__b2b3() \
		+ self.__b4b20() \
		+ self.__b21() \
		+ self.__b22() \
		+ self._b24() \
		+ self._last_b()


		""" # 服务器端解析的请求 
		{
			"batterySystemCnt":20, #可充电储能子系统数
			"batterySystemCode":"HJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOF",
			"batterySystemCodeLen":10,
			"day":16,
			"header":{
				"bodyLength":230,
				"clientId":"46F7AS4G165F49SD8",
				"commandResponse":0,
				"encryption":1,
				"headLength":22,
				"messageId":1,
				"packageNo":1,
				"packageTotal":1,
				"serialNo":0,
				"subpackage":false,
				"verified":true,
				"version":false,
				"versionNo":0,
				"vin":"46F7AS4G165F49SD8" # hex: 3436463741533447313635463439534438
			},
			"hour":16,
			"iccid":"89860023030970003726", # hex: 3839383630303233303330393730303033373236
			"minute":2,
			"month":10,
			"sec":33,
			"serialNo":1, # 登入流水号
			"year":21
		}
		"""    

		return packed_data


	def connect_send(self, packed_data):
		self.soket_client.connect(self.ADDR)
		self.soket_client.settimeout(self.SOCK_TIMEOUT)
		self.soket_client.send(packed_data)


	def receive_and_decode(self):
		try:
			recv_raw = self.soket_client.recv(self.BUFSIZ)
			recv_decoded_data = tongue.Decode(recv_raw)
			print('\n tongue decoded: ') 
			print(recv_decoded_data.dst) 
			#recv_decoded_data.dst : 十六进制用十进制元组表示 (35, 35, 1, 0, 52, 54, 70, 55, 65, 83, 52, 71, 49, 54, 53, 70, 52, 57, 83, 68, 56, 1, 0, 6, 21, 10, 16, 16, 2, 33, 126)
			l = [hex(i) for i in recv_decoded_data.dst] # 还原十六进制
			r = []
			for i in l:
				if len(i) == 3: r.append(i.replace('x','').upper())
				if len(i) == 4: r.append(i.replace('0x','').upper())
			result = ' '.join(r)
			
			return result

		except Exception as e:
			print('@@@@@@@@@@@ '+ str(type(e)))
			if 'socket.timeout' in str(type(e)): print('[server timeout to respond]')
		finally:
			self.soket_client.shutdown(2) # 关闭接收:0，关闭发送:1，两个通道都关闭:2
			print('[shut down socket connect]')




if __name__ == '__main__':
	# correct_req =b'2323010034364637415334473136354634395344380100e6150a1010022100013839383630303233303330393730303033373236140a484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f4682'
	# correct_resp = '23 23 01 00 34 36 46 37 41 53 34 47 31 36 35 46 34 39 53 44 38 01 00 06 15 0A 10 10 02 21 7E'

	# 应答>>> binascii.unhexlify(s)
	# b'\x01\x0046F7AS4G165F49SD8\x01\x00\x06\x15\n\x10\x10\x02!~'


	soket_client1 = TcpClient()
	packed_data = soket_client1.get_register_and_packet_data()
	print('\n ------------ packed_data:')
	print(packed_data)
	soket_client1.connect_send(packed_data)

	decoded_response = soket_client1.receive_and_decode()
	print('#################')
	print(decoded_response)


