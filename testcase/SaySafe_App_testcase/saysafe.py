# coding=utf-8
import os
import time
import unittest

from public.driver import pcdriver
from qiqiao_PublicPage.login_page import LoginPage
from qiqiao_PublicPage.portal_page import PortalPage
from qiqiao_PublicPage.applicationList_page import ApplicationListPage


class JinXiaoCun(unittest.TestCase):

    def setUp(self):
        self.driver = pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage (self.driver)
        loginpage.user_login ('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@do1", "do1qiqiao")
        portalpage = PortalPage (self.driver)
        portalpage.click_header_menu ("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.click_application('默认分组', "全员报平安2.2")

    def tearDown(self):
        self.driver.quit()


    def test_add_record(self):
        '''应用管理员录入商品信息开发'''


        time.sleep(9)


