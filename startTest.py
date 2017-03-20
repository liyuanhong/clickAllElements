#coding:utf-8
#Edit by liyuanhong 2016/10/17#
import sys
curDir = sys.path[0]


def delErrorPng():
	path = sys.path[0]
	path = path + "/" + "errorScreenShot"
	#windows下的写法
	sys.path.append(curDir + '\\common\\FileModule')
	#mac下的写法
	sys.path.append(curDir + '/common/FileModule')
	import FileModule
	FileModule.delAllFilesOfDir(path)













#windows下的写法
sys.path.append(curDir + '\\MPTestCases\\traversElesTest')
#mac下的写法
sys.path.append(curDir + '/MPTestCases/traversElesTest')

import TraverseDiscaveryPage
import TraverseHotPage
import TraverseMyPage
import TraverseRebangPage

#执行完所有用例所消耗的时间
totalTime = 0
#执行完单条用例所消耗的时间
singleTime = 0

#删除上传运行的所有截图
delErrorPng()

#TraverseDiscaveryPage.suite("0")
#TraverseHotPage.suite("0")
#TraverseMyPage.suite("0")
TraverseRebangPage.suite("0")






