# coding=utf-8
import os
import time
import unittest

from public.driver import Driver
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.form_page import FormPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.portal_page import PortalPage
from qiqiao_page.pc_page.process_page import ProcessPage
from util.parseExcel import ParseExcel


class PomAppTest_001(unittest.TestCase):


    # ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"
    # excelPath = ProjectRootPath+"\\testcase\\testcase_data\\user_token.xlsx"
    # sheetName = "user_token"
    # excel = ParseExcel(excelPath, sheetName)
    # accountList = excel.getColValues(1)
    # tokenList = excel.getColValues(2)
    # userDict = dict(zip(accountList, tokenList))

    def setUp(self):
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('http://runtime.qwqa.do1.work', "wanghao@uat", "qiqiao123")
        time.sleep(5)




    def test_01( self ):
        '''道一云生产运营应用，立项申请流程(事业二部)流程'''
        portalPage = PortalPage(self.driver)
        self.assertEquals(portalPage.get_loginUser_name(),'王浩')
        #打开“发起流程列表”
        portalPage.click_header_menu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.click_process_icon("立项申请流程(事业二部)")

        formPage = FormPage(self.driver)
        formPage.sendkeysToText("项目名称","中科信息立项申请")
        formPage.sendkeysToTextarea("项目简介","中科信息立项申请哈哈哈哈哈哈哈")
        #
        # formPage.sendkeysToMonomialDept("所属一级部门","企微")
        # formPage.sendkeysToMonomialDept("所属二级部门", "企微")
        self.assertEquals(formPage.getMonomialUserValue_readOnly("项目经理"),"王浩")

        #点击管理订单添加按钮字段
        formPage.click_ChildForm_AddButton("关联订单")
        formPage.sendkeysToForeignSelection("关联订单","电信")
        time.sleep(1)
        formPage.sendkeysToMonomialSelect("战略意义","标杆作用")
        formPage.sendkeysToNumber("预估成本（人天）",10)
        #点击子表保存按钮
        formPage.click_ChildForm_Button('保存')

        print(formPage.getNumberValue_readOnly("项目总金额"))
        print(formPage.getNumberValue_readOnly("项目预估总成本（人天）"))
        print(formPage.getDateValue_writable("项目启动时间"))
        print(formPage.getSelectionBoxValue_writable("项目类型"))
        time.sleep(1)
        formPage.sendkeysToMonomialSelect('项目等级','普通（普）')
        formPage.sendkeysToDate("预计验收时间","2020-06-22")
        formPage.sendkeysToText("客户名称", "李嘉诚")
        formPage.sendkeysToText("甲方对接人", "李嘉诚")
        formPage.sendkeysToText("联系方式", "13025805485")
        formPage.sendkeysToTextarea("备注信息", "中科信息立项申请哈哈哈哈哈哈哈")

        # 点击项目里程碑添加按钮字段
        formPage.click_ChildForm_AddButton("项目里程碑")
        formPage.sendkeysToText("阶段名称", "测试")
        formPage.sendkeysToText("计划完成时间", "2020-06-22")
        # 点击子表保存按钮
        formPage.click_ChildForm_Button('保存')
        formPage.clickFormButton("提交")
        formPage.selectProcessManager(["王浩"])
        time.sleep(5)
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        formPage.clickFormButton("提交")



    def test_02( self ):
        self.driver.get("http://runtime.qwqa.do1.work/?corp_id=wwd5af6a678822e11b#/application/business?applicationId=b289921621e245e2a114c481ddfc4304&mainColor=orange&businessModelId=e532fc5dc28d414ba10b4311bb2c31da")
        businessPage = BusinessPage(self.driver)
        businessPage.click_ListHeader_Button("添加工时")
        formPage = FormPage(self.driver)
        formPage.click_ChildForm_AddButton('工时明细')
        formPage.sendkeysToRadioSelect("工时类型","产品研发工作")
        time.sleep(1)
        formPage.sendkeysToForeignSelection("产品名称","测试20")
        formPage.sendkeysToMonomialSelect("工作内容","产品测试")
        formPage.click_ChildForm_Button("保存")
        time.sleep(5)











