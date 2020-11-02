# coding=utf-8
import unittest

from ddt import ddt,data,unpack

from public.driver import Driver
from qiqiao_page.console_page.appManage_page import AppManagePage
from qiqiao_page.console_page.console_login_page import ConsoleLoginPage
from qiqiao_page.console_page.header_page import HeaderPage


@ddt
class ConsoleTest_001(unittest.TestCase):
    '''开发平台检查'''

    def ConsoleLogin( self,account,password ):
        '''开发平台登录'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        c = ConsoleLoginPage(self.driver)
        c.user_login("https://qy.do1.com.cn/qiqiao/console",account,password)

    @data(("lijiacheng@AA",1,"资产管理"),
         ("zhoulin@AA",1,"道一云价值观"),
         ("zhaojiangli@AA",5,"七巧质量管理应用"))
    @unpack
    def test_001( self,account,result,appName):
        '''子管理员登录'''
        self.ConsoleLogin(account,"qiqiao2020")
        a = AppManagePage(self.driver)
        self.assertEqual(a.AppManagePage_get_appNumber(),result)
        self.assertIsNotNone(a.AppManagePage_getAppItemLoc(appName))


    def test_002( self):
        '''【补丁】-正式租户开发平台，登录企业名显示错误'''
        self.ConsoleLogin("lijiacheng@AA","qiqiao2020")
        a = HeaderPage(self.driver)
        self.assertEqual(['', '李嘉诚', '接口自动化七巧'],a.HeaderPage_get_userInfo(),msg="【补丁】-正式租户开发平台，登录企业名显示错误")



