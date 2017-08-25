# coding=utf-8
'''
@author: Angie

@desc: 读取环境配置文件

'''

import sys,os
import ConfigParser

baseDir = str(os.path.dirname(os.path.dirname(__file__)))
baseDir = baseDir.replace('\\', '/')
filePath = baseDir + "/apiTestDD.ini"
cf = ConfigParser.ConfigParser()
cf.read(filePath)

Environment = int(cf.get("Environment", "Environment"))
if Environment == 0:
    host = cf.get("host", "apiTestDD")
else:
    host = cf.get("host", "onLine")

reportPath = baseDir+"/report/"
casePath = baseDir+"/testCase"

