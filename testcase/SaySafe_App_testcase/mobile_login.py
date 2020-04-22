# coding=utf-8
import os
import time
import unittest

from public.driver import phonedriver
from qiqiao_PublicPage.mobile_qiqiao_PublicPage.mobile_login_page import MobileLoginPage


class Mobilehome(unittest.TestCase):

    def setUp(self):
        self.driver = phonedriver()
        self.driver.maximize_window()
        loginpage = MobileLoginPage (self.driver)
        loginpage.user_login ('https://qy.do1.com.cn/qiqiao/mruntime', "wujianlun@do1", "do1qiqiao")


    def test_aa(self):
        time.sleep(101)

    def tearDown(self):
        self.driver.quit()