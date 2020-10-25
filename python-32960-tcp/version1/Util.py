#coding:utf-8
import binascii, os, xlrd

class TestSuiteUtil:

	def __init__(self,testSuite):
		testSuiteFile = os.getcwd()+r'\testdata.xls'
		workbook = xlrd.open_workbook(testSuiteFile)
		self.sheet_testsuite = workbook.sheet_by_name(testSuite)


	# def getRaw(self, caseId):
	# 	caseIdList = self.sheet_testsuite.col_values(0)
	# 	rawId = caseIdList.index(caseId)
	# 	caseIdList.remove(caseIdList[0]) # must remove the top raw(changed the list length) after get case raw
	# 	return rawId # return raw number

	def getRawList(self, caseIdList=['vehicleIncome-01','vehicleIncome-02','vehicleIncome-03']):
		rawIds = []
		allCaseIDs = self.sheet_testsuite.col_values(0)
		for caseId in caseIdList: 
			rawIds.append(allCaseIDs.index(caseId))
		return rawIds # [1, 2, 3]

	def _getCaseNumber(self):
		return self.sheet_testsuite.nrows-1

	def _splitColForExpect(self):
		expectedData = self.sheet_testsuite.ncols.pop()

	def readOneCase(self, rawId):
		raw = int(rawId)

		rawContent = ''
		startCol = 2 # 3rd col is the start
		lastCol = self.sheet_testsuite.ncols-1
		for col in range(startCol, lastCol): 
			rawContent = rawContent + str(self.sheet_testsuite.cell_value(raw, col))
		byteStr = "b'##%s'"%rawContent

		oneCaseDict = {'data': eval(byteStr), 'expect': self.sheet_testsuite.cell_value(raw, self.sheet_testsuite.ncols-1) }
		return oneCaseDict


if __name__ == '__main__':
	test_suite_util = TestSuiteUtil('车辆登入相关用例')
	print(test_suite_util.getRawList())



