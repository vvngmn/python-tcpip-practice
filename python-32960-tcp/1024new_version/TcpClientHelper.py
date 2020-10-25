#coding:utf-8

import binascii, tongue, random
from socket import *
from Util import *
from CaseManifest import *


class TcpClientHelper:
	HOST = '127.0.0.1'
	PORT = 8877
	BUFSIZ = 1024
	ADDR = (HOST, PORT)
	SOCK_TIMEOUT = 5

	def __init__(self):
		self.test_suite_util = TestSuiteUtil()

	def _connect_server(self):
		self.soket_client = socket(AF_INET, SOCK_STREAM)
		self.soket_client.connect(self.ADDR)
		self.soket_client.settimeout(self.SOCK_TIMEOUT)

	def _disconnect_server(self):
		self.soket_client.shutdown(2) # 关闭接收:0，关闭发送:1，两个通道都关闭:2
		print('Finished: [shut down socket connect]')

	# output: server's response 
	# Eg. 23 23 01 00 34 36 46 37 41 53 34 47 31 36 35 46 34 39 53 44 38 01 00 06 15 0A 10 10 02 21 7E
	def _receive_and_decode(self):
		try:
			# return '23 23 01 00 34 36 46 37 41 53 34 47 31 36 35 46 34 39 53 44 38 01 00 06 15 0A 10 10 02 21 7E'
			recv_raw = self.soket_client.recv(self.BUFSIZ)
			recv_decoded_data = tongue.Decode(recv_raw) 
			#recv_decoded_data.dst : 十六进制用十进制元组表示 (35, 35, 1, 0, 52, 54, 70, 55, 65, 83, 52, 71, 49, 54, 53, 70, 52, 57, 83, 68, 56, 1, 0, 6, 21, 10, 16, 16, 2, 33, 126)
			l = [hex(i) for i in recv_decoded_data.dst] # 还原十六进制
			r = []
			for i in l:
				if len(i) == 3: r.append(i.replace('x','').upper())
				if len(i) == 4: r.append(i.replace('0x','').upper())
			result = ' '.join(r)		
			return result
		except Exception as e:
			print('###### Catched Error: '+ str(type(e)))
			if 'socket.timeout' in str(type(e)): print('[server timeout to respond]')


	def test_case_suite(self, testSuiteTup=('车辆登入相关用例', ['vehicleIncome-01']), caseFilter='正向'):
		self._connect_server()
		suite = testSuiteTup[0]
		caseIdList = testSuiteTup[1]

		util = TestSuiteUtil()
		util.getSuiteSheet(suite)
		rawList = util.getRawList(caseIdList) 

		for raw in rawList: 
			caseTestDict = util.readOneCase(raw) # dict {data': xxx, 'expect': xxx}
			print('\n ------------ send request:')
			req_data = caseTestDict['data']
			print(req_data)
			# Eg. b'##\x01\x0046F7AS4G165F49SD8\x01\x00\xe6\x15\n\x10\x10\x02!\x00\x0189860023030970000000\x14\nHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOF\x82'
			self.soket_client.send(req_data)

			print('\n ------------ decoded_response:')
			decoded_response = self._receive_and_decode()
			print(decoded_response)

			print('\n ------------ verify_response:')
			expect_data = caseTestDict['expect']
			if caseTestDict['expect'] == decoded_response: return 'PASS'
			else: return 'FAIL'

		self._disconnect_server()


if __name__ == '__main__':
	# 应答>>> binascii.unhexlify(s)
	# b'\x01\x0046F7AS4G165F49SD8\x01\x00\x06\x15\n\x10\x10\x02!~'
	soket_client1 = TcpClientHelper('车辆登入相关用例')
	soket_client1.test_case_suite()

