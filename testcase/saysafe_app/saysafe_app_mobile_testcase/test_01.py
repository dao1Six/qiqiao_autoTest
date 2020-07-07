# coding=utf-8
# coding=utf-8
import datetime
import os
import time
import unittest

from ddt import ddt, data, unpack
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options

from app_page_loc.saysafe_app_page.phone.i_declare_peace_page_loc import IDeclarePeacePage
from public.driver import Driver
from qiqiao_page.mobile_page.business_modelId_page import BusinessModelldPage
from qiqiao_page.mobile_page.form_page import FormPage
from qiqiao_page.mobile_page.mobile_login_page import MobileLoginPage
from util.parseExcel import ParseExcel


@ddt
class SaySafeAppTest(unittest.TestCase):

    ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"
    excelPath = ProjectRootPath+"\\testcase\\testcase_data\\测试数据.xlsx"
    sheetName = "SaySafeAppTest"
    excel = ParseExcel(excelPath, sheetName)


    @data(*excel.getSheetValue())
    @unpack

    def test_001( self,a,b,c,d,e ):
        "加法运算"
        self.assertEquals(a,1)

    def setUp(self):
        self.driver = Driver().phonedriver()
        self.driver.maximize_window()
        loginpage = MobileLoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/mruntime', "wujianlun@auto", "do1qiqiao")
        self.driver.refresh()
        #打开“我要报平安页面”
        self.driver.get()





    # def tearDown(self):
    #     self.driver.quit()
