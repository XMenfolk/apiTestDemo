# coding=utf-8
'''
@author: Angie

@desc: 获取测试数据，发送接口请求执行测试
'''
import json
import sys
import unittest

import ApiTest.apiTestDD.public.sendRequest as sendRequest

import apiTestDD.public.readConf as conf

reload(sys)
sys.setdefaultencoding('utf8')


class ExecuteCases(unittest.TestCase):
    def executeTest(self, method, url, param, expectedResult):
        host = conf.host
        results = sendRequest.request(method, host + url, param)
        expected = json.loads("".join(expectedResult.split()))
        try:
            self.assertEqual(results, expected, msg="实际结果与预期不一致")
        finally:
            print u'接口预期返回值为:\n%s\n' % json.dumps(expected, ensure_ascii=False)

    @staticmethod
    def executeTestFunc(method, url, param, expectedResult):
        def func(self):
            self.executeTest(method, url, param, expectedResult)

        return func
