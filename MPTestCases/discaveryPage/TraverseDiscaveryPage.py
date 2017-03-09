#coding:utf-8
import sys
curDir = sys.path[0]
sys.path.append(curDir + '\\common')
sys.path.append(curDir + '/common')

import Common
import Initialize
import TraverseEles
import unittest
from time import sleep


class TraverseDiscaveryPage(unittest.TestCase):

	def __init__(self,methodName):
		unittest.TestCase.__init__(self, methodName)
		self.lastEleIndex = 0
		self.currentEleIndex = 0
		'''
		self.appPackage = 'com.yixia.videoeditor'         #设置被测试应用的包名
		self.appActivity = '.ui.login.SplashActivity'     #设置被测试应用的启动Activity
		self.testActivity = ".ui.FragmentTabsActivity"    #设置被测试应用的页面的activity
		'''
		
		self.appPackage = 'com.example.crashtest'         #设置被测试应用的包名
		self.appActivity = '.MainMyActivity'              #设置被测试应用的启动Activity
		self.testActivity = ".MainMyActivity"             #设置被测试应用的页面的activity
		
		print '************************** MPdetailPage test **************************'
		print Common.getDesktopActivity()

	#初始化操作
	def setUp(self):
		Common.setUp(self)

	#测试用例执行完成后的操作
	def tearDown(self):
		Common.tearDown(self)

		#初始化进入某个指定的页面进行遍历测试
	def goIntoPage(self):
		'''
		Initialize.init_case(self)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_message_tip').click()
		sleep(2)
		'''
		pass

	def test_traverse_discavery_page(self):
		TraverseEles.traverse_all_elements(self)
		sleep(5)
		print Common.getPorcessId(self.appPackage)


def suite(self):
	suite = unittest.TestSuite()  
	suite.addTest(TraverseDiscaveryPage('test_traverse_discavery_page'))
	runner = unittest.TextTestRunner()  
	runner.run(suite)






