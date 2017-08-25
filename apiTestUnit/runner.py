# coding=utf-8
'''
@author: Angie

@desc: 测试套件执行入口

'''

import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(parentdir)
import interfaceTest.public.reportInfo as report
import interfaceTest.public.createSuite as suite
import interfaceTest.public.sendReport as sendFile
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    report_path, testReport, runner =report.reportInfo()
    allTestCase = suite.createSuite()
    runner.run(allTestCase)
    testReport.close()
    # try:
    #    sendFile.send_report(report_path)  # 发送报告
    # finally:
    #    pass