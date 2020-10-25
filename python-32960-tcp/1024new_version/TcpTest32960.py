#coding:utf-8
import sys
from Util import *
from CaseManifest import *
from TcpClientHelper import *


class TcpTest32960():
	# Eg. python TcpTest32960.py 车辆登入相关用例 实时信息上报用例 positive
	def __init__(self,  suites, caseFilter):
		self.suites = suites
		self.caseFilter = caseFilter
		# TcpClientHelper.__init__()

	def get_case_metrics(self):
		# return {'车辆登入相关用例': ['vehicleIncome-01', 'vehicleIncome-02'], '实时信息上报用例': ['infoUpload-01', 'infoUpload-02', 'infoUpload-03']}
		caseMetrics = {}
		for suite in self.suites:
			caseMetrics[suite] = CaseManifest().suite[suite][self.caseFilter]
		return caseMetrics
 

if __name__ == '__main__':
	print(sys.argv)
	testSuites = sys.argv[1:-1]
	testFilter = sys.argv[-1]

	test = TcpTest32960(testSuites, testFilter)
	casesHash = test.get_case_metrics()
	for testSuiteTup in casesHash.items():
		print("###### Testing the suite: %s ######"%str(testSuiteTup))
		trigger_client = TcpClientHelper()
		result = trigger_client.test_case_suite(testSuiteTup,testFilter)
		print(result)


