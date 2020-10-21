# coding=utf-8
import unittest
import uuid

import requests
import json

from util.codeUtil import CodeUtil


class ConsoleTest_003 (unittest.TestCase):
    '''开发平台集成中心表单接口'''

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
        print(responseJson["data"])
        cls.headers = {
                        "X-Auth0-Token": responseJson["data"],
                        "Content-Type": "application/json"}


    def test_01(self):
        """根据ID获取表单实例数据"""
        url = self.domainName+"/open/applications/e8e7124ff51846118f602b349a1a243a/forms/bab9e16407e349aeb9f4688488e33272/00c01966185f47b0bce05441d83cdfc0"
        print(url)
        response = requests.get (url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson,{'msg': '执行成功', 'code': 0, 'data': {'processInstanceId': None, 'processDefinitionId': None, 'variables': {'生成编码': '00209', '部门单选': '896086cb51aa4f31b3a2e501ec201b71', '地理位置': None, '小数': 1.5, '百分比': 50.0, '级联选择': {'list': [{'id': 'options94207300-aeab-4dc0-9668-8288eb161212', 'value': '男装'}, {'id': 'options98dcfe9b-3378-4035-967d-cc23d86e9c1a', 'value': '衣服'}, {'id': 'options1559ae46-2e2a-4a0f-be28-e56b67086b5a', 'value': '短袖'}]}, '多项选择': ['1', '2'], '评分': 3.0, '日期': 1578240000000, '外键选择': '80343e2daef542a3ae2cab807232330a', '人员多选': ['740905143a3acc008abeed4537781bc5', 'c083aa36e8b0b62960f641c96991f63d', 'f520e04b8cebcbd32fa40a95b72cdb13'], '图片上传': [], '人员单选': 'f520e04b8cebcbd32fa40a95b72cdb13', '单项选择': '1', '地址选择器': {'detail': ' 员村一横路', 'list': [{'id': 'fc86758a9250419d98d55e66b63a582e', 'value': '上海'}, {'id': '7c6f2dfe99f14ef4a84ce6b73120d1e3', 'value': '上海市'}, {'id': 'a57f57636d1840a2aa259d07051285e6', 'value': '黄浦区'}]}, '整数': 1, '单行文本': '道一', '时间': '10:31', '部门多选': ['350d2ddfd3e8432a8381251b8dfce1f5', '49319320942c45bbbb20f934a1bede01', '59725d47a08d416590de18f8eda6b1f4', '896086cb51aa4f31b3a2e501ec201b71'], '数字公式': 2.5, '日期时间': 1578277860000, '多行文本': '道一多行文本', '文件上传': [{'uid': 1600915760823, 'authUrl': '/qiqiao/runtime/api/v1/runtime/forms/bab9e16407e349aeb9f4688488e33272/form_fields/file_upload/key_1578037599818_259018/download?applicationId=e8e7124ff51846118f602b349a1a243a&fileName=SAP%E7%BB%84%E7%BB%87%E3%80%81%E4%BA%BA%E5%91%98%E3%80%81%E5%B2%97%E4%BD%8D%E5%BA%8F%E5%88%97%E5%AD%97%E6%AE%B5%E4%BF%A1%E6%81%AF.xlsx&id=505f3178d5d549408691b7e637cdab19', 'fileSize': 11473, 'name': 'SAP组织、人员、岗位序列字段信息.xlsx', 'hasUploadSuccess': True, 'fileType': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'fileId': '505f3178d5d549408691b7e637cdab19', 'createDate': 1600915758241, 'uploadUser': '740905143a3acc008abeed4537781bc5'}], '子表外键': 'b02c65936bd14fedab6b737e68aef077', '金额': 500.0}, 'author': '740905143a3acc008abeed4537781bc5', 'lastModifier': '740905143a3acc008abeed4537781bc5', 'lastModifierName': '吴健伦', 'version': 3, 'authorName': '吴健伦', 'formDefinitionId': 'bab9e16407e349aeb9f4688488e33272', 'id': '00c01966185f47b0bce05441d83cdfc0', 'applicationId': 'e8e7124ff51846118f602b349a1a243a', 'lastModifyDate': 1600915772000, 'taskId': None, 'createDate': 1595301785000}})




    def test_02(self):
        """获取指定主表数据实例下所有子表的表单实例数据"""
        parentFieldName = CodeUtil.code_quote('子表单')
        url = self.domainName+"/open/applications/e8e7124ff51846118f602b349a1a243a/forms/b02c65936bd14fedab6b737e68aef077/"+parentFieldName+"/ac55d75c96154aaca52d4cc54ff2245e"
        print(url)
        response = requests.get (url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)


    def test_03(self):
        """获取指定表单的分页数据"""
        url = self.domainName+"/open/applications/e8e7124ff51846118f602b349a1a243a/forms/bab9e16407e349aeb9f4688488e33272"
        print(url)
        response = requests.get (url=url,headers=self.headers)
        responseJson = response.json()
        print(responseJson)
        self.assertEqual(responseJson["data"]["list"],[{'processInstanceId': None, 'processDefinitionId': None, 'variables': {'生成编码': '00209', '部门单选': '896086cb51aa4f31b3a2e501ec201b71', '地理位置': None, '小数': 1.5, '百分比': 50.0, '级联选择': {'list': [{'id': 'options94207300-aeab-4dc0-9668-8288eb161212', 'value': '男装'}, {'id': 'options98dcfe9b-3378-4035-967d-cc23d86e9c1a', 'value': '衣服'}, {'id': 'options1559ae46-2e2a-4a0f-be28-e56b67086b5a', 'value': '短袖'}]}, '多项选择': ['1', '2'], '评分': 3.0, '日期': 1578240000000, '外键选择': '80343e2daef542a3ae2cab807232330a', '人员多选': ['740905143a3acc008abeed4537781bc5', 'c083aa36e8b0b62960f641c96991f63d', 'f520e04b8cebcbd32fa40a95b72cdb13'], '图片上传': [], '人员单选': 'f520e04b8cebcbd32fa40a95b72cdb13', '单项选择': '1', '地址选择器': {'detail': ' 员村一横路', 'list': [{'id': 'fc86758a9250419d98d55e66b63a582e', 'value': '上海'}, {'id': '7c6f2dfe99f14ef4a84ce6b73120d1e3', 'value': '上海市'}, {'id': 'a57f57636d1840a2aa259d07051285e6', 'value': '黄浦区'}]}, '整数': 1, '单行文本': '道一', '时间': '10:31', '部门多选': ['350d2ddfd3e8432a8381251b8dfce1f5', '49319320942c45bbbb20f934a1bede01', '59725d47a08d416590de18f8eda6b1f4', '896086cb51aa4f31b3a2e501ec201b71'], '数字公式': 2.5, '日期时间': 1578277860000, '多行文本': '道一多行文本', '文件上传': [{'uid': 1600915760823, 'authUrl': '/qiqiao/runtime/api/v1/runtime/forms/bab9e16407e349aeb9f4688488e33272/form_fields/file_upload/key_1578037599818_259018/download?applicationId=e8e7124ff51846118f602b349a1a243a&fileName=SAP%E7%BB%84%E7%BB%87%E3%80%81%E4%BA%BA%E5%91%98%E3%80%81%E5%B2%97%E4%BD%8D%E5%BA%8F%E5%88%97%E5%AD%97%E6%AE%B5%E4%BF%A1%E6%81%AF.xlsx&id=505f3178d5d549408691b7e637cdab19', 'fileSize': 11473, 'name': 'SAP组织、人员、岗位序列字段信息.xlsx', 'hasUploadSuccess': True, 'fileType': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'fileId': '505f3178d5d549408691b7e637cdab19', 'createDate': 1600915758241, 'uploadUser': '740905143a3acc008abeed4537781bc5'}], '子表外键': 'b02c65936bd14fedab6b737e68aef077', '金额': 500.0}, 'author': '740905143a3acc008abeed4537781bc5', 'lastModifier': '740905143a3acc008abeed4537781bc5', 'lastModifierName': '吴健伦', 'version': 3, 'authorName': '吴健伦', 'formDefinitionId': None, 'id': '00c01966185f47b0bce05441d83cdfc0', 'applicationId': None, 'lastModifyDate': 1600915772000, 'taskId': None, 'createDate': 1595301785000}, {'processInstanceId': None, 'processDefinitionId': None, 'variables': {'生成编码': '00235', '部门单选': '896086cb51aa4f31b3a2e501ec201b71', '地理位置': None, '小数': 1.5, '百分比': 50.0, '级联选择': {'list': [{'id': 'options94207300-aeab-4dc0-9668-8288eb161212', 'value': '男装'}, {'id': 'options98dcfe9b-3378-4035-967d-cc23d86e9c1a', 'value': '衣服'}, {'id': 'options1559ae46-2e2a-4a0f-be28-e56b67086b5a', 'value': '短袖'}]}, '多项选择': ['1', '2'], '评分': 3.0, '日期': 1578240000000, '外键选择': '80343e2daef542a3ae2cab807232330a', '人员多选': ['740905143a3acc008abeed4537781bc5', 'c083aa36e8b0b62960f641c96991f63d', 'f520e04b8cebcbd32fa40a95b72cdb13'], '图片上传': [], '人员单选': 'f520e04b8cebcbd32fa40a95b72cdb13', '单项选择': '1', '地址选择器': {'detail': ' 员村一横路', 'list': [{'id': 'fc86758a9250419d98d55e66b63a582e', 'value': '上海'}, {'id': '7c6f2dfe99f14ef4a84ce6b73120d1e3', 'value': '上海市'}, {'id': 'a57f57636d1840a2aa259d07051285e6', 'value': '黄浦区'}]}, '整数': 1, '单行文本': '道一', '时间': '10:31', '部门多选': ['350d2ddfd3e8432a8381251b8dfce1f5', '49319320942c45bbbb20f934a1bede01', '59725d47a08d416590de18f8eda6b1f4', '896086cb51aa4f31b3a2e501ec201b71'], '数字公式': 2.5, '日期时间': 1578277860000, '多行文本': '道一多行文本', '文件上传': [], '子表外键': 'b02c65936bd14fedab6b737e68aef077', '金额': 500.0}, 'author': '740905143a3acc008abeed4537781bc5', 'lastModifier': '740905143a3acc008abeed4537781bc5', 'lastModifierName': '吴健伦', 'version': 3, 'authorName': '吴健伦', 'formDefinitionId': None, 'id': '0101d0693c9c4424bc036d30c2b8c048', 'applicationId': None, 'lastModifyDate': 1600915772000, 'taskId': None, 'createDate': 1595301785000}, {'processInstanceId': None, 'processDefinitionId': None, 'variables': {'生成编码': '00230', '部门单选': '896086cb51aa4f31b3a2e501ec201b71', '地理位置': None, '小数': 1.5, '百分比': 50.0, '级联选择': {'list': [{'id': 'options94207300-aeab-4dc0-9668-8288eb161212', 'value': '男装'}, {'id': 'options98dcfe9b-3378-4035-967d-cc23d86e9c1a', 'value': '衣服'}, {'id': 'options1559ae46-2e2a-4a0f-be28-e56b67086b5a', 'value': '短袖'}]}, '多项选择': ['1', '2'], '评分': 3.0, '日期': 1578240000000, '外键选择': '80343e2daef542a3ae2cab807232330a', '人员多选': ['740905143a3acc008abeed4537781bc5', 'c083aa36e8b0b62960f641c96991f63d', 'f520e04b8cebcbd32fa40a95b72cdb13'], '图片上传': [], '人员单选': 'f520e04b8cebcbd32fa40a95b72cdb13', '单项选择': '1', '地址选择器': {'detail': ' 员村一横路', 'list': [{'id': 'fc86758a9250419d98d55e66b63a582e', 'value': '上海'}, {'id': '7c6f2dfe99f14ef4a84ce6b73120d1e3', 'value': '上海市'}, {'id': 'a57f57636d1840a2aa259d07051285e6', 'value': '黄浦区'}]}, '整数': 1, '单行文本': '道一', '时间': '10:31', '部门多选': ['350d2ddfd3e8432a8381251b8dfce1f5', '49319320942c45bbbb20f934a1bede01', '59725d47a08d416590de18f8eda6b1f4', '896086cb51aa4f31b3a2e501ec201b71'], '数字公式': 2.5, '日期时间': 1578277860000, '多行文本': '道一多行文本', '文件上传': [], '子表外键': 'b02c65936bd14fedab6b737e68aef077', '金额': 500.0}, 'author': '740905143a3acc008abeed4537781bc5', 'lastModifier': '740905143a3acc008abeed4537781bc5', 'lastModifierName': '吴健伦', 'version': 3, 'authorName': '吴健伦', 'formDefinitionId': None, 'id': '01133bf010e844e6970d4312a7b08e52', 'applicationId': None, 'lastModifyDate': 1600915772000, 'taskId': None, 'createDate': 1595301785000}, {'processInstanceId': None, 'processDefinitionId': None, 'variables': {'生成编码': '00300', '部门单选': '896086cb51aa4f31b3a2e501ec201b71', '地理位置': None, '小数': 1.5, '百分比': 50.0, '级联选择': {'list': [{'id': 'options94207300-aeab-4dc0-9668-8288eb161212', 'value': '男装'}, {'id': 'options98dcfe9b-3378-4035-967d-cc23d86e9c1a', 'value': '衣服'}, {'id': 'options1559ae46-2e2a-4a0f-be28-e56b67086b5a', 'value': '短袖'}]}, '多项选择': ['1', '2'], '评分': 3.0, '日期': 1578240000000, '外键选择': '80343e2daef542a3ae2cab807232330a', '人员多选': ['740905143a3acc008abeed4537781bc5', 'c083aa36e8b0b62960f641c96991f63d', 'f520e04b8cebcbd32fa40a95b72cdb13'], '图片上传': None, '人员单选': 'f520e04b8cebcbd32fa40a95b72cdb13', '单项选择': '1', '地址选择器': {'detail': ' 员村一横路', 'list': [{'id': 'fc86758a9250419d98d55e66b63a582e', 'value': '上海'}, {'id': '7c6f2dfe99f14ef4a84ce6b73120d1e3', 'value': '上海市'}, {'id': 'a57f57636d1840a2aa259d07051285e6', 'value': '黄浦区'}]}, '整数': 1, '单行文本': '道一', '时间': '10:31', '部门多选': ['350d2ddfd3e8432a8381251b8dfce1f5', '49319320942c45bbbb20f934a1bede01', '59725d47a08d416590de18f8eda6b1f4', '896086cb51aa4f31b3a2e501ec201b71'], '数字公式': 2.5, '日期时间': 1578277860000, '多行文本': '道一多行文本', '文件上传': None, '子表外键': None, '金额': 500.0}, 'author': '740905143a3acc008abeed4537781bc5', 'lastModifier': '740905143a3acc008abeed4537781bc5', 'lastModifierName': '吴健伦', 'version': 1, 'authorName': '吴健伦', 'formDefinitionId': None, 'id': '022f6cdcb85c4e9cb2370f5f2e2d72ab', 'applicationId': None, 'lastModifyDate': 1595301785000, 'taskId': None, 'createDate': 1595301785000}, {'processInstanceId': None, 'processDefinitionId': None, 'variables': {'生成编码': '00316', '部门单选': '896086cb51aa4f31b3a2e501ec201b71', '地理位置': None, '小数': 1.5, '百分比': 50.0, '级联选择': {'list': [{'id': 'options94207300-aeab-4dc0-9668-8288eb161212', 'value': '男装'}, {'id': 'options98dcfe9b-3378-4035-967d-cc23d86e9c1a', 'value': '衣服'}, {'id': 'options1559ae46-2e2a-4a0f-be28-e56b67086b5a', 'value': '短袖'}]}, '多项选择': ['1', '2'], '评分': 3.0, '日期': 1578240000000, '外键选择': '80343e2daef542a3ae2cab807232330a', '人员多选': ['740905143a3acc008abeed4537781bc5', 'c083aa36e8b0b62960f641c96991f63d', 'f520e04b8cebcbd32fa40a95b72cdb13'], '图片上传': None, '人员单选': 'f520e04b8cebcbd32fa40a95b72cdb13', '单项选择': '1', '地址选择器': {'detail': ' 员村一横路', 'list': [{'id': 'fc86758a9250419d98d55e66b63a582e', 'value': '上海'}, {'id': '7c6f2dfe99f14ef4a84ce6b73120d1e3', 'value': '上海市'}, {'id': 'a57f57636d1840a2aa259d07051285e6', 'value': '黄浦区'}]}, '整数': 1, '单行文本': '道一', '时间': '10:31', '部门多选': ['350d2ddfd3e8432a8381251b8dfce1f5', '49319320942c45bbbb20f934a1bede01', '59725d47a08d416590de18f8eda6b1f4', '896086cb51aa4f31b3a2e501ec201b71'], '数字公式': 2.5, '日期时间': 1578277860000, '多行文本': '道一多行文本', '文件上传': None, '子表外键': None, '金额': 500.0}, 'author': '740905143a3acc008abeed4537781bc5', 'lastModifier': '740905143a3acc008abeed4537781bc5', 'lastModifierName': '吴健伦', 'version': 1, 'authorName': '吴健伦', 'formDefinitionId': None, 'id': '02395adaf4084c16aff7f8cf5a7a534e', 'applicationId': None, 'lastModifyDate': 1595301785000, 'taskId': None, 'createDate': 1595301785000}, {'processInstanceId': None, 'processDefinitionId': None, 'variables': {'生成编码': '00207', '部门单选': '896086cb51aa4f31b3a2e501ec201b71', '地理位置': None, '小数': 1.5, '百分比': 50.0, '级联选择': {'list': [{'id': 'options94207300-aeab-4dc0-9668-8288eb161212', 'value': '男装'}, {'id': 'options98dcfe9b-3378-4035-967d-cc23d86e9c1a', 'value': '衣服'}, {'id': 'options1559ae46-2e2a-4a0f-be28-e56b67086b5a', 'value': '短袖'}]}, '多项选择': ['1', '2'], '评分': 3.0, '日期': 1578240000000, '外键选择': '80343e2daef542a3ae2cab807232330a', '人员多选': ['740905143a3acc008abeed4537781bc5', 'c083aa36e8b0b62960f641c96991f63d', 'f520e04b8cebcbd32fa40a95b72cdb13'], '图片上传': None, '人员单选': 'f520e04b8cebcbd32fa40a95b72cdb13', '单项选择': '1', '地址选择器': {'detail': ' 员村一横路', 'list': [{'id': 'fc86758a9250419d98d55e66b63a582e', 'value': '上海'}, {'id': '7c6f2dfe99f14ef4a84ce6b73120d1e3', 'value': '上海市'}, {'id': 'a57f57636d1840a2aa259d07051285e6', 'value': '黄浦区'}]}, '整数': 1, '单行文本': '道一', '时间': '10:31', '部门多选': ['350d2ddfd3e8432a8381251b8dfce1f5', '49319320942c45bbbb20f934a1bede01', '59725d47a08d416590de18f8eda6b1f4', '896086cb51aa4f31b3a2e501ec201b71'], '数字公式': 2.5, '日期时间': 1578277860000, '多行文本': '道一多行文本', '文件上传': None, '子表外键': None, '金额': 500.0}, 'author': '740905143a3acc008abeed4537781bc5', 'lastModifier': '740905143a3acc008abeed4537781bc5', 'lastModifierName': '吴健伦', 'version': 1, 'authorName': '吴健伦', 'formDefinitionId': None, 'id': '066c39b5e525433bbd779f76c6c0f341', 'applicationId': None, 'lastModifyDate': 1595301785000, 'taskId': None, 'createDate': 1595301785000}, {'processInstanceId': None, 'processDefinitionId': None, 'variables': {'生成编码': '00291', '部门单选': '896086cb51aa4f31b3a2e501ec201b71', '地理位置': None, '小数': 1.5, '百分比': 50.0, '级联选择': {'list': [{'id': 'options94207300-aeab-4dc0-9668-8288eb161212', 'value': '男装'}, {'id': 'options98dcfe9b-3378-4035-967d-cc23d86e9c1a', 'value': '衣服'}, {'id': 'options1559ae46-2e2a-4a0f-be28-e56b67086b5a', 'value': '短袖'}]}, '多项选择': ['1', '2'], '评分': 3.0, '日期': 1578240000000, '外键选择': '80343e2daef542a3ae2cab807232330a', '人员多选': ['740905143a3acc008abeed4537781bc5', 'c083aa36e8b0b62960f641c96991f63d', 'f520e04b8cebcbd32fa40a95b72cdb13'], '图片上传': None, '人员单选': 'f520e04b8cebcbd32fa40a95b72cdb13', '单项选择': '1', '地址选择器': {'detail': ' 员村一横路', 'list': [{'id': 'fc86758a9250419d98d55e66b63a582e', 'value': '上海'}, {'id': '7c6f2dfe99f14ef4a84ce6b73120d1e3', 'value': '上海市'}, {'id': 'a57f57636d1840a2aa259d07051285e6', 'value': '黄浦区'}]}, '整数': 1, '单行文本': '道一', '时间': '10:31', '部门多选': ['350d2ddfd3e8432a8381251b8dfce1f5', '49319320942c45bbbb20f934a1bede01', '59725d47a08d416590de18f8eda6b1f4', '896086cb51aa4f31b3a2e501ec201b71'], '数字公式': 2.5, '日期时间': 1578277860000, '多行文本': '道一多行文本', '文件上传': None, '子表外键': None, '金额': 500.0}, 'author': '740905143a3acc008abeed4537781bc5', 'lastModifier': '740905143a3acc008abeed4537781bc5', 'lastModifierName': '吴健伦', 'version': 1, 'authorName': '吴健伦', 'formDefinitionId': None, 'id': '0879c6cbc29a477789e32619bc5bfd39', 'applicationId': None, 'lastModifyDate': 1595301785000, 'taskId': None, 'createDate': 1595301785000}, {'processInstanceId': None, 'processDefinitionId': None, 'variables': {'生成编码': '00267', '部门单选': '896086cb51aa4f31b3a2e501ec201b71', '地理位置': None, '小数': 1.5, '百分比': 50.0, '级联选择': {'list': [{'id': 'options94207300-aeab-4dc0-9668-8288eb161212', 'value': '男装'}, {'id': 'options98dcfe9b-3378-4035-967d-cc23d86e9c1a', 'value': '衣服'}, {'id': 'options1559ae46-2e2a-4a0f-be28-e56b67086b5a', 'value': '短袖'}]}, '多项选择': ['1', '2'], '评分': 3.0, '日期': 1578240000000, '外键选择': '80343e2daef542a3ae2cab807232330a', '人员多选': ['740905143a3acc008abeed4537781bc5', 'c083aa36e8b0b62960f641c96991f63d', 'f520e04b8cebcbd32fa40a95b72cdb13'], '图片上传': None, '人员单选': 'f520e04b8cebcbd32fa40a95b72cdb13', '单项选择': '1', '地址选择器': {'detail': ' 员村一横路', 'list': [{'id': 'fc86758a9250419d98d55e66b63a582e', 'value': '上海'}, {'id': '7c6f2dfe99f14ef4a84ce6b73120d1e3', 'value': '上海市'}, {'id': 'a57f57636d1840a2aa259d07051285e6', 'value': '黄浦区'}]}, '整数': 1, '单行文本': '道一', '时间': '10:31', '部门多选': ['350d2ddfd3e8432a8381251b8dfce1f5', '49319320942c45bbbb20f934a1bede01', '59725d47a08d416590de18f8eda6b1f4', '896086cb51aa4f31b3a2e501ec201b71'], '数字公式': 2.5, '日期时间': 1578277860000, '多行文本': '道一多行文本', '文件上传': None, '子表外键': None, '金额': 500.0}, 'author': '740905143a3acc008abeed4537781bc5', 'lastModifier': '740905143a3acc008abeed4537781bc5', 'lastModifierName': '吴健伦', 'version': 1, 'authorName': '吴健伦', 'formDefinitionId': None, 'id': '0bb62a90191d44afbc4cda46e7d52dc9', 'applicationId': None, 'lastModifyDate': 1595301785000, 'taskId': None, 'createDate': 1595301785000}, {'processInstanceId': None, 'processDefinitionId': None, 'variables': {'生成编码': '00234', '部门单选': '896086cb51aa4f31b3a2e501ec201b71', '地理位置': None, '小数': 1.5, '百分比': 50.0, '级联选择': {'list': [{'id': 'options94207300-aeab-4dc0-9668-8288eb161212', 'value': '男装'}, {'id': 'options98dcfe9b-3378-4035-967d-cc23d86e9c1a', 'value': '衣服'}, {'id': 'options1559ae46-2e2a-4a0f-be28-e56b67086b5a', 'value': '短袖'}]}, '多项选择': ['1', '2'], '评分': 3.0, '日期': 1578240000000, '外键选择': '80343e2daef542a3ae2cab807232330a', '人员多选': ['740905143a3acc008abeed4537781bc5', 'c083aa36e8b0b62960f641c96991f63d', 'f520e04b8cebcbd32fa40a95b72cdb13'], '图片上传': None, '人员单选': 'f520e04b8cebcbd32fa40a95b72cdb13', '单项选择': '1', '地址选择器': {'detail': ' 员村一横路', 'list': [{'id': 'fc86758a9250419d98d55e66b63a582e', 'value': '上海'}, {'id': '7c6f2dfe99f14ef4a84ce6b73120d1e3', 'value': '上海市'}, {'id': 'a57f57636d1840a2aa259d07051285e6', 'value': '黄浦区'}]}, '整数': 1, '单行文本': '道一', '时间': '10:31', '部门多选': ['350d2ddfd3e8432a8381251b8dfce1f5', '49319320942c45bbbb20f934a1bede01', '59725d47a08d416590de18f8eda6b1f4', '896086cb51aa4f31b3a2e501ec201b71'], '数字公式': 2.5, '日期时间': 1578277860000, '多行文本': '道一多行文本', '文件上传': None, '子表外键': None, '金额': 500.0}, 'author': '740905143a3acc008abeed4537781bc5', 'lastModifier': '740905143a3acc008abeed4537781bc5', 'lastModifierName': '吴健伦', 'version': 1, 'authorName': '吴健伦', 'formDefinitionId': None, 'id': '0c06bc2b816a45ca904fe1ed66423714', 'applicationId': None, 'lastModifyDate': 1595301785000, 'taskId': None, 'createDate': 1595301785000}, {'processInstanceId': None, 'processDefinitionId': None, 'variables': {'生成编码': '00309', '部门单选': '896086cb51aa4f31b3a2e501ec201b71', '地理位置': None, '小数': 1.5, '百分比': 50.0, '级联选择': {'list': [{'id': 'options94207300-aeab-4dc0-9668-8288eb161212', 'value': '男装'}, {'id': 'options98dcfe9b-3378-4035-967d-cc23d86e9c1a', 'value': '衣服'}, {'id': 'options1559ae46-2e2a-4a0f-be28-e56b67086b5a', 'value': '短袖'}]}, '多项选择': ['1', '2'], '评分': 3.0, '日期': 1578240000000, '外键选择': '80343e2daef542a3ae2cab807232330a', '人员多选': ['740905143a3acc008abeed4537781bc5', 'c083aa36e8b0b62960f641c96991f63d', 'f520e04b8cebcbd32fa40a95b72cdb13'], '图片上传': None, '人员单选': 'f520e04b8cebcbd32fa40a95b72cdb13', '单项选择': '1', '地址选择器': {'detail': ' 员村一横路', 'list': [{'id': 'fc86758a9250419d98d55e66b63a582e', 'value': '上海'}, {'id': '7c6f2dfe99f14ef4a84ce6b73120d1e3', 'value': '上海市'}, {'id': 'a57f57636d1840a2aa259d07051285e6', 'value': '黄浦区'}]}, '整数': 1, '单行文本': '道一', '时间': '10:31', '部门多选': ['350d2ddfd3e8432a8381251b8dfce1f5', '49319320942c45bbbb20f934a1bede01', '59725d47a08d416590de18f8eda6b1f4', '896086cb51aa4f31b3a2e501ec201b71'], '数字公式': 2.5, '日期时间': 1578277860000, '多行文本': '道一多行文本', '文件上传': None, '子表外键': None, '金额': 500.0}, 'author': '740905143a3acc008abeed4537781bc5', 'lastModifier': '740905143a3acc008abeed4537781bc5', 'lastModifierName': '吴健伦', 'version': 1, 'authorName': '吴健伦', 'formDefinitionId': None, 'id': '1222f601294b43cbad9af1ba6a95ad3f', 'applicationId': None, 'lastModifyDate': 1595301785000, 'taskId': None, 'createDate': 1595301785000}])



