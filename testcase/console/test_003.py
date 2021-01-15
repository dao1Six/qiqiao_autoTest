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
        """001根据部门唯一标识获取指定部门"""  #c0a65f17979f45f89929b07cda257ba1  创新技术中心->产品研发二部->产品规划组
        url = self.domainName+"/open/departments/c0a65f17979f45f89929b07cda257ba1"
        print(url)
        response = requests.get (url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'fullName': '创新技术中心->产品研发二部->产品规划组', 'id': 'c0a65f17979f45f89929b07cda257ba1', 'name': '产品规划组', 'parentId': 'b15ecfb8787c487cb7ffca4798bc793a', 'parentName': '产品研发二部'}})



    def test_02(self):
        """002获取指定部门的子级部门列表"""  #b15ecfb8787c487cb7ffca4798bc793a
        url = self.domainName+"/open/departments/b15ecfb8787c487cb7ffca4798bc793a/children"
        print(url)
        response = requests.get (url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': [{'fullName': '创新技术中心->产品研发二部->研发一组', 'id': '500c697a75e046edb1596e2b71323b33', 'name': '研发一组', 'parentId': 'b15ecfb8787c487cb7ffca4798bc793a', 'parentName': '产品研发二部'}, {'fullName': '创新技术中心->产品研发二部->产品规划组', 'id': 'c0a65f17979f45f89929b07cda257ba1', 'name': '产品规划组', 'parentId': 'b15ecfb8787c487cb7ffca4798bc793a', 'parentName': '产品研发二部'}, {'fullName': '创新技术中心->产品研发二部->研发二组', 'id': 'c526518fded9444ba7c986813387868b', 'name': '研发二组', 'parentId': 'b15ecfb8787c487cb7ffca4798bc793a', 'parentName': '产品研发二部'}]}
)

    def test_03( self ):
        """003获取直属上级部门"""  ##c0a65f17979f45f89929b07cda257ba1  创新技术中心->产品研发二部->产品规划组
        url = self.domainName + "/open/departments/c0a65f17979f45f89929b07cda257ba1/parent"
        print(url)
        response = requests.get(url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'fullName': '创新技术中心->产品研发二部', 'id': 'b15ecfb8787c487cb7ffca4798bc793a', 'name': '产品研发二部', 'parentId': '6e704cf6f412495697e7265016bc6c13', 'parentName': '创新技术中心'}})



    def test_04( self ):
        """004获取根部门信息"""
        url = self.domainName + "/open/departments/root"
        print(url)
        response = requests.get(url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': [{'fullName': '事业二部', 'id': 'f036f64d4df04581adbdb68b47ce63d7', 'name': '事业二部', 'parentId': '', 'parentName': ''}, {'fullName': '事业一部', 'id': '34c1fdebe2d04b1cbc3f887783a1744b', 'name': '事业一部', 'parentId': '', 'parentName': ''}, {'fullName': '创新技术中心', 'id': '6e704cf6f412495697e7265016bc6c13', 'name': '创新技术中心', 'parentId': '', 'parentName': ''}, {'fullName': '财务管理中心', 'id': 'aad18ec27bc049d08d6e71b88886febd', 'name': '财务管理中心', 'parentId': '', 'parentName': ''}, {'fullName': '事业四部', 'id': '918724deb4374ed8a030201c254e2a3d', 'name': '事业四部', 'parentId': '', 'parentName': ''}, {'fullName': '企微', 'id': '6cd71b7095a44df9a761e46537c96fea', 'name': '企微', 'parentId': '', 'parentName': ''}, {'fullName': '综合部', 'id': '35a979b48b6842d5b9d3afc824b9bd5b', 'name': '综合部', 'parentId': '', 'parentName': ''}, {'fullName': '技术委员会', 'id': '48465f5e81e040649d75c301c3bd0632', 'name': '技术委员会', 'parentId': '', 'parentName': ''}, {'fullName': '员工成功部', 'id': '8ccd5f83f2804ba68b93356acf54bc9d', 'name': '员工成功部', 'parentId': '', 'parentName': ''}, {'fullName': '市场运营部', 'id': '6a559eb7afed4a64b08d401beb55d1ce', 'name': '市场运营部', 'parentId': '', 'parentName': ''}, {'fullName': '总办', 'id': 'f161d78396ee4067b5466fd53d34dcff', 'name': '总办', 'parentId': '', 'parentName': ''}, {'fullName': '董办', 'id': '0c2628a266084c4baf0533b0796a3439', 'name': '董办', 'parentId': '', 'parentName': ''}, {'fullName': '人力资源部', 'id': 'e6757d2b66744b17b4bde9c1a2eb9147', 'name': '人力资源部', 'parentId': '', 'parentName': ''}, {'fullName': '事业三部', 'id': '3c241232001a4e858c2ba7a07f41f498', 'name': '事业三部', 'parentId': '', 'parentName': ''}, {'fullName': '质量委员会', 'id': 'a572f0c68d9d47f48c3350a63f498f14', 'name': '质量委员会', 'parentId': '', 'parentName': ''}]})




    def test_05( self ):
        """根据部门ID批量获取部门列表"""
        url = self.domainName + "/open/departments/list?departmentIds=35a979b48b6842d5b9d3afc824b9bd5b&departmentIds=40d0e1cc9c314454a5fc367c85debda1&departmentIds=bee79deb808c49288500059ecbc3faf3"
        print(url)
        response = requests.get(url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': [{'fullName': '综合部', 'id': '35a979b48b6842d5b9d3afc824b9bd5b', 'name': '综合部', 'parentId': '', 'parentName': ''}, {'fullName': '事业一部->业务支持部->设计组->本部', 'id': '40d0e1cc9c314454a5fc367c85debda1', 'name': '本部', 'parentId': 'db9213170de24ad0aee55a70c0776d93', 'parentName': '设计组'}, {'fullName': '综合部->外包清洁', 'id': 'bee79deb808c49288500059ecbc3faf3', 'name': '外包清洁', 'parentId': '35a979b48b6842d5b9d3afc824b9bd5b', 'parentName': '综合部'}]})


    def test_06( self ):
        """根据账号名获取用户"""
        url = self.domainName + "/open/users/account?account="+self.Useraccount
        print(url)
        response = requests.get(url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'account': 'DiaoHuiYun', 'defaultDepartmentId': '6e704cf6f412495697e7265016bc6c13', 'defaultDepartmentName': '', 'departmentIds': ['6e704cf6f412495697e7265016bc6c13'], 'gender': 2, 'id': 'b896c6a0f44b64eb3391e8adfc898e4b', 'name': '刁惠云', 'telephone': '13536270716'}})




    def test_07( self ):
        """根据用户ID获取用户"""
        url = self.domainName + "/open/users/b896c6a0f44b64eb3391e8adfc898e4b"
        print(url)
        response = requests.get(url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'account': 'DiaoHuiYun', 'defaultDepartmentId': '6e704cf6f412495697e7265016bc6c13', 'defaultDepartmentName': '', 'departmentIds': ['6e704cf6f412495697e7265016bc6c13'], 'gender': 2, 'id': 'b896c6a0f44b64eb3391e8adfc898e4b', 'name': '刁惠云', 'telephone': '13536270716'}})


    def test_08( self ):
        """根据用户ID批量获取用户"""
        url = self.domainName + "/open/users/list"+"?userIds=b896c6a0f44b64eb3391e8adfc898e4b&userIds=407b536100b4b9cd5aec7c219837688c&userIds=4f525f49ec82a6190c55c873f15f23e3"
        print(url)
        response = requests.get(url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': [{'account': 'DiaoHuiYun', 'defaultDepartmentId': '6e704cf6f412495697e7265016bc6c13', 'defaultDepartmentName': '', 'departmentIds': ['6e704cf6f412495697e7265016bc6c13'], 'gender': 2, 'id': 'b896c6a0f44b64eb3391e8adfc898e4b', 'name': '刁惠云', 'telephone': '13536270716'}, {'account': 'lijiacheng', 'defaultDepartmentId': '48465f5e81e040649d75c301c3bd0632', 'defaultDepartmentName': '', 'departmentIds': ['48465f5e81e040649d75c301c3bd0632'], 'gender': 1, 'id': '4f525f49ec82a6190c55c873f15f23e3', 'name': '李嘉诚', 'telephone': '13560462483'}, {'account': 'zhaojianrong', 'defaultDepartmentId': '48465f5e81e040649d75c301c3bd0632', 'defaultDepartmentName': '', 'departmentIds': ['48465f5e81e040649d75c301c3bd0632'], 'gender': 1, 'id': '407b536100b4b9cd5aec7c219837688c', 'name': '赵建荣', 'telephone': '15033023704'}]})


    def test_09( self ):
        """根据部门ID获取用户集合(分页)"""
        url = self.domainName + "/open/users?departmentId=c0a65f17979f45f89929b07cda257ba1&page=0&pageSize=5"
        print(url)
        response = requests.get (url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'currPage': 0, 'list': [{'account': 'liuqi', 'defaultDepartmentId': 'c0a65f17979f45f89929b07cda257ba1', 'defaultDepartmentName': '', 'departmentIds': ['c0a65f17979f45f89929b07cda257ba1'], 'gender': 2, 'id': '035d786fd80f1f879ac2099b76c26fb6', 'name': '刘琦', 'telephone': '13250530283'}, {'account': 'zhangyuejuan@auto', 'defaultDepartmentId': 'c0a65f17979f45f89929b07cda257ba1', 'defaultDepartmentName': '', 'departmentIds': ['c0a65f17979f45f89929b07cda257ba1'], 'gender': 2, 'id': '9aab8cbdfcb82c74a00614a3ff2cd49e', 'name': '张月娟', 'telephone': '19806897760'}, {'account': 'luolinyue@A', 'defaultDepartmentId': 'c0a65f17979f45f89929b07cda257ba1', 'defaultDepartmentName': '', 'departmentIds': ['c0a65f17979f45f89929b07cda257ba1'], 'gender': 2, 'id': '9d5736318fdbc51b250cf5a5bdf7e292', 'name': '罗琳月', 'telephone': '17819184847'}, {'account': 'zhanghuanting', 'defaultDepartmentId': 'c0a65f17979f45f89929b07cda257ba1', 'defaultDepartmentName': '', 'departmentIds': ['c0a65f17979f45f89929b07cda257ba1'], 'gender': 1, 'id': '08320a9f851777e6be376d811a786a5c', 'name': '张焕珽', 'telephone': '13808819421'}, {'account': '13751879314', 'defaultDepartmentId': 'c0a65f17979f45f89929b07cda257ba1', 'defaultDepartmentName': '', 'departmentIds': ['c0a65f17979f45f89929b07cda257ba1'], 'gender': 1, 'id': '374dddaafd1fa997133a7e825bdf2378', 'name': '李旭明', 'telephone': '13751879314'}], 'pageSize': 5, 'totalCount': 19, 'totalPage': 4}})