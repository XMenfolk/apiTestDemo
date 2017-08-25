# coding=utf-8
'''
@author: Angie

@desc: 创建测试套件

'''

import unittest
import interfaceTest.public.readConf as conf


# ================将用例添加到测试套件===========
def createSuite():
    testSuite = unittest.TestSuite()
    # 定义测试文件查找的目录
    testDir = conf.casePath
    # 定义 discover 方法的参数
    discover = unittest.defaultTestLoader.discover(testDir,
                                                   pattern='*.py',
                                                   top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for testCase in discover:
        print testCase
        testSuite.addTests(testCase)
    return testSuite