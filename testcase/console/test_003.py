# coding=utf-8
import unittest
import uuid

import requests
import json

class ConsoleTest_003 (unittest.TestCase):
    '''开发平台集成中心接口'''

    http = "https://qiqiao.do1.com.cn/cgi-bin"
    headers = { "X-Auth0-Token": "ce3813608c189adf7f4d1a6d61f10b29"}

    def test_02( self ):
        url = self.http + "/securities/access_token?corpId=ww6b6c5c4fa6f34b16&secret=b2c2a9fb8dfc9f222f546de4aa60616f&account=DiaoHuiYun"
        print(url)
        response = requests.get (url=url)
        responseJson = response.json()
        print(responseJson)


    def test_01(self):
        """【补丁】-集成中心插入表单记录，单行文本字段的唯一属性没有进行校验"""
        uid = str(uuid.uuid4())
        suid = ''.join(uid.split('-'))
        url = self.http+"/open/applications/5f339e6dbcc5400001145b29/forms/5f6810339909c90001abc3ec"
        print(url)
        data = json.dumps({
    "variables":{
        "单行文本": "1"
    },
    "id": suid,
    "version": 1,
    "loginUserId":"740905143a3acc008abeed4537781bc5"
})
        print(self.headers)
        print(data)
        response = requests.post (url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)


