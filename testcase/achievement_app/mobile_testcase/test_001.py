# coding=utf-8
import unittest

import requests
import json



class AchievementAppTest_001 (unittest.TestCase):
    '''移动端科目成绩应用报表测试'''


    Token = "cd10d473600ede7e7666eaa8d7c5b42d"

    http = "https://qy.do1.com.cn/qiqiao"

    @classmethod
    def setUpClass(cls):

        # 添加请求头，模拟浏览器访问
        cls.headers = {"Accept": "application/json, text/plain, */*",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
                        "X-Auth0-Token": cls.Token,
                        "Content-Type": "application/json",
                       "Cookie": "corpAB = ww6b6c5c4fa6f34b16"}


    def test_01(self):
        """后端课成绩大于80的学生年龄报表"""
        url = self.http+"/mruntime/api/v1/runtime/report/adf6dfc1bfa7426db243fb90aae5aad3/c6d0f69d9c0d41e9a88291469f0abccb/key_1595840161734_588820"
        print(url)
        data = json.dumps({"linkages":None})
        response = requests.post (url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson['code'],0)
        self.assertEqual(responseJson['data']['name'],"后端课成绩大于80的学生年龄")
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'chartBindConfig': {'dataSetFilterGroups': [{'dataSetFilters': {'advancedConditions': [{'displayValue': '', 'value': ''}], 'baseConditions': [[{'alias': 'T1.', 'field': '课程名字', 'fieldId': 'key_1586225210540_97907', 'fkTableField': '', 'fkTableName': '', 'logic': 'eq', 'type': 'textBox', 'value': '后端课', 'valueType': 'CONST'}, {'alias': 'T0.', 'field': '成绩', 'fieldId': 'key_1586225686685_272118', 'fkTableField': '', 'fkTableName': '', 'logic': 'gt', 'type': 'number', 'value': '80', 'valueType': 'CONST'}]], 'conditionMode': 'base', 'conditionType': 'reportDataSet'}, 'filterType': '', 'id': 'key_1595840238539_32958', 'isAllRole': True, 'name': '数据过滤组1'}], 'dataSetSorts': [], 'dimensions': [{'alias': 'T2.', 'dimensionName': '学生姓名', 'fieldName': '学生姓名', 'fieldType': 'singleUserSelect', 'fieldWidth': None, 'formId': '', 'id': 'key_1586224890119_45881', 'summaryMode': ''}], 'linkages': [], 'metrics': [{'alias': 'T2.', 'fieldName': '年龄', 'id': 'key_1586224915612_66281', 'metricName': '年龄', 'summaryType': 'max'}], 'reportDataSources': {'id': '', 'joins': [{'T0.': 'key_1586225538348_67130', 'T1.': None, 'T2.': 'system_id'}, {'T0.': 'key_1586225626891_223150', 'T1.': 'system_id', 'T2.': None}], 'name': '', 'tableNumType': None, 'tables': [{'alias': 'T0.', 'applicationId': 'adf6dfc1bfa7426db243fb90aae5aad3', 'tableId': 'be49d24cb1f2492bb0bbdc2cc87a29bf', 'tableName': 'f_成绩表_52da63f8b9e4a3e8'}, {'alias': 'T1.', 'applicationId': 'adf6dfc1bfa7426db243fb90aae5aad3', 'tableId': 'f445516cdf3d461797975ecac8dbe8bb', 'tableName': 'f_课程表_52da63f8b9e4a3e8'}, {'alias': 'T2.', 'applicationId': 'adf6dfc1bfa7426db243fb90aae5aad3', 'tableId': 'a32aba85b230480baaecb8b078981415', 'tableName': 'f_学生表_52da63f8b9e4a3e8'}], 'type': 'formds'}, 'searches': []}, 'chartRenderConfig': {'chartData': {'columns': ['学生姓名', '年龄'], 'linkages': {'charts': [], 'colDims': [], 'rowDims': ['a32aba85b230480baaecb8b078981415.学生姓名']}, 'page': 0, 'pageSize': 0, 'rows': [{'学生姓名': '刘言⿴aee5b3312da1d55704df8270c0e5fa73', '年龄': 19.0}, {'学生姓名': '赵立民⿴f520e04b8cebcbd32fa40a95b72cdb13', '年龄': 25.0}], 'total': 0}, 'chartExtend': '{"legend":{"y":"bottom","type":"scroll"},"tooltip":{"confine":true},"series":{"smooth":false}}', 'chartSetting': '{"axisSite":{"right":[]},"xAxisType":"category","yAxisType":[],"yAxisName":[],"stack":{},"labelMap":{},"legendName":{}}'}, 'id': 'key_1595840161734_588820', 'name': '后端课成绩大于80的学生年龄', 'reportId': 'c6d0f69d9c0d41e9a88291469f0abccb', 'type': 'line'}})


    def test_02(self):
        """学生成绩柱状图"""
        url = self.http+"/mruntime/api/v1/runtime/report/adf6dfc1bfa7426db243fb90aae5aad3/c6d0f69d9c0d41e9a88291469f0abccb/key_1595839997902_40593"
        print(url)
        data = json.dumps({"linkages":None})
        response = requests.post (url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson['code'],0)
        self.assertEqual(responseJson['data']['name'],"学生成绩柱状图")
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'chartBindConfig': {'dataSetFilterGroups': [], 'dataSetSorts': [], 'dimensions': [{'alias': 'T0.', 'dimensionName': '学生姓名', 'fieldName': '学生姓名', 'fieldType': 'singleUserSelect', 'fieldWidth': None, 'formId': '', 'id': 'key_1586224890119_45881', 'summaryMode': ''}, {'alias': 'T2.', 'dimensionName': '课程名字', 'fieldName': '课程名字', 'fieldType': 'textBox', 'fieldWidth': None, 'formId': '', 'id': 'key_1586225210540_97907', 'summaryMode': ''}], 'linkages': [], 'metrics': [{'alias': 'T1.', 'fieldName': '成绩', 'id': 'key_1586225686685_272118', 'metricName': '成绩', 'summaryType': 'sum'}], 'reportDataSources': {'id': '', 'joins': [{'T0.': 'system_id', 'T1.': 'key_1586225538348_67130', 'T2.': None}, {'T0.': None, 'T1.': 'key_1586225626891_223150', 'T2.': 'system_id'}], 'name': '', 'tableNumType': None, 'tables': [{'alias': 'T0.', 'applicationId': 'adf6dfc1bfa7426db243fb90aae5aad3', 'tableId': 'a32aba85b230480baaecb8b078981415', 'tableName': 'f_学生表_52da63f8b9e4a3e8'}, {'alias': 'T1.', 'applicationId': 'adf6dfc1bfa7426db243fb90aae5aad3', 'tableId': 'be49d24cb1f2492bb0bbdc2cc87a29bf', 'tableName': 'f_成绩表_52da63f8b9e4a3e8'}, {'alias': 'T2.', 'applicationId': 'adf6dfc1bfa7426db243fb90aae5aad3', 'tableId': 'f445516cdf3d461797975ecac8dbe8bb', 'tableName': 'f_课程表_52da63f8b9e4a3e8'}], 'type': 'formds'}, 'searches': []}, 'chartRenderConfig': {'chartData': {'columns': ['学生姓名', '后端课⿴后端课', '前端课⿴前端课', '测试课⿴测试课'], 'linkages': {'charts': [], 'colDims': [], 'rowDims': ['a32aba85b230480baaecb8b078981415.学生姓名', 'f445516cdf3d461797975ecac8dbe8bb.课程名字']}, 'page': 0, 'pageSize': 0, 'rows': [{'学生姓名': '赵立民⿴f520e04b8cebcbd32fa40a95b72cdb13', '后端课⿴后端课': 89.0, '前端课⿴前端课': 89.0, '测试课⿴测试课': 77.0}, {'学生姓名': '范宇民⿴b6261bd412fbf05cee29c70ec2b11dbd', '后端课⿴后端课': 58.0, '前端课⿴前端课': 55.0, '测试课⿴测试课': 76.0}, {'学生姓名': '刘言⿴aee5b3312da1d55704df8270c0e5fa73', '后端课⿴后端课': 98.0, '前端课⿴前端课': 56.0, '测试课⿴测试课': 67.0}, {'学生姓名': '罗琳月⿴9d5736318fdbc51b250cf5a5bdf7e292', '后端课⿴后端课': 77.0, '前端课⿴前端课': 87.0, '测试课⿴测试课': 86.0}, {'学生姓名': '刁惠云⿴b896c6a0f44b64eb3391e8adfc898e4b', '后端课⿴后端课': 76.0, '前端课⿴前端课': 67.0, '测试课⿴测试课': 90.0}, {'学生姓名': '刘海涛⿴12cb028f00a78bc77235505c6fa812d0', '后端课⿴后端课': 76.0, '前端课⿴前端课': 76.0, '测试课⿴测试课': 43.0}, {'学生姓名': '杨李杰⿴a845e17e17c864adf99a63bc6e7c373b', '后端课⿴后端课': 76.0, '前端课⿴前端课': 87.0, '测试课⿴测试课': 88.0}], 'total': 0}, 'chartExtend': '{"legend":{"y":"bottom","type":"scroll"},"tooltip":{"confine":true}}', 'chartSetting': '{"axisSite":{"right":[]},"xAxisType":"category","yAxisType":[],"yAxisName":[],"labelMap":{},"legendName":{}}'}, 'id': 'key_1595839997902_40593', 'name': '学生成绩柱状图', 'reportId': 'c6d0f69d9c0d41e9a88291469f0abccb', 'type': 'histogram'}})


    def test_03(self):
        """平均每门课成绩"""
        url = self.http+"/mruntime/api/v1/runtime/report/adf6dfc1bfa7426db243fb90aae5aad3/c6d0f69d9c0d41e9a88291469f0abccb/key_1595839130687_218522"
        print(url)
        data = json.dumps({"linkages":None})
        response = requests.post (url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson['code'],0)
        self.assertEqual(responseJson['data']['name'],"平均每门课成绩")
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'chartBindConfig': {'dataSetFilterGroups': [], 'dataSetSorts': [], 'dimensions': [], 'linkages': [], 'metrics': [{'alias': 'T0.', 'fieldName': '成绩', 'id': 'key_1586225686685_272118', 'metricName': '成绩', 'summaryType': 'avg'}], 'reportDataSources': {'id': '', 'joins': [], 'name': '', 'tableNumType': None, 'tables': [{'alias': 'T0.', 'applicationId': 'adf6dfc1bfa7426db243fb90aae5aad3', 'tableId': 'be49d24cb1f2492bb0bbdc2cc87a29bf', 'tableName': 'f_成绩表_52da63f8b9e4a3e8'}], 'type': 'formds'}, 'scriptContext': '', 'searches': [], 'summaryMode': 'normal'}, 'chartRenderConfig': {'chartData': {'columns': [], 'linkages': {'charts': [], 'colDims': [], 'rowDims': []}, 'page': 0, 'pageSize': 0, 'rows': [{'成绩': 75.904761904}], 'total': 0}, 'chartExtend': '{}', 'chartSetting': '{"displayEffect":"medium","fontColor":"#000","color":"#000","remarks":"","displayNameText":true,"dataDisplay":{"extras":{"decimal":{"digit":2}},"list":[]}}'}, 'id': 'key_1595839130687_218522', 'name': '平均每门课成绩', 'reportId': 'c6d0f69d9c0d41e9a88291469f0abccb', 'type': 'metric'}})

    def test_04(self):
        """成绩明细表"""
        url = self.http+"/mruntime/api/v1/runtime/report/adf6dfc1bfa7426db243fb90aae5aad3/c6d0f69d9c0d41e9a88291469f0abccb/key_1595837966232_110241"
        print(url)
        data = json.dumps({"linkages":None})
        response = requests.post (url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson['code'],0)
        self.assertEqual(responseJson['data']['name'],"成绩明细表")
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'chartBindConfig': {'dataSetFilterGroups': [], 'dataSetSorts': [], 'dimensions': [{'alias': 'T0.', 'dimensionName': '学生姓名', 'fieldName': '学生姓名', 'fieldType': 'singleUserSelect', 'fieldWidth': None, 'formId': 'a32aba85b230480baaecb8b078981415', 'id': 'key_1586224890119_45881', 'summaryMode': ''}, {'alias': 'T1.', 'dimensionName': '课程名字', 'fieldName': '课程名字', 'fieldType': 'textBox', 'fieldWidth': None, 'formId': 'f445516cdf3d461797975ecac8dbe8bb', 'id': 'key_1586225210540_97907', 'summaryMode': ''}, {'alias': 'T2.', 'dimensionName': '成绩', 'fieldName': '成绩', 'fieldType': 'number', 'fieldWidth': None, 'formId': 'be49d24cb1f2492bb0bbdc2cc87a29bf', 'id': 'key_1586225686685_272118', 'summaryMode': ''}], 'linkages': [], 'metrics': [], 'reportDataSources': {'id': '', 'joins': [{'T0.': None, 'T1.': 'system_id', 'T2.': 'key_1586225626891_223150'}, {'T0.': 'system_id', 'T1.': None, 'T2.': 'key_1586225538348_67130'}], 'name': '', 'tableNumType': None, 'tables': [{'alias': 'T0.', 'applicationId': 'adf6dfc1bfa7426db243fb90aae5aad3', 'tableId': 'a32aba85b230480baaecb8b078981415', 'tableName': 'f_学生表_52da63f8b9e4a3e8'}, {'alias': 'T1.', 'applicationId': 'adf6dfc1bfa7426db243fb90aae5aad3', 'tableId': 'f445516cdf3d461797975ecac8dbe8bb', 'tableName': 'f_课程表_52da63f8b9e4a3e8'}, {'alias': 'T2.', 'applicationId': 'adf6dfc1bfa7426db243fb90aae5aad3', 'tableId': 'be49d24cb1f2492bb0bbdc2cc87a29bf', 'tableName': 'f_成绩表_52da63f8b9e4a3e8'}], 'type': 'formds'}, 'searches': [], 'tablePage': [10, 20]}, 'chartRenderConfig': {'chartData': {'columns': [{'fieldId': 'key_1586224890119_45881', 'fieldName': '学生姓名', 'fieldType': 'singleUserSelect', 'fieldWidth': None, 'title': '学生姓名', 'uploadType': ''}, {'fieldId': 'key_1586225210540_97907', 'fieldName': '课程名字', 'fieldType': 'textBox', 'fieldWidth': None, 'title': '课程名字', 'uploadType': ''}, {'fieldId': 'key_1586225686685_272118', 'fieldName': '成绩', 'fieldType': 'number', 'fieldWidth': None, 'title': '成绩', 'uploadType': ''}], 'linkages': {'charts': [], 'colDims': [], 'rowDims': ['a32aba85b230480baaecb8b078981415.学生姓名', 'f445516cdf3d461797975ecac8dbe8bb.课程名字', 'be49d24cb1f2492bb0bbdc2cc87a29bf.成绩']}, 'page': 0, 'pageSize': 0, 'rows': [{'课程名字': '后端课', '成绩': '77.00', '学生姓名': '罗琳月'}, {'课程名字': '前端课', '成绩': '55.00', '学生姓名': '范宇民'}, {'课程名字': '前端课', '成绩': '67.00', '学生姓名': '刁惠云'}, {'课程名字': '前端课', '成绩': '87.00', '学生姓名': '杨李杰'}, {'课程名字': '测试课', '成绩': '76.00', '学生姓名': '范宇民'}, {'课程名字': '后端课', '成绩': '76.00', '学生姓名': '杨李杰'}, {'课程名字': '前端课', '成绩': '76.00', '学生姓名': '刘海涛'}, {'课程名字': '后端课', '成绩': '89.00', '学生姓名': '赵立民'}, {'课程名字': '测试课', '成绩': '90.00', '学生姓名': '刁惠云'}, {'课程名字': '前端课', '成绩': '89.00', '学生姓名': '赵立民'}, {'课程名字': '测试课', '成绩': '77.00', '学生姓名': '赵立民'}, {'课程名字': '测试课', '成绩': '43.00', '学生姓名': '刘海涛'}, {'课程名字': '前端课', '成绩': '56.00', '学生姓名': '刘言'}, {'课程名字': '后端课', '成绩': '76.00', '学生姓名': '刁惠云'}, {'课程名字': '测试课', '成绩': '88.00', '学生姓名': '杨李杰'}, {'课程名字': '前端课', '成绩': '87.00', '学生姓名': '罗琳月'}, {'课程名字': '后端课', '成绩': '98.00', '学生姓名': '刘言'}, {'课程名字': '测试课', '成绩': '67.00', '学生姓名': '刘言'}, {'课程名字': '后端课', '成绩': '76.00', '学生姓名': '刘海涛'}, {'课程名字': '后端课', '成绩': '58.00', '学生姓名': '范宇民'}, {'课程名字': '测试课', '成绩': '86.00', '学生姓名': '罗琳月'}], 'total': 0}, 'chartExtend': '{}', 'chartSetting': '{}'}, 'id': 'key_1595837966232_110241', 'name': '成绩明细表', 'reportId': 'c6d0f69d9c0d41e9a88291469f0abccb', 'type': 'detailTable'}})


    def test_05(self):
        """学生能力图"""
        url = self.http+"/mruntime/api/v1/runtime/report/adf6dfc1bfa7426db243fb90aae5aad3/c6d0f69d9c0d41e9a88291469f0abccb/key_1595838889517_354001"
        print(url)
        data = json.dumps({"linkages":None})
        response = requests.post (url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson['code'],0)
        self.assertEqual(responseJson['data']['name'],"学生能力图")
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'chartBindConfig': {'dataSetFilterGroups': [], 'dataSetSorts': [], 'dimensions': [{'alias': 'T1.', 'dimensionName': '学生姓名', 'fieldName': '学生姓名', 'fieldType': 'singleUserSelect', 'fieldWidth': None, 'formId': '', 'id': 'key_1586224890119_45881', 'summaryMode': ''}, {'alias': 'T2.', 'dimensionName': '课程名字', 'fieldName': '课程名字', 'fieldType': 'textBox', 'fieldWidth': None, 'formId': '', 'id': 'key_1586225210540_97907', 'summaryMode': ''}], 'linkages': [], 'metrics': [{'alias': 'T0.', 'fieldName': '成绩', 'id': 'key_1586225686685_272118', 'metricName': '成绩', 'summaryType': 'sum'}], 'reportDataSources': {'id': '', 'joins': [{'T0.': 'key_1586225538348_67130', 'T1.': 'system_id', 'T2.': None}, {'T0.': 'key_1586225626891_223150', 'T1.': None, 'T2.': 'system_id'}], 'name': '', 'tableNumType': None, 'tables': [{'alias': 'T0.', 'applicationId': 'adf6dfc1bfa7426db243fb90aae5aad3', 'tableId': 'be49d24cb1f2492bb0bbdc2cc87a29bf', 'tableName': 'f_成绩表_52da63f8b9e4a3e8'}, {'alias': 'T1.', 'applicationId': 'adf6dfc1bfa7426db243fb90aae5aad3', 'tableId': 'a32aba85b230480baaecb8b078981415', 'tableName': 'f_学生表_52da63f8b9e4a3e8'}, {'alias': 'T2.', 'applicationId': 'adf6dfc1bfa7426db243fb90aae5aad3', 'tableId': 'f445516cdf3d461797975ecac8dbe8bb', 'tableName': 'f_课程表_52da63f8b9e4a3e8'}], 'type': 'formds'}, 'searches': []}, 'chartRenderConfig': {'chartData': {'columns': ['学生姓名', '后端课⿴后端课', '前端课⿴前端课', '测试课⿴测试课'], 'linkages': {'charts': [], 'colDims': [], 'rowDims': ['a32aba85b230480baaecb8b078981415.学生姓名', 'f445516cdf3d461797975ecac8dbe8bb.课程名字']}, 'page': 0, 'pageSize': 0, 'rows': [{'学生姓名': '赵立民⿴f520e04b8cebcbd32fa40a95b72cdb13', '后端课⿴后端课': 89.0, '前端课⿴前端课': 89.0, '测试课⿴测试课': 77.0}, {'学生姓名': '范宇民⿴b6261bd412fbf05cee29c70ec2b11dbd', '后端课⿴后端课': 58.0, '前端课⿴前端课': 55.0, '测试课⿴测试课': 76.0}, {'学生姓名': '刘言⿴aee5b3312da1d55704df8270c0e5fa73', '后端课⿴后端课': 98.0, '前端课⿴前端课': 56.0, '测试课⿴测试课': 67.0}, {'学生姓名': '罗琳月⿴9d5736318fdbc51b250cf5a5bdf7e292', '后端课⿴后端课': 77.0, '前端课⿴前端课': 87.0, '测试课⿴测试课': 86.0}, {'学生姓名': '刁惠云⿴b896c6a0f44b64eb3391e8adfc898e4b', '后端课⿴后端课': 76.0, '前端课⿴前端课': 67.0, '测试课⿴测试课': 90.0}, {'学生姓名': '刘海涛⿴12cb028f00a78bc77235505c6fa812d0', '后端课⿴后端课': 76.0, '前端课⿴前端课': 76.0, '测试课⿴测试课': 43.0}, {'学生姓名': '杨李杰⿴a845e17e17c864adf99a63bc6e7c373b', '后端课⿴后端课': 76.0, '前端课⿴前端课': 87.0, '测试课⿴测试课': 88.0}], 'total': 0}, 'chartExtend': '{"legend":{"y":"bottom","type":"scroll"},"radar":{"shape":"polygon","radius":"45 %"},"tooltip":{"confine":true}}', 'chartSetting': '{"dataType":"normal"}'}, 'id': 'key_1595838889517_354001', 'name': '学生能力图', 'reportId': 'c6d0f69d9c0d41e9a88291469f0abccb', 'type': 'radar'}})


    def test_06(self):
        '''成绩和'''
        url = self.http+"/mruntime/api/v1/runtime/report/adf6dfc1bfa7426db243fb90aae5aad3/c6d0f69d9c0d41e9a88291469f0abccb/df9777d03fc844649cca67bb8bb62153"
        print(url)
        data = json.dumps({"linkages":None})
        response = requests.post (url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson['code'],0)
        self.assertEqual(responseJson['data']['name'],"成绩和")
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'chartBindConfig': {'colDimensions': [{'alias': 'T0.', 'dimensionName': '科目导师', 'fieldName': '科目导师', 'fieldType': 'singleUserSelect', 'fieldWidth': None, 'formId': '', 'id': 'key_1586225765075_495060', 'summaryMode': ''}, {'alias': 'T0.', 'dimensionName': '科目', 'fieldName': '科目', 'fieldType': 'foreignSelection', 'fieldWidth': None, 'formId': '', 'id': 'key_1586225626891_223150', 'summaryMode': ''}], 'dataSetFilterGroups': [], 'dataSetSorts': [{'alias': 'T0.', 'fieldName': '成绩', 'fieldType': 'number', 'id': 'key_1586225686685_272118', 'name': '总成绩', 'settingType': 'metric', 'type': 'asc'}], 'dimensions': [{'alias': 'T1.', 'dimensionName': '学生姓名', 'fieldName': '学生姓名', 'fieldType': 'singleUserSelect', 'fieldWidth': None, 'formId': '', 'id': 'key_1586224890119_45881', 'summaryMode': ''}], 'linkages': [], 'metrics': [{'alias': 'T0.', 'fieldName': '成绩', 'id': 'key_1586225686685_272118', 'metricName': '总成绩', 'summaryType': 'sum'}], 'reportDataSources': {'id': '', 'joins': [{'T0.': 'key_1586225538348_67130', 'T1.': 'system_id'}], 'name': '', 'tableNumType': None, 'tables': [{'alias': 'T0.', 'applicationId': 'adf6dfc1bfa7426db243fb90aae5aad3', 'tableId': 'be49d24cb1f2492bb0bbdc2cc87a29bf', 'tableName': 'f_成绩表_52da63f8b9e4a3e8'}, {'alias': 'T1.', 'applicationId': 'adf6dfc1bfa7426db243fb90aae5aad3', 'tableId': 'a32aba85b230480baaecb8b078981415', 'tableName': 'f_学生表_52da63f8b9e4a3e8'}], 'type': 'formds'}, 'searches': [], 'tablePage': [10, 20]}, 'chartRenderConfig': {'chartData': {'columns': [{'children': [{'children': [{'children': [], 'dataIndex': '学生姓名', 'realValue': '科目导师学生姓名', 'summary': False, 'title': '学生姓名'}], 'dataIndex': '科目', 'realValue': '科目导师科目', 'summary': False, 'title': '科目'}], 'dataIndex': '科目导师', 'realValue': '科目导师', 'summary': False, 'title': '科目导师'}, {'children': [{'children': [{'children': [], 'dataIndex': '39ec01158b2b13f9bab61caaf67549bf-9192477bdf544f8aa1d122237bd0ff29-总成绩', 'realValue': '39ec01158b2b13f9bab61caaf67549bf⿴9192477bdf544f8aa1d122237bd0ff29⿴总成绩', 'summary': False, 'title': '总成绩'}], 'dataIndex': '39ec01158b2b13f9bab61caaf67549bf-9192477bdf544f8aa1d122237bd0ff29', 'realValue': '39ec01158b2b13f9bab61caaf67549bf⿴9192477bdf544f8aa1d122237bd0ff29', 'summary': False, 'title': '00003'}], 'dataIndex': '刘秀维', 'realValue': '39ec01158b2b13f9bab61caaf67549bf', 'summary': False, 'title': '刘秀维'}, {'children': [{'children': [{'children': [], 'dataIndex': '4f525f49ec82a6190c55c873f15f23e3-5547ad69aa274c7691bfcac3af6a48d5-总成绩', 'realValue': '4f525f49ec82a6190c55c873f15f23e3⿴5547ad69aa274c7691bfcac3af6a48d5⿴总成绩', 'summary': False, 'title': '总成绩'}], 'dataIndex': '4f525f49ec82a6190c55c873f15f23e3-5547ad69aa274c7691bfcac3af6a48d5', 'realValue': '4f525f49ec82a6190c55c873f15f23e3⿴5547ad69aa274c7691bfcac3af6a48d5', 'summary': False, 'title': '00002'}], 'dataIndex': '李嘉诚', 'realValue': '4f525f49ec82a6190c55c873f15f23e3', 'summary': False, 'title': '李嘉诚'}, {'children': [{'children': [{'children': [], 'dataIndex': '740905143a3acc008abeed4537781bc5-4bdc7a4f4b16445d839ab805a759bcdb-总成绩', 'realValue': '740905143a3acc008abeed4537781bc5⿴4bdc7a4f4b16445d839ab805a759bcdb⿴总成绩', 'summary': False, 'title': '总成绩'}], 'dataIndex': '740905143a3acc008abeed4537781bc5-4bdc7a4f4b16445d839ab805a759bcdb', 'realValue': '740905143a3acc008abeed4537781bc5⿴4bdc7a4f4b16445d839ab805a759bcdb', 'summary': False, 'title': '00001'}], 'dataIndex': '吴健伦', 'realValue': '740905143a3acc008abeed4537781bc5', 'summary': False, 'title': '吴健伦'}, {'children': [{'children': [{'children': [], 'dataIndex': '总成绩', 'realValue': '汇总总成绩', 'summary': True, 'title': '总成绩'}], 'dataIndex': '汇总', 'realValue': '汇总汇总', 'summary': True, 'title': '汇总'}], 'dataIndex': '汇总', 'realValue': '汇总', 'summary': True, 'title': '汇总'}], 'linkages': {'charts': [], 'colDims': ['be49d24cb1f2492bb0bbdc2cc87a29bf.科目导师', 'be49d24cb1f2492bb0bbdc2cc87a29bf.科目'], 'rowDims': ['a32aba85b230480baaecb8b078981415.学生姓名']}, 'page': 0, 'pageSize': 0, 'rows': [{'总成绩': 195.0, '39ec01158b2b13f9bab61caaf67549bf-9192477bdf544f8aa1d122237bd0ff29-总成绩': 76.0, '学生姓名': '刘海涛', '740905143a3acc008abeed4537781bc5-4bdc7a4f4b16445d839ab805a759bcdb-总成绩': 43.0, '4f525f49ec82a6190c55c873f15f23e3-5547ad69aa274c7691bfcac3af6a48d5-总成绩': 76.0, '_extras_': {'学生姓名': {'fieldName': 'a32aba85b230480baaecb8b078981415.学生姓名', 'value': '12cb028f00a78bc77235505c6fa812d0'}}}, {'总成绩': 250.0, '39ec01158b2b13f9bab61caaf67549bf-9192477bdf544f8aa1d122237bd0ff29-总成绩': 77.0, '学生姓名': '罗琳月', '740905143a3acc008abeed4537781bc5-4bdc7a4f4b16445d839ab805a759bcdb-总成绩': 86.0, '4f525f49ec82a6190c55c873f15f23e3-5547ad69aa274c7691bfcac3af6a48d5-总成绩': 87.0, '_extras_': {'学生姓名': {'fieldName': 'a32aba85b230480baaecb8b078981415.学生姓名', 'value': '9d5736318fdbc51b250cf5a5bdf7e292'}}}, {'总成绩': 251.0, '39ec01158b2b13f9bab61caaf67549bf-9192477bdf544f8aa1d122237bd0ff29-总成绩': 76.0, '学生姓名': '杨李杰', '740905143a3acc008abeed4537781bc5-4bdc7a4f4b16445d839ab805a759bcdb-总成绩': 88.0, '4f525f49ec82a6190c55c873f15f23e3-5547ad69aa274c7691bfcac3af6a48d5-总成绩': 87.0, '_extras_': {'学生姓名': {'fieldName': 'a32aba85b230480baaecb8b078981415.学生姓名', 'value': 'a845e17e17c864adf99a63bc6e7c373b'}}}, {'总成绩': 221.0, '39ec01158b2b13f9bab61caaf67549bf-9192477bdf544f8aa1d122237bd0ff29-总成绩': 98.0, '学生姓名': '刘言', '740905143a3acc008abeed4537781bc5-4bdc7a4f4b16445d839ab805a759bcdb-总成绩': 67.0, '4f525f49ec82a6190c55c873f15f23e3-5547ad69aa274c7691bfcac3af6a48d5-总成绩': 56.0, '_extras_': {'学生姓名': {'fieldName': 'a32aba85b230480baaecb8b078981415.学生姓名', 'value': 'aee5b3312da1d55704df8270c0e5fa73'}}}, {'总成绩': 189.0, '39ec01158b2b13f9bab61caaf67549bf-9192477bdf544f8aa1d122237bd0ff29-总成绩': 58.0, '学生姓名': '范宇民', '740905143a3acc008abeed4537781bc5-4bdc7a4f4b16445d839ab805a759bcdb-总成绩': 76.0, '4f525f49ec82a6190c55c873f15f23e3-5547ad69aa274c7691bfcac3af6a48d5-总成绩': 55.0, '_extras_': {'学生姓名': {'fieldName': 'a32aba85b230480baaecb8b078981415.学生姓名', 'value': 'b6261bd412fbf05cee29c70ec2b11dbd'}}}, {'总成绩': 233.0, '39ec01158b2b13f9bab61caaf67549bf-9192477bdf544f8aa1d122237bd0ff29-总成绩': 76.0, '学生姓名': '刁惠云', '740905143a3acc008abeed4537781bc5-4bdc7a4f4b16445d839ab805a759bcdb-总成绩': 90.0, '4f525f49ec82a6190c55c873f15f23e3-5547ad69aa274c7691bfcac3af6a48d5-总成绩': 67.0, '_extras_': {'学生姓名': {'fieldName': 'a32aba85b230480baaecb8b078981415.学生姓名', 'value': 'b896c6a0f44b64eb3391e8adfc898e4b'}}}, {'总成绩': 255.0, '39ec01158b2b13f9bab61caaf67549bf-9192477bdf544f8aa1d122237bd0ff29-总成绩': 89.0, '学生姓名': '赵立民', '740905143a3acc008abeed4537781bc5-4bdc7a4f4b16445d839ab805a759bcdb-总成绩': 77.0, '4f525f49ec82a6190c55c873f15f23e3-5547ad69aa274c7691bfcac3af6a48d5-总成绩': 89.0, '_extras_': {'学生姓名': {'fieldName': 'a32aba85b230480baaecb8b078981415.学生姓名', 'value': 'f520e04b8cebcbd32fa40a95b72cdb13'}}}, {'summary': True, '总成绩': 1594.0, '39ec01158b2b13f9bab61caaf67549bf-9192477bdf544f8aa1d122237bd0ff29-总成绩': 550.0, '学生姓名': '汇总', '740905143a3acc008abeed4537781bc5-4bdc7a4f4b16445d839ab805a759bcdb-总成绩': 527.0, '4f525f49ec82a6190c55c873f15f23e3-5547ad69aa274c7691bfcac3af6a48d5-总成绩': 517.0, '_extras_': {'学生姓名': {'fieldName': 'a32aba85b230480baaecb8b078981415.学生姓名', 'value': '汇总'}}}], 'total': 0}, 'chartExtend': '{}', 'chartSetting': '{}'}, 'id': 'df9777d03fc844649cca67bb8bb62153', 'name': '成绩和', 'reportId': 'c6d0f69d9c0d41e9a88291469f0abccb', 'type': 'pivotTable'}})
