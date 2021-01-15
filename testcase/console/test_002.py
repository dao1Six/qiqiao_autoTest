# coding=utf-8
import unittest

import requests
import json



class ConsoleTest_002 (unittest.TestCase):
    """开发平台报表接口"""


    Token = "6c1a94649df6f8dfde27612dc6c7e840"

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
        #实施支持应用  行为报表
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
        self.assertEqual(responseJson2,{'msg': '执行成功', 'code': 0, 'data': {'total': 1, 'columns': [{'summary': False, 'realValue': None, 'children': [], 'dataIndex': '创建人名称', 'title': '创建人名称'}, {'summary': False, 'realValue': None, 'children': [], 'dataIndex': '客户全称', 'title': '客户全称'}], 'pageSize': 0, 'page': 0, 'rows': [{'创建人名称': '汇总', '客户全称': 0}], 'linkages': {'charts': [], 'rowDims': ['c80c2583dd38444797838ce1594104b1.author_name'], 'colDims': []}}})


        url3 = self.http+"/api/v1/workbench/applications/d1729726a6584f4c8b4a8e7d4f1b0687/reports/ddcd4eea0c544af783988c171764738e/charts/f9c7f5f97f874069b3b1b245b106b279/chart_render_data?page=1&pageSize=20"
        print(url3)
        data = json.dumps({"filter":[{"alias":"c80c2583dd38444797838ce1594104b1","field":"createDate","fieldId":"system_createDate","logic":"eqRange","valueType":"VARIABLE","value":"thisMonth"}]})
        response3 = requests.post (url=url3,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson3 = response3.json()
        print(responseJson3)
        self.assertEqual(responseJson3,{'msg': '执行成功', 'code': 0, 'data': {'total': 1, 'columns': [{'summary': False, 'realValue': None, 'children': [], 'dataIndex': '创建人名称', 'title': '创建人名称'}, {'summary': False, 'realValue': None, 'children': [], 'dataIndex': '客户全称', 'title': '客户全称'}], 'pageSize': 0, 'page': 0, 'rows': [{'创建人名称': '汇总', '客户全称': 0}], 'linkages': {'charts': [], 'rowDims': ['c80c2583dd38444797838ce1594104b1.author_name'], 'colDims': []}}})

    def test_02( self ):
        """【补丁】-开发平台，运行平台表单中有数据时，开发平台明细表配置时出现系统繁忙报错"""
        url = self.http + "/api/v1/workbench/applications/f982d22df3bf4814bade00a2102fab85/reports/bc55e5583e7a4464a54a379244887f94/charts/a650d3b8ed9a4a638ee36d6a20789e51/chart_render_data?page=1&pageSize=20"
        print(url)
        data = json.dumps({"filter":[]})
        response = requests.post(url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'total': 1, 'columns': [{'fieldWidth': {'unit': 'px', 'width': 120, 'type': 'compactly'}, 'fieldName': '项目名称', 'uploadType': '', 'title': '项目名称', 'fieldType': 'textBox', 'fieldId': 'key_1586248723328_174764'}, {'fieldWidth': {'unit': 'px', 'width': 120, 'type': 'compactly'}, 'fieldName': '单位名称', 'uploadType': '', 'title': '单位名称', 'fieldType': 'textBox', 'fieldId': 'key_1586243371336_137302'}, {'fieldWidth': {'unit': 'px', 'width': 100, 'type': 'compactly'}, 'fieldName': '合同金额', 'uploadType': '', 'title': '合同金额（万元）', 'fieldType': 'number', 'fieldId': 'key_1586241891104_215866'}, {'fieldWidth': {'unit': 'px', 'width': 100, 'type': 'compactly'}, 'fieldName': '责任部门', 'uploadType': '', 'title': '责任部门', 'fieldType': 'singleDepartmentSelect', 'fieldId': 'key_1586241894280_200595'}, {'fieldWidth': {'unit': 'px', 'width': 100, 'type': 'compactly'}, 'fieldName': '告警情况', 'uploadType': '', 'title': '告警情况', 'fieldType': 'singleSelect', 'fieldId': 'key_1586241899520_288864'}], 'pageSize': 20, 'page': 1, 'rows': [{'项目名称': '所发生的防守打法', '告警情况': '正常', '合同金额（万元）': '', '责任部门': '', '单位名称': ''}], 'linkages': {'charts': [], 'rowDims': ['ee375638c64143779d046fbcf6010178.项目名称', 'ee375638c64143779d046fbcf6010178.单位名称', 'ee375638c64143779d046fbcf6010178.合同金额', 'ee375638c64143779d046fbcf6010178.责任部门', 'ee375638c64143779d046fbcf6010178.告警情况'], 'colDims': []}}})

    def test_03( self ):
        """【补丁】开发平台-明细表多表数据源中的两张表有重名字段时，勾选显示字段提示系统繁忙；明细表不能勾选子表单"""
        url = self.http + "/api/v1/workbench/applications/be2b359aaa7540208da213289e26bc3c/reports/bb02aad7c3974d4ab33710ed9ed9ead6/charts/afecd7d09be74e4ba02cf2e33fc6dc7a/chart_render_data?page=1&pageSize=20"
        print(url)
        data = json.dumps({"filter":[]})
        response = requests.post(url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'total': 2, 'columns': [{'fieldWidth': {'unit': 'px', 'width': 120, 'type': 'compactly'}, 'fieldName': '车牌号', 'uploadType': '', 'title': '车牌号', 'fieldType': 'textBox', 'fieldId': 'key_1594603660879_236098'}, {'fieldWidth': {'unit': 'px', 'width': 120, 'type': 'compactly'}, 'fieldName': '所属客户', 'uploadType': '', 'title': '所属客户', 'fieldType': 'foreignSelection', 'fieldId': 'key_1594639341653_368429'}, {'fieldWidth': {'unit': 'px', 'width': 150, 'type': 'compactly'}, 'fieldName': '负责人员', 'uploadType': '', 'title': '负责人员', 'fieldType': 'multiUserSelect', 'fieldId': 'key_1594782110375_138528'}, {'fieldWidth': {'unit': 'px', 'width': 100, 'type': 'compactly'}, 'fieldName': '车型', 'uploadType': '', 'title': '车型', 'fieldType': 'singleSelect', 'fieldId': 'key_1594603660879_182515'}, {'fieldWidth': {'unit': 'px', 'width': 120, 'type': 'compactly'}, 'fieldName': '品牌', 'uploadType': '', 'title': '品牌', 'fieldType': 'textBox', 'fieldId': 'key_1594604382294_112001'}, {'fieldWidth': {'unit': 'px', 'width': 100, 'type': 'compactly'}, 'fieldName': '车种', 'uploadType': '', 'title': '车种', 'fieldType': 'singleSelect', 'fieldId': 'key_1594605437716_259094'}, {'fieldWidth': {'unit': 'px', 'width': 100, 'type': 'compactly'}, 'fieldName': '跟进状态', 'uploadType': '', 'title': '跟进状态', 'fieldType': 'singleSelect', 'fieldId': 'key_1594603660881_1656'}, {'fieldWidth': {'unit': 'px', 'width': 100, 'type': 'compactly'}, 'fieldName': '最后拜访日期', 'uploadType': '', 'title': '最后拜访日期', 'fieldType': 'date', 'fieldId': 'key_1594603660880_203163'}, {'fieldWidth': {'unit': 'px', 'width': 120, 'type': 'compactly'}, 'fieldName': '联系人', 'uploadType': '', 'title': '联系人', 'fieldType': 'textBox', 'fieldId': 'key_1594604271407_116641'}, {'fieldWidth': {'unit': 'px', 'width': 100, 'type': 'compactly'}, 'fieldName': '手机号码', 'uploadType': '', 'title': '手机号码', 'fieldType': 'number', 'fieldId': 'key_1594604303440_7382'}], 'pageSize': 20, 'page': 1, 'rows': [{'负责人员': '罗琳月', '跟进状态': '已跟进', '品牌': '', '联系人': '日发顺丰', '车型': '低端车型', '手机号码': '121432453', '车种': '公车', '最后拜访日期': '2020年09月18日', '车牌号': 'gdg', '所属客户': '林品如'}, {'负责人员': '罗琳月', '跟进状态': '已跟进', '品牌': '', '联系人': 'sdfsd', '车型': '低端车型', '手机号码': '143254354', '车种': '公车', '最后拜访日期': '2020年09月18日', '车牌号': 'gsfsdg', '所属客户': '高珊珊'}], 'linkages': {'charts': [], 'rowDims': ['dada5356f72e4ef6bc1f1527ac1a45a9.车牌号', 'dada5356f72e4ef6bc1f1527ac1a45a9.所属客户', 'dada5356f72e4ef6bc1f1527ac1a45a9.负责人员', 'dada5356f72e4ef6bc1f1527ac1a45a9.车型', 'dada5356f72e4ef6bc1f1527ac1a45a9.品牌', 'dada5356f72e4ef6bc1f1527ac1a45a9.车种', 'dada5356f72e4ef6bc1f1527ac1a45a9.跟进状态', 'dada5356f72e4ef6bc1f1527ac1a45a9.最后拜访日期', 'dada5356f72e4ef6bc1f1527ac1a45a9.联系人', 'dada5356f72e4ef6bc1f1527ac1a45a9.手机号码'], 'colDims': []}}})






    def test_04( self ):
        """【补丁】-正式环境，开发平台明细表，人员及部门组件值显示乱码"""
        url = self.http + "/api/v1/workbench/applications/d6d4ce1a14954e85adc8ca1f9f1b73b2/reports/ae8ee295d5f1423a950ca5abc583080b/charts/a043c859f0ae4281adcbfbe8fa0f6d4c/chart_render_data?page=1&pageSize=20"
        print(url)
        data = json.dumps({"filter":[]})
        response = requests.post(url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'total': 1, 'columns': [{'fieldWidth': {'unit': 'px', 'width': 100, 'type': 'compactly'}, 'fieldName': 'user_name', 'uploadType': '', 'title': '代表姓名', 'fieldType': 'singleUserSelect', 'fieldId': 'key_1596327531716_294664'}, {'fieldWidth': {'unit': 'px', 'width': 150, 'type': 'compactly'}, 'fieldName': 'user_department', 'uploadType': '', 'title': '代表部门', 'fieldType': 'multiDepartmentSelect', 'fieldId': 'key_1596376234122_343700'}, {'fieldWidth': {'unit': 'px', 'width': 120, 'type': 'compactly'}, 'fieldName': 'id_card', 'uploadType': '', 'title': '账号', 'fieldType': 'textBox', 'fieldId': 'key_1596433857209_1421'}], 'pageSize': 20, 'page': 1, 'rows': [{'账号': '热给对方', '代表姓名': '罗琳月', '代表部门': '创新技术中心->产品研发二部->产品规划组'}], 'linkages': {'charts': [], 'rowDims': ['ba17f7b1a94842e5a7130c530b8c28a6.user_name', 'ba17f7b1a94842e5a7130c530b8c28a6.user_department', 'ba17f7b1a94842e5a7130c530b8c28a6.id_card'], 'colDims': []}}})


    def test_05( self ):
        """开发平台/identity/info接口"""
        url = self.http + "/api/v1/workbench/identity/info"
        print(url)
        data = json.dumps({"users":[]})
        response = requests.put(url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson['code'],0,msg="/identity/info接口请求失败")


    def test_06( self ):
        """明细表多数据源人员关联"""
        url = self.http + "/api/v1/workbench/applications/adf6dfc1bfa7426db243fb90aae5aad3/reports/5fa0ef3dc298430001338ad5/charts/key_1604383387840_419145/chart_render_data?page=1&pageSize=20"
        print(url)
        data = json.dumps({"filter":[]})
        response = requests.post(url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'total': 150, 'columns': [{'fieldWidth': None, 'fieldName': '学生姓名', 'uploadType': '', 'title': '学生姓名-人员单选', 'fieldType': 'singleUserSelect', 'fieldId': 'a32aba85b230480baaecb8b078981415.key_1586224890119_45881-bab9e16407e349aeb9f4688488e33272.key_1578037630202_25283'}, {'fieldWidth': None, 'fieldName': '部门多选', 'uploadType': '', 'title': '部门多选', 'fieldType': 'multiDepartmentSelect', 'fieldId': 'key_1578037634901_63721'}, {'fieldWidth': None, 'fieldName': '部门单选', 'uploadType': '', 'title': '部门单选', 'fieldType': 'singleDepartmentSelect', 'fieldId': 'key_1578037649735_348457'}, {'fieldWidth': None, 'fieldName': '人员多选', 'uploadType': '', 'title': '人员多选', 'fieldType': 'multiUserSelect', 'fieldId': 'key_1578037639418_283555'}, {'fieldWidth': None, 'fieldName': 'author_name', 'uploadType': '', 'title': '创建人名称', 'fieldType': 'textBox', 'fieldId': 'system_author_name'}, {'fieldWidth': None, 'fieldName': '年龄', 'uploadType': '', 'title': '年龄', 'fieldType': 'number', 'fieldId': 'key_1586224915612_66281'}], 'pageSize': 20, 'page': 1, 'rows': [{'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '学生姓名-人员单选': '赵立民', '部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '创建人名称': '吴健伦', '年龄': '25'}], 'linkages': {'charts': [], 'rowDims': ['a32aba85b230480baaecb8b078981415.学生姓名-bab9e16407e349aeb9f4688488e33272.人员单选', 'bab9e16407e349aeb9f4688488e33272.部门多选', 'bab9e16407e349aeb9f4688488e33272.部门单选', 'bab9e16407e349aeb9f4688488e33272.人员多选', 'a32aba85b230480baaecb8b078981415.author_name', 'a32aba85b230480baaecb8b078981415.年龄'], 'colDims': []}}})


    def test_07( self ):
        """明细表多数据源部门关联"""
        url = self.http + "/api/v1/workbench/applications/adf6dfc1bfa7426db243fb90aae5aad3/reports/5fa0ef3dc298430001338ad5/charts/key_1604384569167_3841/chart_render_data?page=1&pageSize=20"
        print(url)
        data = json.dumps({"filter":[]})
        response = requests.post(url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'total': 45900, 'columns': [{'fieldWidth': None, 'fieldName': '部门单选', 'uploadType': '', 'title': '部门单选-部门单选', 'fieldType': 'singleDepartmentSelect', 'fieldId': 'bab9e16407e349aeb9f4688488e33272.key_1578037649735_348457-5f9bab1098cfca000107ad0b.key_1604037395886_412001'}, {'fieldWidth': None, 'fieldName': '人员多选', 'uploadType': '', 'title': '人员多选', 'fieldType': 'multiUserSelect', 'fieldId': 'key_1578037639418_283555'}, {'fieldWidth': None, 'fieldName': '人员单选', 'uploadType': '', 'title': '人员单选', 'fieldType': 'singleUserSelect', 'fieldId': 'key_1578037630202_25283'}, {'fieldWidth': None, 'fieldName': '部门多选', 'uploadType': '', 'title': '部门多选', 'fieldType': 'multiDepartmentSelect', 'fieldId': 'key_1578037634901_63721'}, {'fieldWidth': None, 'fieldName': '部门多选', 'uploadType': '', 'title': '多表组件关联表⿴部门多选', 'fieldType': 'multiDepartmentSelect', 'fieldId': 'key_1604037395886_264165'}, {'fieldWidth': None, 'fieldName': '人员多选', 'uploadType': '', 'title': '多表组件关联表⿴人员多选', 'fieldType': 'multiUserSelect', 'fieldId': 'key_1604037395886_296753'}, {'fieldWidth': None, 'fieldName': '人员单选', 'uploadType': '', 'title': '多表组件关联表⿴人员单选', 'fieldType': 'singleUserSelect', 'fieldId': 'key_1604037395885_770131'}], 'pageSize': 20, 'page': 1, 'rows': [{'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'人员单选': '赵立民', '部门多选': '董办,员工成功部,人力资源部,总办', '多表组件关联表⿴人员单选': '赵立民', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}], 'linkages': {'charts': [], 'rowDims': ['bab9e16407e349aeb9f4688488e33272.部门单选-5f9bab1098cfca000107ad0b.部门单选', 'bab9e16407e349aeb9f4688488e33272.人员多选', 'bab9e16407e349aeb9f4688488e33272.人员单选', 'bab9e16407e349aeb9f4688488e33272.部门多选', '5f9bab1098cfca000107ad0b.部门多选', '5f9bab1098cfca000107ad0b.人员多选', '5f9bab1098cfca000107ad0b.人员单选'], 'colDims': []}}})


    def test_08( self ):
        """汇总表多数据源人员关联"""
        url = self.http + "/api/v1/workbench/applications/adf6dfc1bfa7426db243fb90aae5aad3/reports/5fa0ef3dc298430001338ad5/charts/key_1604383476256_340329/chart_render_data?page=1&pageSize=20"
        print(url)
        data = json.dumps({"filter":[]})
        response = requests.post(url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'total': 2, 'columns': [{'summary': False, 'realValue': None, 'children': [], 'dataIndex': '学生姓名-人员单选', 'title': '学生姓名-人员单选'}, {'summary': False, 'realValue': None, 'children': [], 'dataIndex': '年龄', 'title': '年龄'}, {'summary': False, 'realValue': None, 'children': [], 'dataIndex': '金额', 'title': '金额'}, {'summary': False, 'realValue': None, 'children': [], 'dataIndex': '部门单选', 'title': '部门单选'}, {'summary': False, 'realValue': None, 'children': [], 'dataIndex': '人员单选', 'title': '人员单选'}, {'summary': False, 'realValue': None, 'children': [], 'dataIndex': '学生姓名', 'title': '学生姓名'}], 'pageSize': 20, 'page': 1, 'rows': [{'人员单选': 150, '学生姓名-人员单选': '赵立民', '部门单选': 150, '年龄': 3750.0, '学生姓名': 150, '金额': 75000.0, '_extras_': {'学生姓名-人员单选': {'fieldName': 'a32aba85b230480baaecb8b078981415.学生姓名-bab9e16407e349aeb9f4688488e33272.人员单选', 'value': 'f520e04b8cebcbd32fa40a95b72cdb13'}}}, {'summary': True, '人员单选': 150, '学生姓名-人员单选': '汇总', '部门单选': 150, '年龄': 3750.0, '学生姓名': 150, '金额': 75000.0, '_extras_': {'学生姓名-人员单选': {'fieldName': 'a32aba85b230480baaecb8b078981415.学生姓名-bab9e16407e349aeb9f4688488e33272.人员单选', 'value': '汇总'}}}], 'linkages': {'charts': [], 'rowDims': ['a32aba85b230480baaecb8b078981415.学生姓名-bab9e16407e349aeb9f4688488e33272.人员单选'], 'colDims': []}}})

    def test_09( self ):
        """明细表多数据源人员部门关联"""
        url = self.http + "/api/v1/workbench/applications/adf6dfc1bfa7426db243fb90aae5aad3/reports/5fa0ef3dc298430001338ad5/charts/key_1604390547024_299993/chart_render_data?page=1&pageSize=20"
        print(url)
        data = json.dumps({"filter": []})
        response = requests.post(url=url,headers=self.headers,data=data.encode("utf-8").decode("latin1"))
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'total': 45900, 'columns': [{'fieldWidth': None, 'fieldName': '人员单选', 'uploadType': '', 'title': '人员单选-人员单选', 'fieldType': 'singleUserSelect', 'fieldId': 'bab9e16407e349aeb9f4688488e33272.key_1578037630202_25283-5f9bab1098cfca000107ad0b.key_1604037395885_770131'}, {'fieldWidth': None, 'fieldName': '部门单选', 'uploadType': '', 'title': '部门单选-部门单选', 'fieldType': 'singleDepartmentSelect', 'fieldId': 'bab9e16407e349aeb9f4688488e33272.key_1578037649735_348457-5f9bab1098cfca000107ad0b.key_1604037395886_412001'}, {'fieldWidth': None, 'fieldName': '人员多选', 'uploadType': '', 'title': '人员多选', 'fieldType': 'multiUserSelect', 'fieldId': 'key_1578037639418_283555'}, {'fieldWidth': None, 'fieldName': '部门多选', 'uploadType': '', 'title': '部门多选', 'fieldType': 'multiDepartmentSelect', 'fieldId': 'key_1578037634901_63721'}, {'fieldWidth': None, 'fieldName': '人员多选', 'uploadType': '', 'title': '多表组件关联表⿴人员多选', 'fieldType': 'multiUserSelect', 'fieldId': 'key_1604037395886_296753'}, {'fieldWidth': None, 'fieldName': '部门多选', 'uploadType': '', 'title': '多表组件关联表⿴部门多选', 'fieldType': 'multiDepartmentSelect', 'fieldId': 'key_1604037395886_264165'}], 'pageSize': 20, 'page': 1, 'rows': [{'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}, {'部门多选': '董办,员工成功部,人力资源部,总办', '部门单选-部门单选': '总办', '人员多选': '吴健伦,孙凤娟,赵立民', '多表组件关联表⿴人员多选': '吴健伦,孙凤娟,赵立民', '人员单选-人员单选': '赵立民', '多表组件关联表⿴部门多选': '董办,员工成功部,人力资源部,总办'}], 'linkages': {'charts': [], 'rowDims': ['bab9e16407e349aeb9f4688488e33272.人员单选-5f9bab1098cfca000107ad0b.人员单选', 'bab9e16407e349aeb9f4688488e33272.部门单选-5f9bab1098cfca000107ad0b.部门单选', 'bab9e16407e349aeb9f4688488e33272.人员多选', 'bab9e16407e349aeb9f4688488e33272.部门多选', '5f9bab1098cfca000107ad0b.人员多选', '5f9bab1098cfca000107ad0b.部门多选'], 'colDims': []}}})