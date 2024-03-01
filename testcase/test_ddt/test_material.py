#!/user/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from ddt import ddt, data, unpack, file_data
from core.basecase import BaseCase


@ddt
class test_material(BaseCase):

    @data(["1c65sa5c465df", 40007], ["dedq3_crhgrt", 40007])
    @unpack
    def test_add_material(self, media_id, except_errcode):
        """
        数据驱动测试
        测试步骤：删除素材
        :return:
        """
        url = f"https://api.weixin.qq.com/cgi-bin/material/del_material?access_token={self.token}"
        json = {"media_id": f"{media_id}"}
        res = self.requeset("post", url, json=json)
        self.assertEqual(res.json()["errcode"], except_errcode, "errmsg: " + res.json()["errmsg"])

    @file_data("../../testdata/material.json")
    def test_del_material(self, media_id, except_errcode, except_errmsg):
        """
        #删除永久资源
        :param media_id:
        :param except_errcode:
        :param except_errmsg:
        :return:
        """
        url = f"https://api.weixin.qq.com/cgi-bin/material/del_material?access_token={self.token}"
        json = {"media_id": f"{media_id}"}
        res = self.requeset("post", url, json=json)
        self.assertEqual(res.json()["errcode"], except_errcode, "errmsg: " + res.json()["errmsg"])
        self.assertTrue(except_errmsg in res.json()["errmsg"], "errmsg: " + res.json()["errmsg"])

    @file_data("../../testdata/material.yaml")
    def test_del1_material(self, media_id, except_errcode, except_errmsg):
        """
        #删除永久资源
        :param media_id:
        :param except_errcode:
        :param except_errmsg:
        :return:
        """
        url = f"https://api.weixin.qq.com/cgi-bin/material/del_material?access_token={self.token}"
        json = {"media_id": f"{media_id}"}
        res = self.requeset("post", url, json=json)
        self.assertEqual(res.json()["errcode"], except_errcode, "errmsg: " + res.json()["errmsg"])
        self.assertTrue(except_errmsg in res.json()["errmsg"], "errmsg: " + res.json()["errmsg"])