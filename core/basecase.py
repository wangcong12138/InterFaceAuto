import unittest
import requests
from config import BaseData
from common import logger


class BaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        appid = BaseData.configdata['weixin']['appid']
        secret = BaseData.configdata['weixin']['secret']
        url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}'
        r = cls.requeset("get", url)
        # r = requests.get(
        #     f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}')
        cls.token = r.json()["access_token"]
        ACCESS_TOKEN = cls.token

    @classmethod
    def requeset(cls, method, url, params=None, data=None, json=None, **args):
        """
        自定义发送请求
        :param method:请求方法
        :param url:请求URL
        :param params:请求参数
        :param data:body data
        :param json:json格式
        :param args:其他字典参数
        :return:
        """
        method = method.upper()
        if method == "GET":
            res = requests.get(url, params=params, **args)
            logger.info(f"请求方法:{method},请求url:{url},请求参数:{res.request.body},响应结果:{res.text}")
            return res

        elif method == "POST":
            res = requests.post(url, data=data, json=json,  **args)
            logger.info(f"请求方法:{method},请求url:{url},请求参数:{res.request.body},响应结果:{res.text}")
            return res

