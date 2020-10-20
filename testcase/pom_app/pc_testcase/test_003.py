# coding=utf-8
import time
import unittest

from public.driver import Driver
from qiqiao_page.pc_page.applicationList_page import ApplicationListPage
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.form_page import FormPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.portal_page import PortalPage
from util.dateTimeUtil import DateTimeUtil


class PomAppTest_003(unittest.TestCase):
    '''生产运营应用PC端组合页面检查'''


    def setUp(self):
        '''登录'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        time.sleep(5)


    def test_01( self ):
        '''组合页面按钮显示'''
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','生产运管系统')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('组合页面')
        self.assertEqual(['导出', '导入', '删除（临时）'],businessPage.ListComponent_Get_ListHeader_Buttons())
        businessPage.ListComponent_containerViewOption_Click(" 视图2")
        self.assertEqual(['导出', '导入', '推送（停用）', '填充未填数据', '删除(临时)'],businessPage.ListComponent_Get_ListHeader_Buttons())


    def test_02( self ):
        '''【补丁】PC运行平台，列表外键查询报系统繁忙'''
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','生产运管系统')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('开票记录管理')
        businessPage.ListComponent_Click_ExpandBtn()
        businessPage.ListComponent_QueryItem_Sendkeys("关联订单编号","aaaaa",QueryItemType="text")
        businessPage.ListComponent_Click_SerachBtn()
        time.sleep(3)
        self.assertEqual(0,businessPage.ListComponent_GetRecordTotal())
