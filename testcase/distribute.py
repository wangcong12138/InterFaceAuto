from core.basecase import BaseCase
import requests
import json
from common import logger
from image import material


class test_distribute(BaseCase):

    def test_sendmessage(self):
        """
        新建草稿
        """
        # url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={self.token}"
        # taile = "Learn one sentence of English every day"
        # json = {
        #     "articles": [
        #         {
        #             "title": f"{taile}",
        #             "author": "",
        #             "digest": "TEST",
        #             "content": "Good Morning, and in case I don't see you, good afternoon, good evening, and good night!你好，早上好",
        #             "content_source_url": "",
        #             "thumb_media_id": "1C_CAzBh-7yqxQs1GgOzCij_5a_txx9J08nOJOTYoFwdtYdYMVDdqeDJeFjDRfTO",
        #             "need_open_comment": 0,
        #             "only_fans_can_comment": 0
        #         }]}
        # r = self.requeset("post", url, json=json)
        # media_id = r.json()["media_id"]
        #
        # url1 = f"https://api.weixin.qq.com/cgi-bin/freepublish/submit?access_token={self.token}"
        # json = {"media_id": media_id}
        # r1 = self.requeset("post", url1, json=json)
        # errcode = r1.json()["errcode"]
        # message = r1.json()["errmsg"]
        # self.assertEqual(errcode, 0 ,msg="发布失败")
        # self.assertEqual(message, "ok")

    def test_addmaterial(self):
        """
        添加永久素材
        :return:
        """
        url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={self.token}"  # 上传文件
        # test.jpg为本地要上传的素材
        with open('../material/sunflower.jpeg', 'rb') as fp:
            files = {'media': fp}
            res = requests.post(url, files=files)
            res = json.loads(str(res.content, 'utf8'))
            media_id = res["media_id"]
            self.assertIn("url", res, "添加素材失败")
            logger.info("添加永久素材成功，media_id是： " + media_id)
            # 设置上下游传参
            material.media_id = media_id
            print(material.media_id)

    def test_delmaterial(self):
        """
        删除永久素材
        :return:
        """
        url = f"https://api.weixin.qq.com/cgi-bin/material/del_material?access_token={self.token}"
        print(material.media_id)
        json = {"media_id": f"{material.media_id}"}
        res = self.requeset("post", url, json=json)
        self.assertEqual(res.json()["errcode"], 0, "errmsg: "+res.json()["errmsg"])

    def test_step(self):
        print("media_id is: "+material.media_id)
