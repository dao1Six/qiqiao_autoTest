# coding=utf-8
import os
import time
import unittest

from public.driver import Driver
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
        portalPage = PortalPage(self.driver)
        self.assertEquals(portalPage.get_loginUser_name(),'王浩')
        #打开“发起流程列表”
        self.driver.get("http://runtime.qwqa.do1.work/?corp_id=wwd5af6a678822e11b#/process/processList")


    def test_01( self ):
        '''道一云生产运营应用，立项申请流程(事业二部)流程'''
        processPage = ProcessPage(self.driver);
        processPage.click_process_icon("立项申请流程(事业二部)")

        formPage = FormPage(self.driver)
        formPage.sendkeysToText("项目名称","中科信息立项申请")
        # formPage.sendkeysToTextarea("项目简介","中科信息立项申请哈哈哈哈哈哈哈")
        #
        # formPage.sendkeysToMonomialDept("所属一级部门","企微")
        # formPage.sendkeysToMonomialDept("所属二级部门", "企微")

        formPage.click_ChildForm_AddButton("关联订单")
        formPage.sendkeysToForeignSelection("关联订单","电信")
        # formPage.sendkeysToMonomialSelect("战略意义","标杆作用")


        time.sleep(20)




