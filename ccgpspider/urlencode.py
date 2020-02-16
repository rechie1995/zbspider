"""
爬虫：urlencode带参url的拼接
@author: rechie
@date: 2020-02-16
"""
from urllib.parse import urlencode


def get_url(url, parameters):
    """
    拼接url与所带参数
    :param url: {str} 网页地址
    :param parameters: {dict} 参数
    :return: {str} 拼接后的url
    """
    data = urlencode(parameters)
    return url+"?"+data
