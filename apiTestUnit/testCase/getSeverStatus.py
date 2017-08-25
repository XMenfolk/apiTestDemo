# coding=utf-8
'''
@author: Angie

@desc:检查服务器状态接口

'''
import unittest
import interfaceTest.public.readConf as conf
import interfaceTest.public.sendRequest as R


class GetServerStatus(unittest.TestCase):
    def setUp(self):
        self.url = conf.host + "/status"
        self.method = "get"
        self.header = {"accept":"application/json"}
        self.param = {'serverId':1,'update':'false'}

    def testGetServerStatus(self):
        u"""检查服务器运行状态"""
        rs = R.request('get',self.url, self.param,self.header)
        status = rs.get('status')
        self.assertEqual(status, 'success')
        print 'webserver ok\nredis ok\n'

    def testGetServerUpdate(self):
        u"""更改状态后，检查服务器状态"""
        param = self.param.copy()
        param['update'] = 'true'
        # post请求更改服务器状态
        R.request('post',self.url + '/update', param,self.header)
        # 请求查询最新状态
        rs = R.request('get', self.url, self.param, self.header)
        status = rs.get('status')
        self.assertEqual(status, 'success')
        print 'webserver ok\nredis ok\n'

if __name__ == '__main__':
    unittest.main()