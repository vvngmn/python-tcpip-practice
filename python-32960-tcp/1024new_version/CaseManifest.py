#coding:utf-8

# Usage: 选取case用。 要严格和testdata.xls保持一致：
# 第一列：suite名称
# 第二列：positive，negative
# 值：case ID要严格和testdata.xls保持一致。 
# Eg. python TcpTest32960.py 车辆登入相关用例 实时信息上报用例 positive

class CaseManifest:
	suite = {}
	# 车辆登入相关用例分类
	suite['车辆登入相关用例'] ={}
	suite['车辆登入相关用例']['正向'] = ['vehicleIncome-01', 'vehicleIncome-02']
	suite['车辆登入相关用例']['反向'] = ['vehicleIncome-11', 'vehicleIncome-12', 'vehicleIncome-13']

	# 实时信息上报用例分类
	suite['实时信息上报用例'] ={}
	suite['实时信息上报用例']['正向'] = ['infoUpload-01', 'infoUpload-02', 'infoUpload-03']
