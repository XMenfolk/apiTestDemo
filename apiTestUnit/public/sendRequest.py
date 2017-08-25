# coding=utf-8
'''
@author: Angie

@desc: 发送接口请求

'''

import json
import requests
import parameter

def request(method,url, param,header):
    try:
        if method == 'get':
            # 发送get请求,参数为传入parameter.requestParams(param) 进行签名拼接，若参数无签名，则直接传入param
            request = requests.get(url, parameter.requestParams(param),headers=header)
            # 获取返回值
        else:
            # 发送post请求
            request = requests.post(url, parameter.requestParams(param),headers=header)
        response = request.text
        try:
            jsonResponse = json.loads(response)
            print (u'接口返回值为:\n%s' % (json.dumps(jsonResponse, ensure_ascii=False)))
            return jsonResponse
        except:
            print response
            return response
    except Exception as e:
        print u'接口请求失败', e
