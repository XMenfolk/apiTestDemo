# coding=utf-8
'''
@author: Angie

@desc:将参数做md5签名，此模块根据当前接口规则自行改造

'''

import hashlib

def requestParams(param):
    """
    :param param:请求参数
    :return:拼接好的参数串
    """
    paramk = param.keys()  # 获取键，即参数名
    paramk.sort()  # 按照键值字典序由小到大排列
    params = ""
    for i in paramk:
        kvalue = param.get(i)  # 获取键值
        params = '%s%s=%s' % (params, i, kvalue)  # 按照key1=value1key2=values2方式拼接，没有分割符
    sign = paramSign(params)  # 调用签名方法
    param['sign'] = sign  # 加入参数sign
    return param


def paramSign(params):
    """
    :param params:按照key1=value1key2=values2方式拼接的参数串
    :return:返回最终的签名值sign
    """
    sign1 = hashlib.md5(params).hexdigest()
    sign2 = "%s%s" % (sign1, 'abc')  # 将md5结果尾部拼接渠道的私钥内容
    sign = hashlib.md5(sign2).hexdigest()
    print sign
    return sign  # 返回最终的签名值