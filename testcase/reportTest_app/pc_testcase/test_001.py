# coding=utf-8
import unittest

import requests
import json



class ReportAppTest_001 (unittest.TestCase):
    '''PC端数据过滤应用报表测试'''


    Token = "4ace76ed98e9d52b2b8f48f514db7fce"

    http = "https://qy.do1.com.cn/qiqiao"

    @classmethod
    def setUpClass(cls):

        # 添加请求头，模拟浏览器访问
        cls.headers = {"Accept": "application/json, text/plain, */*",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
                        "X-Auth0-Token": cls.Token,
                        "Content-Type": "application/json"}


    def test_01(self):
        """明细表报表"""
        url = self.http+"/runtime/api/v1/runtime/report/e8e7124ff51846118f602b349a1a243a/a1d28a1d64eb49f783cc3b65ae9877d3/b7cc6d94d625454dbd62615b38c28ffb?page=1&pageSize=20"
        print(url)
        data = json.dumps({"linkages":None})
        response = requests.post (url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson['code'],0)
        self.assertEqual(responseJson['data']['name'],"明细表")


    def test_02(self):
        """饼状图数据值30报表"""
        url = self.http+"/runtime/api/v1/runtime/report/e8e7124ff51846118f602b349a1a243a/a1d28a1d64eb49f783cc3b65ae9877d3/aed7b105290e4decbb9558ec8814ffb5?"
        print(url)
        data = json.dumps({"linkages":None})
        response = requests.post (url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson['code'],0)
        self.assertEqual(responseJson['data']['name'],"饼状图数据值30")

    def test_03(self):
        """多过滤组多角色报表"""
        url = self.http+"/runtime/api/v1/runtime/report/e8e7124ff51846118f602b349a1a243a/a1d28a1d64eb49f783cc3b65ae9877d3/e0be27e1f1b54b4697c37308cd583b4b?page=1&pageSize=20"
        print(url)
        data = json.dumps({"linkages":None})
        response = requests.post (url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson['code'],0)
        self.assertEqual(responseJson['data']['name'],"多过滤组多角色")

    def test_04(self):
        """汇总表数据值50报表"""
        url = self.http+"/runtime/api/v1/runtime/report/e8e7124ff51846118f602b349a1a243a/a1d28a1d64eb49f783cc3b65ae9877d3/a1d8b7acd11c4a36b5652dd67c0d717b?page=1&pageSize=20"
        print(url)
        data = json.dumps({"linkages":None})
        response = requests.post (url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson['code'],0)
        self.assertEqual(responseJson['data']['name'],"汇总表数据值50")

    def test_05(self):
        """柱状图数据值报表"""
        url = self.http+"/runtime/api/v1/runtime/report/e8e7124ff51846118f602b349a1a243a/a1d28a1d64eb49f783cc3b65ae9877d3/d6a8a9accae74eada421fec7606aa7f3?"
        print(url)
        data = json.dumps({"linkages":None})
        response = requests.post (url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson['code'],0)
        self.assertEqual(responseJson['data']['name'],"柱状图数据值")

    def test_06(self):
        '''条形图数据值20报表'''
        url = self.http+"/runtime/api/v1/runtime/report/e8e7124ff51846118f602b349a1a243a/a1d28a1d64eb49f783cc3b65ae9877d3/e62f140f18a54a47a8a4da100a1c7146?"
        print(url)
        data = json.dumps({"linkages":None})
        response = requests.post (url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson['code'],0)
        self.assertEqual(responseJson['data']['name'],"条形图数据值20")