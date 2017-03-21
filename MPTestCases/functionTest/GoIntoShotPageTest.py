#coding:utf-8
#测试从各个页面进入拍摄页面

import sys
curDir = sys.path[0]
sys.path.append(curDir + '\\common')
sys.path.append(curDir + '/common')

import Common
import Initialize
import TraverseEles
import unittest
from time import sleep

class GoIntoShotPageTest(unittest.TestCase):
	def __init__(self,methodName):
		unittest.TestCase.__init__(self, methodName)
		self.lastEleIndex = 0
		self.currentEleIndex = 0
		self.desktopActivity = Common.getDesktopActivity()
		
		
		self.appPackage = 'com.yixia.videoeditor'         #设置被测试应用的包名
		self.appActivity = '.login.ui.SplashActivity'     #设置被测试应用的启动Activity


		#初始化操作
	def setUp(self):
		Common.setUp(self)

	#测试用例执行完成后的操作
	def tearDown(self):
		Common.tearDown(self)



	#测试从首页点击进入拍摄界面
	def test_shouye_to_shotPage(self):
		pass

	#测试从话题进入拍摄界面
	def test_huati_to_shotPage(self):
		pass

	#测试从悬赏进入拍摄界面
	def test_xuanshang_to_shotPage(self):
		pass

	



def suite(self):
	suite = unittest.TestSuite()  
	suite.addTest(GoIntoShotPageTest('test_traverse_discavery_page'))
	runner = unittest.TextTestRunner()  
	runner.run(suite)