# coding=utf-8
import time
import unittest

from public.driver import Driver
from qiqiao_page.mobile_page.business_components.mb_list_component import MbListComponent
from qiqiao_page.mobile_page.mb_form_page import MbFormPage
from qiqiao_page.mobile_page.mobile_application_page import MbApplicationListPage
from qiqiao_page.mobile_page.mobile_home_page import MbHomePage
from qiqiao_page.mobile_page.mobile_login_page import MbLoginPage
from qiqiao_page.pc_page.applicationList_page import ApplicationListPage
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.form_page import FormPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.portal_page import PortalPage
from util.dateTimeUtil import DateTimeUtil


class MbBugAppTest_001(unittest.TestCase):
    '''移动端过往补丁'''


    def setUp(self):
        '''登录'''
        self.mbLogin("wujianlun@auto","do1qiqiao")


    def mbLogin(self,account,password):
        '''登录移动端'''
        self.driver = Driver().phonedriver()
        self.driver.maximize_window()
        loginpage = MbLoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/mruntime', account, password)
        time.sleep(5)


    def test_01( self ):
        '''【补丁】移动端运行平台，分组可见条件无效'''
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('外键数据升级','分组可见')
        listPage = MbListComponent(self.driver)
        listPage.MbListComponent_AddButton_Click()
        formPage = MbFormPage(self.driver)
        formPage.MbSelection_SingleBox_Senkeys("单项选择","选项一")
        self.assertTrue(formPage.MbText_IsVisible("单行文本"))
        formPage.MbSelection_SingleBox_Senkeys("单项选择","选项二")
        time.sleep(1)
        self.assertFalse(formPage.MbText_IsVisible("单行文本"))
        self.assertTrue(formPage.MbNumber_IsVisible("数字"))


    def test_02( self ):
        '''【补丁】移动端运行平台，在组织架构顶部搜索选择人员时，部门选择连带写入无效'''
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('外键数据升级','分组可见')
        self.driver.refresh()
        time.sleep(1)
        listPage = MbListComponent(self.driver)
        listPage.MbListComponent_AddButton_Click()
        formPage = MbFormPage(self.driver)
        formPage.MbUser_MonomialUser_Sendkeys("人员单选","吴健伦")
        time.sleep(1)
        self.assertEqual(formPage.MbDept_MonomialDept_GetValue("部门单选"),'创新技术中心->产品研发二部->产品规划组产品规划组')

