# coding=utf-8
import os
import time
import unittest

from public.driver import Driver
from qiqiao_page.pc_page.login_page import LoginPage
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
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        time.sleep(0.5)
        self.driver.refresh()
        #打开“发起流程列表”
        self.driver.get("https://qy.do1.com.cn/qiqiao/runtime/?corp_id=ww6b6c5c4fa6f34b16#/process/processList")


    def test_01( self ):
        processPage = ProcessPage(self.driver);
        processPage.clickElemByCSS_Presence("p[title='立项申请流程(事业二部)']")
        time.sleep(10)




