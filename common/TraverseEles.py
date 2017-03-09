#coding:utf-8
import sys
curDir = sys.path[0]
sys.path.append(curDir + '\\common')
sys.path.append(curDir + '/common')

import Common
import os
import pickle  #导入python序列化模块
from time import sleep

#遍历点击页面所有元素
def traverse_all_elements(params):
	print '开始测试...........'
	reload(sys)
	sys.setdefaultencoding('utf8')
	#traverseEles(params)
	#traverseAllEles(params)
	traverseAllPicAndTextEles(params)

#执行元素的遍历点击测试，针对可点击元素
def traverseEles(params):
	#进入要测试的页面
	params.goIntoPage()
	#获取该页面的所有元素存到数组
	sleep(5)
	e1 = params.driver.find_elements_by_xpath('//*')
	print "当前页面共有：" + str(len(e1)) + " 元素"
	print params.driver.current_activity
	for i in range (params.currentEleIndex,len(e1)):
		try:
			e1[i].get_attribute("clickable")  #如果元素不存在，则进入except代码块
			if(e1[i].get_attribute("clickable") == "true"):
				print "这是第：" + str(i) + " 个元素 ; 元素文本为：" + str(e1[i].text)
				print "元素的resource-id为:" + str(e1[i].get_attribute("resourceId"))
				print ""

				reLanchAppRule(params)

				params.lastEleIndex = i
				params.currentEleIndex = i
				e1[i].click()
				sleep(1)
				backToLastPage(params)   #如果跳槽当前Activity则点击返回键
				sleep(1)
			else:
				params.lastEleIndex = i
				params.currentEleIndex = i
				print "跳过第：" + str(i) + " 个元素"
		except:
			print "跳过第：" + str(i) + " 个元素" + "----获取该元素失败..."
			params.lastEleIndex = i
			params.currentEleIndex = i
			params.currentEleIndex = params.currentEleIndex + 1
			params.driver.launch_app()
			print "lanch app"
			traverseEles(params)
			break

#执行所有元素的遍历点击测试
def traverseAllEles(params):
	#进入要测试的页面
	params.goIntoPage()
	#获取该页面的所有元素存到数组
	sleep(5)
	e1 = params.driver.find_elements_by_xpath('//*')
	print "当前页面共有：" + str(len(e1)) + " 元素"
	print params.driver.current_activity
	
	for i in range (params.currentEleIndex,len(e1)):
		try:
			e1[i].get_attribute("clickable")  #如果元素不存在，则进入except代码块
			print "这是第：" + str(i) + " 个元素 ; 元素文本为：" + str(e1[i].text)
			print "元素的resource-id为:" + str(e1[i].get_attribute("resourceId"))
			print ""
			reLanchAppRule(params)
			params.lastEleIndex = i
			params.currentEleIndex = i
			e1[i].click()
			sleep(1)
			backToLastPage(params)   #如果跳槽当前Activity则点击返回键
			sleep(1)
		except:
			print "跳过第：" + str(i) + " 个元素" + "----获取该元素失败..."
			params.lastEleIndex = i
			params.currentEleIndex = i
			params.currentEleIndex = params.currentEleIndex + 1
			params.driver.launch_app()
			print "lanch app"
			traverseAllEles(params)
			break

#点击页面的所有图片，Text，按钮,编辑框和可点击元素
def traverseAllPicAndTextEles(params):
	#进入要测试的页面
	params.goIntoPage()
	#获取该页面的所有元素存到数组
	sleep(5)
	e1 = params.driver.find_elements_by_xpath('//*')
	print "当前页面共有：" + str(len(e1)) + " 元素"
	print params.driver.current_activity
	for i in range (params.currentEleIndex,len(e1)):
		try:
			e1[i].get_attribute("clickable")   #如果元素不存在，则进入except代码块
			if(e1[i].get_attribute("className") == "android.widget.ImageView" or e1[i].get_attribute("className") == "android.widget.TextView" or e1[i].get_attribute("className") == "android.widget.Button" or e1[i].get_attribute("className") == "android.widget.EditText"):
				print "这是第：" + str(i) + " 个元素 ; 元素文本为-：" + str(e1[i].text)
				print "元素的resource-id为:" + str(e1[i].get_attribute("resourceId"))
				print ""
				reLanchAppRule(params)
				params.lastEleIndex = i
				params.currentEleIndex = i
				e1[i].click()
				sleep(1)
				backToLastPage(params)   #如果跳槽当前Activity则点击返回键
				sleep(1)
			elif(e1[i].get_attribute("clickable") == "true"):
				print "这是第：" + str(i) + " 个元素 ; 元素文本为--：" + str(e1[i].text)
				print "元素的resource-id为:" + str(e1[i].get_attribute("resourceId"))
				print ""
				reLanchAppRule(params)
				params.lastEleIndex = i
				params.currentEleIndex = i
				e1[i].click()
				sleep(1)
				backToLastPage(params)   #如果跳槽当前Activity则点击返回键
				sleep(1)
			else:
				params.lastEleIndex = i
				params.currentEleIndex = i
				print "跳过第：" + str(i) + " 个元素---" + e1[i].get_attribute("className")
		except:
			print "跳过第：" + str(i) + " 个元素" + "----获取该元素失败..."
			handleCrash(params)
			params.lastEleIndex = i
			params.currentEleIndex = i
			params.currentEleIndex = params.currentEleIndex + 1
			params.driver.launch_app()
			print "lanch app"
			traverseAllPicAndTextEles(params)
			break

def handleCrash(params):
	pid = Common.getPorcessId(params.appPackage)
	desktopActivity = Common.getDesktopActivity()
	activity = params.driver.current_activity   #获取当前Activity
	if(pid == ""):
		Common.cutScreenShot(str(params.currentEleIndex),params)
	elif(desktopActivity == activity):
		Common.cutScreenShot((params.currentEleIndex),params)
	else:
		pass



#重启被测试应用
def reLanchAppRule(params):
	curActivity = params.driver.current_activity
	activity = params.testActivity
	if(curActivity != activity):
		print curActivity
		print "不是被测试 activity"
		print "lanch app"
		params.driver.launch_app()
		params.goIntoPage()

#如果不是被测试activity，则点击返回键
def backToLastPage(params):
	activity = params.driver.current_activity   #获取当前Activity
	theActivity=params.testActivity
	if(activity != theActivity):      #设置页面
		params.driver.keyevent('4')
		if(activity == params.driver.current_activity):
			sleep(0.5)
			params.driver.keyevent('4')

#将获取到的页面元素写到文件，每行写一个元素，以便下次读取
def writeElementToFile(self,txt):
	filename = './elements.txt'
	if os.path.exists(filename):
		os.remove(filename)
	eleFile = open('elements.txt','w+')
	#将list转换为array
	arr = []
	for j in txt:
		arr.append(j)
		eleFile.write(str(j) + "\n")
	eleFile.close()


#根据元素的索引来获取元素,elements传获取的所有元素，index为索引号
def getElementFromFile(self,elements,index):
	pass

#从文件读取元素，并转换为一个list（将文件的的元素还原为索取到的所有元素）
def getAllElementsFromFile(self,filename=""):
	eleFile = open('elements.txt')
	lis = []
	for line in eleFile:
		lis.append(line)
	return lis

#将获取到的页面所有元素序列化为字符串，并写入文件
def toPickleStr(self,allAlements):
	filePath = "./elementsPickle.txt"
	txt = pickle.dumps(allAlements)
	fileObj = open(filePath,'w')
	fileObj.write(txt)
	fileObj.close()

#从序列化文件里面读取获取到的页面所有元素
def getAllElementsFromPickleFile(self):
	filePath = "./elementsPickle.txt"
	fileObj = open(filePath)
	eles = None
	try:
		eles = fileObj.read()
	finally:
		fileObj.close()
	elesObj = pickle.loads(eles)
	print type(elesObj)
	elesObj[30].click()
	print "点击了第  30  个元素" 

