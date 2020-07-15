# coding=utf-8
import unittest

from ddt import ddt,data,unpack

from public.driver import Driver
from qiqiao_page.console_page.appManage_page import AppManagePage
from qiqiao_page.console_page.console_login_page import ConsoleLoginPage


@ddt
class ConsoleTest_001(unittest.TestCase):
    '''开发平台检查'''



    @data(("lijiacheng@AA",1,"资产管理"),
         ("zhoulin@AA",1,"道一云价值观"),
         ("zhaojiangli@AA",5,"七巧质量管理应用"))
    @unpack
    def test_001( self,account,result,appName):
        '''子管理员登录'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        c = ConsoleLoginPage(self.driver)
        c.user_login("https://qy.do1.com.cn/qiqiao/console",account,"qiqiao2020")
        a = AppManagePage(self.driver)
        self.assertEqual(a.AppManagePage_get_appNumber(),result)
        self.assertIsNotNone(a.AppManagePage_getAppItemLoc(appName))


