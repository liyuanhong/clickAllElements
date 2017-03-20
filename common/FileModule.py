#coding: utf-8
import os

def delAllFilesOfDir(theDir):
	filelist = os.listdir(theDir)
	for fi in filelist:
		os.remove(theDir + "/" + fi)