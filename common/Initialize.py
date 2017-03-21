#coding:utf-8

from time import sleep

#处理开屏广告
def init_case(params):
	#处理开屏广告是否存在的情况
	print "Initialize"
	try:
		sleep(4)
		el = params.driver.find_element_by_id('com.yixia.videoeditor:id/adver_imageview')   #获取开屏广告是否存在
		params.driver.find_element_by_id('com.yixia.videoeditor:id/textview')    #点击开屏广告上的'点击跳过'按钮
		sleep(4)
	except Exception,ex:
		pass