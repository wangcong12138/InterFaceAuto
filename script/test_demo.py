import json

import requests
import pycurl

from core.basecase import BaseCase
import unittest
import random


class test_demo(BaseCase):

    def test_01(self):
        """
        获取草稿箱信息
        """
        # url = f"https://api.weixin.qq.com/cgi-bin/draft/batchget?access_token={self.token}"
        # json = {"offset": 0, "count": 5, "no_content": 0}
        # r = self.requeset("post", url, json=json)
        # print(r.json())

        """
        获取永久素材
        """
        # rul = f"https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token={self.token}"
        # c = pycurl.Curl()
        pass

        """
        新建草稿信息
        """
        # url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={self.token}"
        # json = {"articles": [
        #     {
        #         "title": "每天学习一句英语",
        #         "author": "晓学笙",
        #         "digest": "",
        #         "content": "Good Morning, and in case I don't see you, good afternoon, good evening, and good night!"
        #         "content_source_url": CONTENT_SOURCE_URL,
        #         "thumb_media_id": THUMB_MEDIA_ID,
        #         "need_open_comment": 0,
        #         "only_fans_can_comment": 0
        #     }
        #
        # ]
        # }


if __name__ == "__main__":
    unittest.main(verbosity=2)
