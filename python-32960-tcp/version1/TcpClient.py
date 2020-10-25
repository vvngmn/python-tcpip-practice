#coding:utf-8
import sys
from Util import *
from CaseManifest import *
# import TcpClientHelper


class TcpClient():

	def __init__(self, suite='车辆登入相关用例', caseType='正向'):
		# TcpClientHelper.__init__('车辆登入相关用例')
		cases = CaseManifest().suite[suite][caseType]
		print(type(cases))
		for case in cases: print(case)

if __name__ == '__main__':
	client = TcpClient(sys.argv[1], sys.argv[2])
