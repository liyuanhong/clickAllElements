#coding: utf-8
import os
import sys
import platform
from appium import webdriver
import commands


#初始化操作
def setUp(params):
	desired_caps={}
	desired_caps['device']='android'
	desired_caps['platformName']='Android'
	desired_caps['browserName']=''
	desired_caps['version']='6.0.1'
	desired_caps['deviceName']='HUAWEI H60-L01'

	#desired_caps['app'] = PATH('D:\\AndroidAutomation\\AndroidAutoTest\\app\\zhongchou.apk')
	#被测试的App在电脑上的位置
	desired_caps['appPackage']=params.appPackage
	desired_caps['appActivity']=params.appActivity
	params.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


#测试用例执行完成后的操作
def tearDown(params):
	params.driver.quit()
	print 'end ... '

#获取桌面的Activity
def getDesktopActivity():
	output = commands.getstatusoutput('adb shell dumpsys activity | grep "mFocusedActivity"')
	aaa =  output[1]
	bbb = aaa.split("/")
	ccc = bbb[1].split(" ")
	result = ccc[0]
	return result

#获取被测试应用的进程号
def getPorcessId(packageName):
	command = "adb shell ps | grep " + "'" + packageName + "'"
	output = commands.getstatusoutput(command)
	result = ""
	if(output[1] == ""):
		pass
	else:
		aaa = output[1]
		bbb = aaa.split("\r\n")
		for i in bbb:
			ccc = i.split(" ")
			li = []
			for j in ccc:
				if(j != ""):
					li.append(j)
			li[8] = li[8].replace("\r","")    #去掉字符串末尾的换行符号
			li[8] = li[8].replace("\n","")    #去掉字符串末尾的换行符号
			if(li[8] == packageName):
				result = li[1]
	return result


#判断当前activity是否为被测试Activity
def isTestActivity(params):
	activity = params.testActivity
	curActivity = params.driver.current_activity
	if(activity == curActivity):
		return True
	else:
		return False

#让用例执行失败
def excuteFailed(info):
	print "do excuteFailed ..."
	raise Exception(info)


#截取错误截图，并保存到相应的文件夹
def cutScreenShot(picName,params):
	if(os.path.exists("errorScreenShot")):
		pass
	else:
		os.makedirs("errorScreenShot")

	if(platform.system() == "Darwin"):
		filePath = os.getcwd()
	elif(platform.system() == "Windows"):
		filePath = os.path.split(os.path.realpath(sys.argv[0]))[0]  #获取当前脚本路径
	else:
		filePath = os.path.split(os.path.realpath(sys.argv[0]))[0]  #获取当前脚本路径

	if(platform.system() == "Darwin"):
		fileName = filePath + "/errorScreenShot/" + picName + ".png"  #将用例方法名作为图片名
	elif(platform.system() == "Windows"):
		fileName = filePath + "\\errorScreenShot\\" + picName + ".png"  #将用例方法名作为图片名
	else:
		fileName = filePath + "\\errorScreenShot\\" + picName + ".png"  #将用例方法名作为图片名
		
	params.driver.get_screenshot_as_file(fileName)






