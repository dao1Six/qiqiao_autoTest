# coding=utf-8
import time
import unittest

from public.driver import Driver
from qiqiao_page.mobile_page.mb_form_page import MbFormPage
from qiqiao_page.mobile_page.mobile_home_page import MbHomePage
from qiqiao_page.mobile_page.mobile_login_page import MbLoginPage
from qiqiao_page.mobile_page.mobile_to_do_page import MbTodoPage
from qiqiao_page.pc_page.applicationList_page import ApplicationListPage
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.portal_page import PortalPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.mobile_page.mobile_application_page import MbApplicationListPage
from qiqiao_page.okr_page.mb_okr_page import MbOkrPage



class MbOkrAppTest_001(unittest.TestCase):
    """移动端OKR应用检查"""



    def mbLogin(self,account,password):
        """登录移动端"""
        self.driver = Driver().phonedriver()
        self.driver.maximize_window()
        loginpage = MbLoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/mruntime', account, password)
        time.sleep(3)



    def test_01( self ):
        """【补丁】---windows环境-PC企业微信OKR应用--全员OKR页面打开空白"""
        self.mbLogin("D001186","do1qiqiao")
        homePage = MbHomePage(self.driver)
        homePage.HomePage_BottomNav_Click("应用")
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('全员OKR','全员OKR')
        mbOkrPage =MbOkrPage(self.driver)
        time.sleep(5)
        mbOkrPage.MbOkrPage_switch_iframeElem()
        self.assertEqual("提高自动化测试框架稳定性及速度，七巧发版质量",mbOkrPage.MbOkrPage_get_O(),"okr目标显示值不对")
        self.assertEqual("自动化用例编写100条",mbOkrPage.MbOkrPage_get_KRs(1),msg="okr目标显示值不对")
