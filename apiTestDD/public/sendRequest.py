# coding=utf-8
'''
@author: Angie

@desc: 发送接口请求

'''

import json

import requests

import parameter
import readConf


def request(method, url, param):
    """
    发送http请求
    """
    if readConf.signStatus == 'on' and readConf.signType == 'md5':
        theParam = parameter.requestParams(param)
    elif readConf.signStatus == 'off':
        theParam = param

    try:
        if method.upper == 'GET':
            request = requests.get(url, theParam, headers={"accept":"application/json"})
        else:
            request = requests.get(url, theParam, headers={"accept": "application/json"})
        response = request.text
        try:
            jsonResponse = json.loads("".join(response.split()))
            print (u'\n接口实际返回值为:\n%s\n'%(json.dumps(jsonResponse, ensure_ascii=False)))
            return jsonResponse
        except:
            print response
            return response

    except Exception as e:
        print u'接口请求失败', e

