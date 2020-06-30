# coding=utf-8
import time
import unittest

from public.driver import Driver
from qiqiao_page.pc_page.login_page import LoginPage


class CapitalAppTest_001(unittest.TestCase):



    def setUp(self):
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        time.sleep(5)
