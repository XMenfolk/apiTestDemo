# coding=utf-8
'''
@author: Angie

@desc: 获取Excel中的测试数据，生成测试类和测试方法
'''

import json
import time
import unittest

import ApiTest.apiTestDD.testCase.executeCases as execute
import HTMLTestRunner
import xlrd

import apiTestDD.public.readConf as conf


def generateTestCases():
    caseNames = []
    suite = unittest.TestSuite()
    filePath = conf.casePath
    try:
        excel = xlrd.open_workbook(filePath)  # 打开excel
    except Exception as e:
        print '路径不存在或者excel格式不正确', e
        return e
    else:
        sheet = excel.sheet_by_index(0)  # 取第一个sheet页
        rows = sheet.nrows  # 取这个sheet页中所有行数
        caseList = []  # 保存每一条case
        for i in range(rows):
            if i != 0:
                # 把每一条测试用例添加到case_list中
                caseList.append(sheet.row_values(i))

        apiNameList = []
        for case in caseList:
            apiName = case[1]
            caseName = case[2]
            caseNames.append(caseName)
            method = case[3]
            url = case[4]
            param = case[5]
            try:
                param = json.loads(param)
            except:
                param = param
            expectedResult = case[6]
            global customClass
            # 读取Excel 动态生成测试类及测试用例方法，装载到测试套件中
            if apiName not in apiNameList:
                customClass = type(str(apiName), (execute.ExecuteCases,), {"__doc__": None})
                apiNameList.append(apiName)
                #print id(customClass)
                #print customClass
                setattr(customClass, '%s' % caseName,
                        execute.ExecuteCases.executeTestFunc(method, url, param, expectedResult))
                suite.addTest(customClass(caseName))
            else:
                setattr(customClass, '%s' % caseName,
                        execute.ExecuteCases.executeTestFunc(method, url, param, expectedResult))

                suite.addTest(customClass(caseName))

    return suite



if __name__ == '__main__':
    suite = generateTestCases()
    print suite
    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    filename = conf.reportPath + timestr + ".html"
    print (filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='接口测试报告',
                                           description='用例执行情况：')

    runner.run(suite)
    fp.close()