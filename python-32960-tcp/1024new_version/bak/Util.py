#coding:utf-8
import binascii, os, xlrd

class TestSuiteUtil:

	def __init__(self):
		pass

	def getSuiteSheet(self, suite):
		suiteDataFile = os.getcwd()+r'\testdata.xls'
		workbook = xlrd.open_workbook(suiteDataFile)
		self.sheet_testsuite = workbook.sheet_by_name(suite)

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

		caseTestDict = {'data': eval(byteStr), 'expect': self.sheet_testsuite.cell_value(raw, self.sheet_testsuite.ncols-1) }
		return caseTestDict


if __name__ == '__main__':
	test_suite_util = TestSuiteUtil('车辆登入相关用例')
	print(test_suite_util.getRawList())



