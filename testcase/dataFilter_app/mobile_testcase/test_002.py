# coding=utf-8
import time
import unittest

from ddt import ddt,data,unpack

from public.driver import Driver
from qiqiao_page.mobile_page.business_components.mb_list_component import MbListComponent
from qiqiao_page.mobile_page.mb_business_page import MbBusinessPage
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


class MbDataFilterAppTest_002(unittest.TestCase):
    '''移动端数据过滤测试应用数据显示及数据过滤检查'''

    def mbLogin(self,account,password):
        '''登录移动端'''
        self.driver = Driver().phonedriver()
        self.driver.maximize_window()
        loginpage = MbLoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/mruntime', account, password)
        time.sleep(5)


    def setUp(self):
        self.mbLogin("wujianlun@auto","do1qiqiao")


    def test_01( self):
        '''移动端列表数据单行文本搜索检查'''
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('数据过滤测试应用','基础表单数据列表')
        mbBusinessPage = MbBusinessPage(self.driver)
        mbBusinessPage.MbListComponent_searchInput_Sendkeys("七巧")
        mbBusinessPage.Public_Alert_disappear()
        #检查记录状态值
        # self.assertEqual(mbBusinessPage.MbListComponent_Get_RecoreStatusValule(1),result1)
        print(mbBusinessPage.MbListComponent_Get_RecoreStatusValule(1))
        #检查记录文本值
        # self.assertEqual(mbBusinessPage.MbListComponent_Get_RecoreTextContents(1),result2)
        print(mbBusinessPage.MbListComponent_Get_RecoreTextContents(1))
        mbBusinessPage.MbListComponent_Recore_Click(2)
        time.sleep(5)
        self.driver.back()
        print(mbBusinessPage.MbListComponent_Get_RecoreStatusValule(1))
        print(mbBusinessPage.MbListComponent_Get_RecoreTextContents(1))