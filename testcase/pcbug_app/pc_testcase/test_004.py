# coding=utf-8
import unittest

from ddt import ddt,data,unpack

from public.driver import Driver
from qiqiao_page.console_page.appManage_page import AppManagePage
from qiqiao_page.console_page.console_login_page import ConsoleLoginPage
from qiqiao_page.console_page.header_page import HeaderPage
import time

from qiqiao_page.pc_page.applicationList_page import ApplicationListPage
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.portal_page import PortalPage


@ddt
class PcBugAppTest_004(unittest.TestCase):
    '''PC端过往补丁4'''

    def pcLogin(self,account,password):
        '''登录pc端'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', account, password)
        time.sleep(3)

    @data(("wujianlun@auto","do1qiqiao",912),
         ("wanghao@auto","do1qiqiao",912),
         ("diaohuiyun@auto","do1qiqiao",912),
          ("luolinyue@auto","do1qiqiao",456),
          ("zhangyuejuan@auto","qiqiao123",0))
    @unpack
    def test_001( self,account,password,result):
        '''【补丁】---列表数据过滤，配置角色范围为自定义时，无效'''
        self.pcLogin(account,password)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '固定资产管理3.0')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('基础管理')
        businessPage.BusinessPage_LeftMenu_Click('资产列表')
        self.assertEqual(result,businessPage.ListComponent_GetRecordTotal())


