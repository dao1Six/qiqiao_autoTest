# coding=utf-8
import unittest

import requests
import json



class ConsoleTest_002 (unittest.TestCase):
    '''开发平台报表接口'''


    Token = "72cf02891c9b5b049f8b4304e65cfd64"

    http = "https://qy.do1.com.cn/qiqiao/console"

    @classmethod
    def setUpClass(cls):

        # 添加请求头，模拟浏览器访问
        cls.headers = {"Accept": "application/json, text/plain, */*",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
                        "X-Auth0-Token": cls.Token,
                        "Content-Type": "application/json",
                       "Cookie": "corpAB = ww6b6c5c4fa6f34b16"}


    def test_01(self):
        """【ID1083988】【补丁】-开发平台，进入报表页面报系统繁忙"""
        url = self.http+"/api/v1/workbench/applications/d1729726a6584f4c8b4a8e7d4f1b0687/reports/ddcd4eea0c544af783988c171764738e/charts/a747a7da395b448c991990de1891a0c3/chart_render_data?page=1&pageSize=20"
        print(url)
        data = json.dumps({"filter":[{"alias":"d56e66af715b4e5384a30f0558150b0d","field":"createDate","fieldId":"system_createDate","logic":"eqRange","valueType":"VARIABLE","value":"thisMonth"}]})
        response = requests.post (url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'total': 1, 'columns': [{'summary': False, 'realValue': None, 'children': [], 'dataIndex': '人员', 'title': '人员'}, {'summary': False, 'realValue': None, 'children': [], 'dataIndex': '客户名称', 'title': '客户名称'}], 'pageSize': 20, 'page': 1, 'rows': [{'summary': True, '人员': '汇总', '客户名称': 0, '_extras_': {'人员': {'fieldName': 'd56e66af715b4e5384a30f0558150b0d.人员', 'value': '汇总'}}}], 'linkages': {'charts': [], 'rowDims': ['d56e66af715b4e5384a30f0558150b0d.人员'], 'colDims': []}}})

        url2 = self.http+"/api/v1/workbench/applications/d1729726a6584f4c8b4a8e7d4f1b0687/reports/ddcd4eea0c544af783988c171764738e/charts/f9c7f5f97f874069b3b1b245b106b279/chart_render_data?page=1&pageSize=20"
        print(url2)
        data = json.dumps({"filter":[{"alias":"c80c2583dd38444797838ce1594104b1","field":"createDate","fieldId":"system_createDate","logic":"eqRange","valueType":"VARIABLE","value":"thisMonth"}]})
        response2 = requests.post (url=url2,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson2 = response2.json()
        print(responseJson2)
        self.assertEqual(responseJson2,{'msg': '执行成功', 'code': 0, 'data': {'total': 1, 'columns': [{'summary': False, 'realValue': None, 'children': [], 'dataIndex': '创建人名称', 'title': '创建人名称'}, {'summary': False, 'realValue': None, 'children': [], 'dataIndex': '客户全称', 'title': '客户全称'}], 'pageSize': 20, 'page': 1, 'rows': [{'summary': True, '创建人名称': '汇总', '客户全称': 0, '_extras_': {'创建人名称': {'fieldName': 'c80c2583dd38444797838ce1594104b1.author_name', 'value': '汇总'}}}], 'linkages': {'charts': [], 'rowDims': ['c80c2583dd38444797838ce1594104b1.author_name'], 'colDims': []}}})


        url3 = self.http+"/api/v1/workbench/applications/d1729726a6584f4c8b4a8e7d4f1b0687/reports/ddcd4eea0c544af783988c171764738e/charts/f9c7f5f97f874069b3b1b245b106b279/chart_render_data?page=1&pageSize=20"
        print(url3)
        data = json.dumps({"filter":[{"alias":"c80c2583dd38444797838ce1594104b1","field":"createDate","fieldId":"system_createDate","logic":"eqRange","valueType":"VARIABLE","value":"thisMonth"}]})
        response3 = requests.post (url=url3,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson3 = response3.json()
        print(responseJson3)
        self.assertEqual(responseJson3,{'msg': '执行成功', 'code': 0, 'data': {'total': 1, 'columns': [{'summary': False, 'realValue': None, 'children': [], 'dataIndex': '创建人名称', 'title': '创建人名称'}, {'summary': False, 'realValue': None, 'children': [], 'dataIndex': '客户全称', 'title': '客户全称'}], 'pageSize': 20, 'page': 1, 'rows': [{'summary': True, '创建人名称': '汇总', '客户全称': 0, '_extras_': {'创建人名称': {'fieldName': 'c80c2583dd38444797838ce1594104b1.author_name', 'value': '汇总'}}}], 'linkages': {'charts': [], 'rowDims': ['c80c2583dd38444797838ce1594104b1.author_name'], 'colDims': []}}})

    def test_02( self ):
        """【补丁】-开发平台，运行平台表单中有数据时，开发平台明细表配置时出现系统繁忙报错"""
        url = self.http + "/api/v1/workbench/applications/f982d22df3bf4814bade00a2102fab85/reports/bc55e5583e7a4464a54a379244887f94/charts/a650d3b8ed9a4a638ee36d6a20789e51/chart_render_data?page=1&pageSize=20"
        print(url)
        data = json.dumps({"filter":[]})
        response = requests.post(url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'total': 1, 'columns': [{'fieldWidth': {'unit': 'px', 'width': 120, 'type': 'compactly'}, 'fieldName': '项目名称', 'uploadType': '', 'title': '项目名称', 'fieldType': 'textBox', 'fieldId': 'key_1586248723328_174764'}, {'fieldWidth': {'unit': 'px', 'width': 120, 'type': 'compactly'}, 'fieldName': '单位名称', 'uploadType': '', 'title': '单位名称', 'fieldType': 'textBox', 'fieldId': 'key_1586243371336_137302'}, {'fieldWidth': {'unit': 'px', 'width': 100, 'type': 'compactly'}, 'fieldName': '合同金额', 'uploadType': '', 'title': '合同金额（万元）', 'fieldType': 'number', 'fieldId': 'key_1586241891104_215866'}, {'fieldWidth': {'unit': 'px', 'width': 100, 'type': 'compactly'}, 'fieldName': '责任部门', 'uploadType': '', 'title': '责任部门', 'fieldType': 'singleDepartmentSelect', 'fieldId': 'key_1586241894280_200595'}, {'fieldWidth': {'unit': 'px', 'width': 100, 'type': 'compactly'}, 'fieldName': '告警情况', 'uploadType': '', 'title': '告警情况', 'fieldType': 'singleSelect', 'fieldId': 'key_1586241899520_288864'}], 'pageSize': 20, 'page': 1, 'rows': [{'项目名称': '所发生的防守打法', '告警情况': '正常', '合同金额（万元）': '', '责任部门': '', '单位名称': ''}], 'linkages': {'charts': [], 'rowDims': ['ee375638c64143779d046fbcf6010178.项目名称', 'ee375638c64143779d046fbcf6010178.单位名称', 'ee375638c64143779d046fbcf6010178.合同金额', 'ee375638c64143779d046fbcf6010178.责任部门', 'ee375638c64143779d046fbcf6010178.告警情况'], 'colDims': []}}})

