# coding=utf-8
import time
import unittest

from ddt import ddt,data,unpack

from public.driver import Driver
from qiqiao_page.console_page.appManage_page import AppManagePage
from qiqiao_page.console_page.console_login_page import ConsoleLoginPage
from qiqiao_page.console_page.help_page import HelpPage


class ConsoleTest_001(unittest.TestCase):
    '''开发平台检查'''

    driver = Driver().pcdriver()


    def consoleLogin( self,account,password):
        '''开发平台登录'''
        self.driver.maximize_window()
        c = ConsoleLoginPage(self.driver)
        c.user_login("https://qy.do1.com.cn/qiqiao/console",account,password)

    def test_001( self):
        '''帮助中心跳转检查'''
        self.consoleLogin("lijiacheng@AA","qiqiao2020")
        appPage = AppManagePage(self.driver)
        appPage.HeaderPage_topbar_click("帮助")
        time.sleep(2)
        appPage.switch_tab(2)
        help = HelpPage(self.driver)
        help.HelpPage_h4Link_click("快速了解七巧plus")
        time.sleep(2)
        help.switch_tab(3)
        self.assertIn("快速了解七巧Plus · 帮助中心-道一云|七巧",self.driver.title)


