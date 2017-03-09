#coding:utf-8
#Edit by liyuanhong 2016/10/17#
import sys

curDir = sys.path[0]

#windows下的写法
sys.path.append(curDir + '\\MPTestCases\\discaveryPage')

#mac下的写法
sys.path.append(curDir + '/MPTestCases/discaveryPage')

import TraverseDiscaveryPage


TraverseDiscaveryPage.suite("0")
