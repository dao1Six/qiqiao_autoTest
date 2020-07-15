# coding=utf-8
import time
import unittest

from public.driver import Driver
from qiqiao_page.mobile_page.mb_business_page import MbBusinessPage
from qiqiao_page.mobile_page.mobile_application_page import MbApplicationListPage
from qiqiao_page.mobile_page.mobile_home_page import MbHomePage
from qiqiao_page.mobile_page.mobile_login_page import MbLoginPage


class MbCapitalAppTest_002(unittest.TestCase):
    '''移动端资产管理应用流程检查'''

    def setUp(self):
        '''登录'''
        self.mbLogin("wanghao@auto","do1qiqiao")

    def mbLogin(self,account,password):
        '''登录pc端'''
        self.driver = Driver().phonedriver()
        self.driver.maximize_window()
        loginpage = MbLoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/mruntime', account, password)
        time.sleep(5)

    def test_01( self ):
        '''移动端运行平台，导航列表发起流程设置可见范围小于流程发布范围时，发起流程'''
        homePage = MbHomePage(self.driver)
        homePage.HomePage_BottomNav_Click("应用")
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('资产管理','资产管理')
        businessPage = MbBusinessPage(self.driver)
        businessPage.MbNavigationComponent_Click_Navigation("领用")
        time.sleep(2)
