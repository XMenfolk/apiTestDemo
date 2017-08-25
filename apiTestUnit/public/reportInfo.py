# coding=utf-8
'''
@author: Angie

@desc: 定义测试报告存放路径及报告信息

'''
import time
import HTMLTestRunner
import interfaceTest.public.readConf as conf

def reportInfo():
    now = time.strftime("%Y-%m-%d%H%M%S")
    reportPath = conf.reportPath
    reportFile = reportPath + now + 'result.html'
    testReport = file(reportFile, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=testReport,
        title=u'接口测试报告',
        description=u'用例执行情况：')
    return reportPath, testReport, runner