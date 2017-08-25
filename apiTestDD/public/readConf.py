# coding=utf-8
"""
读取配置文件
"""

import os
import ConfigParser

baseDir = str(os.path.dirname(os.path.dirname(__file__)))
baseDir = baseDir.replace('\\', '/')
filePath = baseDir + "/apiTestDD.ini"
cf = ConfigParser.ConfigParser()
cf.read(filePath)
host = cf.get("host", "apiTestDD")
signStatus = cf.get("sign", "status")
signType = cf.get("sign", "type")
reportPath = baseDir+"/reports/"
casePath = baseDir+"/testData.xls"
