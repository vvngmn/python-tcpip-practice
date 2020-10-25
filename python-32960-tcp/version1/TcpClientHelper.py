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

	def __init__(self, suite):
		self.soket_client = socket(AF_INET, SOCK_STREAM)
		self.soket_client.connect(self.ADDR)
		self.test_suite_util = TestSuiteUtil(suite)

	# input: one caseid such as vehicleIncome-01
	# output: a dict {data': xxx, 'expect': xxx}
	def _get_one_case_data_by_raw(self, caseRaw):
		caseDataDict = self.test_suite_util.readOneCase(caseRaw)
		return caseDataDict

	# input: one case data
	# Eg. b'##\x01\x0046F7AS4G165F49SD8\x01\x00\xe6\x15\n\x10\x10\x02!\x00\x0189860023030970000000\x14\nHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOFHJKLASDFHUAILHFUIAOF\x82'
	def _connect_send(self, packed_data):
		self.soket_client.settimeout(self.SOCK_TIMEOUT)
		self.soket_client.send(packed_data)

	# output: server's response 
	# Eg. 23 23 01 00 34 36 46 37 41 53 34 47 31 36 35 46 34 39 53 44 38 01 00 06 15 0A 10 10 02 21 7E
	def _receive_and_decode(self):
		try:
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
			print('@@@@@@@@@@@ '+ str(type(e)))
			if 'socket.timeout' in str(type(e)): print('[server timeout to respond]')

	# input: expect (from self._get_one_case_data()), response (from self._receive_and_decode())
	# output: PASS / FAIL
	def _verify_case(self, expect, response=''):
		if expect == response: return 'PASS'
		else: return 'FAIL'


	def test_case_suite(self, suite='车辆登入相关用例', caseType='正向'):
		caseIdList = CaseManifest().suite[suite][caseType]
		rawList = self.test_suite_util.getRawList(caseIdList) 

		for raw in rawList: 
			caseDataDict = self._get_one_case_data_by_raw(raw)
			print('\n ------------ packed_data:')
			packed_data = caseDataDict['data']
			print(packed_data)
			soket_client1._connect_send(packed_data)

			print('\n ------------ decoded_response:')
			decoded_response = soket_client1._receive_and_decode()
			print(decoded_response)

			print('\n ------------ verify_response:')
			expect_data = caseDataDict['expect']
			print(soket_client1._verify_case(expect_data, decoded_response))

		self.soket_client.shutdown(2) # 关闭接收:0，关闭发送:1，两个通道都关闭:2
		print('Finished: [shut down socket connect]')


if __name__ == '__main__':
	# 应答>>> binascii.unhexlify(s)
	# b'\x01\x0046F7AS4G165F49SD8\x01\x00\x06\x15\n\x10\x10\x02!~'
	soket_client1 = TcpClientHelper('车辆登入相关用例')
	soket_client1.test_case_suite()

