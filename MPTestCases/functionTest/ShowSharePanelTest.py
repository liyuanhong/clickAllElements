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

class ShowSharePanelTest(unittest.TestCase):
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



	#测试视频详情页面点击弹出分享面板
	def test_xiangqing_show_sharePanel(self):
		pass

	#测试黑色单列点击分享可以弹出分享面板
	def test_heisedanlie_show_sharePanel(self):
		pass

	#测试关注页面点击分享，可以弹出分享面板
	def test_guanzuPage_show_sharePanel(self):
		pass

	#测试个人主页点击分享，可以弹出分享面板
	def test_gerenzheye_show_sharePanel(self):
		pass

	#测试热榜点击分享，可以弹出分享面板
	def test_rebang_show_sharePanel(self):
		pass

	#测试全屏播放，点击分享，可以弹出分享面板
	def test_quanpingbofang_show_sharePanel(self):
		pass

	#测试合集页面，点击分享，可以弹出分享面板
	def test_heji_show_sharePanel(self):
		pass

	



def suite(self):
	suite = unittest.TestSuite()  
	suite.addTest(ShowSharePanelTest('test_traverse_discavery_page'))
	runner = unittest.TextTestRunner()  
	runner.run(suite)

ShowSharePanelTest