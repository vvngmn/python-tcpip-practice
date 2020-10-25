#coding:utf-8

# Usage: Filter test cases by testsuite and type, caseid is unique, which should be exactly SAME as testdata.xls
class CaseManifest:
	# 车辆登入相关用例
	suite = {}
	suite['车辆登入相关用例'] ={}
	suite['车辆登入相关用例']['正向'] = ['vehicleIncome-01', 'vehicleIncome-02', 'vehicleIncome-03']
	suite['车辆登入相关用例']['反向'] = ['vehicleIncome-11', 'vehicleIncome-12', 'vehicleIncome-13']

	# 实时信息上报用例
	suite['实时信息上报用例'] ={}


