# coding=utf-8
import unittest
import uuid

import requests
import json

class ConsoleTest_003 (unittest.TestCase):
    '''开发平台集成中心通讯录接口'''

    domainName = "https://qiqiao.do1.com.cn/cgi-bin"
    corpid ="ww6b6c5c4fa6f34b16"
    secret = "b2c2a9fb8dfc9f222f546de4aa60616f"
    Useraccount = "DiaoHuiYun"
    token = ""
    headers = {}


    @classmethod
    def setUpClass(cls):
        # 添加请求头，模拟浏览器访问
        url = cls.domainName+"/securities/access_token?corpId="+cls.corpid+"&secret="+cls.secret+"&account="+cls.Useraccount
        response = requests.get (url=url)
        responseJson = response.json()
        cls.headers = {"Accept": "application/json, text/plain, */*",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
                        "X-Auth0-Token": responseJson["data"],
                        "Content-Type": "application/json"}


    def test_01(self):
        """001根据部门唯一标识获取指定部门"""
        url = self.domainName+"/open/departments/97481fb9f70548e8bb311ed118b2836a"
        print(url)
        response = requests.get (url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'fullName': '创新技术中心->产品研发二部->产品规划组', 'id': '97481fb9f70548e8bb311ed118b2836a', 'name': '产品规划组', 'parentId': 'ff72a1c45f0f45499b9ad865016ab9f8', 'parentName': '产品研发二部'}})



    def test_02(self):
        """002获取指定部门的子级部门列表"""
        url = self.domainName+"/open/departments/d4a2f6c07330450ebff69c6365a05345/children"
        print(url)
        response = requests.get (url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': [{'fullName': '创新技术中心->产品研发二部', 'id': 'ff72a1c45f0f45499b9ad865016ab9f8', 'name': '产品研发二部', 'parentId': 'd4a2f6c07330450ebff69c6365a05345', 'parentName': '创新技术中心'}, {'fullName': '创新技术中心->项目支撑部', 'id': '1151dbc0ed4640fdb003bf409154bb70', 'name': '项目支撑部', 'parentId': 'd4a2f6c07330450ebff69c6365a05345', 'parentName': '创新技术中心'}, {'fullName': '创新技术中心->产品研发一部', 'id': 'a18ec52649be4e3fadf89264eb50ada9', 'name': '产品研发一部', 'parentId': 'd4a2f6c07330450ebff69c6365a05345', 'parentName': '创新技术中心'}, {'fullName': '创新技术中心->系统运维部', 'id': '447165869cde48ec876f1014d41ca83a', 'name': '系统运维部', 'parentId': 'd4a2f6c07330450ebff69c6365a05345', 'parentName': '创新技术中心'}]})

    def test_03( self ):
        """003获取直属上级部门"""
        url = self.domainName + "/open/departments/97481fb9f70548e8bb311ed118b2836a/parent"
        print(url)
        response = requests.get(url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'fullName': '创新技术中心->产品研发二部', 'id': 'ff72a1c45f0f45499b9ad865016ab9f8', 'name': '产品研发二部', 'parentId': 'd4a2f6c07330450ebff69c6365a05345', 'parentName': '创新技术中心'}})



    def test_04( self ):
        """004获取根部门信息"""
        url = self.domainName + "/open/departments/root"
        print(url)
        response = requests.get(url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': [{'fullName': '事业二部', 'id': '83c172b95e324eae8cce131afa5d1bac', 'name': '事业二部', 'parentId': '', 'parentName': ''}, {'fullName': '事业一部', 'id': '7da8f2a0510f462b9c0024369ebd1924', 'name': '事业一部', 'parentId': '', 'parentName': ''}, {'fullName': '创新技术中心', 'id': 'd4a2f6c07330450ebff69c6365a05345', 'name': '创新技术中心', 'parentId': '', 'parentName': ''}, {'fullName': '财务管理中心', 'id': '1c45df1a05c54f9bb74c546cfede7fcb', 'name': '财务管理中心', 'parentId': '', 'parentName': ''}, {'fullName': '事业四部', 'id': '68b5b7564fb54e3fbd0863515ea16a22', 'name': '事业四部', 'parentId': '', 'parentName': ''}, {'fullName': '企微', 'id': '45a66ccf24e94e73afc378a2b1e70505', 'name': '企微', 'parentId': '', 'parentName': ''}, {'fullName': '综合部', 'id': '2688df4c46e848b69445cbbc15928e4f', 'name': '综合部', 'parentId': '', 'parentName': ''}, {'fullName': '技术委员会', 'id': '3c8830c114ea41328f55d88264b88814', 'name': '技术委员会', 'parentId': '', 'parentName': ''}, {'fullName': '员工成功部', 'id': '49319320942c45bbbb20f934a1bede01', 'name': '员工成功部', 'parentId': '', 'parentName': ''}, {'fullName': '市场运营部', 'id': 'a3481e4a5f2b427db75a8a0436a49b7a', 'name': '市场运营部', 'parentId': '', 'parentName': ''}, {'fullName': '总办', 'id': '896086cb51aa4f31b3a2e501ec201b71', 'name': '总办', 'parentId': '', 'parentName': ''}, {'fullName': '董办', 'id': '350d2ddfd3e8432a8381251b8dfce1f5', 'name': '董办', 'parentId': '', 'parentName': ''}, {'fullName': '人力资源部', 'id': '59725d47a08d416590de18f8eda6b1f4', 'name': '人力资源部', 'parentId': '', 'parentName': ''}, {'fullName': '事业三部', 'id': '44eb0451b8d7459488a1b4405c0b9766', 'name': '事业三部', 'parentId': '', 'parentName': ''}, {'fullName': '质量委员会', 'id': '9b5acd0ced7f4c4794fcd855083a02ce', 'name': '质量委员会', 'parentId': '', 'parentName': ''}]})




    def test_05( self ):
        """根据部门ID批量获取部门列表"""
        url = self.domainName + "/open/departments/list?departmentIds=2688df4c46e848b69445cbbc15928e4f&departmentIds=c1c22cc175544360a33ee2ce57b9ae2f&departmentIds=911c8e6a401048c3823e8334af8dcd2f"
        print(url)
        response = requests.get(url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': [{'fullName': '综合部', 'id': '2688df4c46e848b69445cbbc15928e4f', 'name': '综合部', 'parentId': '', 'parentName': ''}, {'fullName': '事业一部->业务支持部->设计组->本部', 'id': '911c8e6a401048c3823e8334af8dcd2f', 'name': '本部', 'parentId': 'e2ee074c072548c98c8bc529b6211dfe', 'parentName': '设计组'}, {'fullName': '综合部->外包清洁', 'id': 'c1c22cc175544360a33ee2ce57b9ae2f', 'name': '外包清洁', 'parentId': '2688df4c46e848b69445cbbc15928e4f', 'parentName': '综合部'}]})


    def test_06( self ):
        """根据账号名获取用户"""
        url = self.domainName + "/open/users/account?account="+self.Useraccount
        print(url)
        response = requests.get(url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'account': 'DiaoHuiYun', 'defaultDepartmentId': 'd4a2f6c07330450ebff69c6365a05345', 'defaultDepartmentName': '', 'departmentIds': ['d4a2f6c07330450ebff69c6365a05345'], 'gender': 2, 'id': 'b896c6a0f44b64eb3391e8adfc898e4b', 'name': '刁惠云', 'telephone': '13536270716'}})




    def test_07( self ):
        """根据用户ID获取用户"""
        url = self.domainName + "/open/users/b896c6a0f44b64eb3391e8adfc898e4b"
        print(url)
        response = requests.get(url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'account': 'DiaoHuiYun', 'defaultDepartmentId': 'd4a2f6c07330450ebff69c6365a05345', 'defaultDepartmentName': '', 'departmentIds': ['d4a2f6c07330450ebff69c6365a05345'], 'gender': 2, 'id': 'b896c6a0f44b64eb3391e8adfc898e4b', 'name': '刁惠云', 'telephone': '13536270716'}})


    def test_08( self ):
        """根据用户ID批量获取用户"""
        url = self.domainName + "/open/users/list"+"?userIds=b896c6a0f44b64eb3391e8adfc898e4b&userIds=407b536100b4b9cd5aec7c219837688c&userIds=4f525f49ec82a6190c55c873f15f23e3"
        print(url)
        response = requests.get(url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': [{'account': 'DiaoHuiYun', 'defaultDepartmentId': 'd4a2f6c07330450ebff69c6365a05345', 'defaultDepartmentName': '', 'departmentIds': ['d4a2f6c07330450ebff69c6365a05345'], 'gender': 2, 'id': 'b896c6a0f44b64eb3391e8adfc898e4b', 'name': '刁惠云', 'telephone': '13536270716'}, {'account': 'lijiacheng', 'defaultDepartmentId': '3c8830c114ea41328f55d88264b88814', 'defaultDepartmentName': '', 'departmentIds': ['3c8830c114ea41328f55d88264b88814'], 'gender': 1, 'id': '4f525f49ec82a6190c55c873f15f23e3', 'name': '李嘉诚', 'telephone': '13560462483'}, {'account': 'zhaojianrong', 'defaultDepartmentId': '3c8830c114ea41328f55d88264b88814', 'defaultDepartmentName': '', 'departmentIds': ['3c8830c114ea41328f55d88264b88814'], 'gender': 1, 'id': '407b536100b4b9cd5aec7c219837688c', 'name': '赵建荣', 'telephone': '15033023704'}]})


    def test_09( self ):
        """根据部门ID获取用户集合(分页)"""
        url = self.domainName + "/open/users?departmentId=f9929e81df574a87921c139b82461fca&page=0&pageSize=5"
        print(url)
        response = requests.get (url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'currPage': 0, 'list': [{'account': 'zhourunze', 'defaultDepartmentId': 'f9929e81df574a87921c139b82461fca', 'defaultDepartmentName': '', 'departmentIds': ['f9929e81df574a87921c139b82461fca'], 'gender': 1, 'id': '8dcc71aae56c18113d0d27c0deb7c997', 'name': '周润泽', 'telephone': '18146195190'}, {'account': 'zhouzixian', 'defaultDepartmentId': 'f9929e81df574a87921c139b82461fca', 'defaultDepartmentName': '', 'departmentIds': ['f9929e81df574a87921c139b82461fca'], 'gender': 1, 'id': '956acf5dd4d2b020339aaa7b60af130b', 'name': '周子贤', 'telephone': '13948433550'}, {'account': 'zhoudaojun', 'defaultDepartmentId': 'f9929e81df574a87921c139b82461fca', 'defaultDepartmentName': '', 'departmentIds': ['f9929e81df574a87921c139b82461fca'], 'gender': 1, 'id': '01ab04ef13a9197bc659b12a4f9ac5bc', 'name': '周到钧', 'telephone': '17621954705'}, {'account': 'zhouyinuo', 'defaultDepartmentId': 'f9929e81df574a87921c139b82461fca', 'defaultDepartmentName': '', 'departmentIds': ['f9929e81df574a87921c139b82461fca'], 'gender': 1, 'id': '04b033d5d1059193321f7732872a57d4', 'name': '周一诺', 'telephone': '14781429545'}, {'account': 'zhouwanfang', 'defaultDepartmentId': 'f9929e81df574a87921c139b82461fca', 'defaultDepartmentName': '', 'departmentIds': ['f9929e81df574a87921c139b82461fca'], 'gender': 1, 'id': '0ae0a2bde2b98717dffb5137df64b062', 'name': '周婉芳', 'telephone': '13067413636'}], 'pageSize': 5, 'totalCount': 42, 'totalPage': 9}})