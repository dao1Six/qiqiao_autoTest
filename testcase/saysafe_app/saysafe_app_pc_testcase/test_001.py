# coding=utf-8
import os
import time
import unittest
from functools import wraps

from public.HTMLTestRunner_cn import _TestResult
from public.driver import Driver
from qiqiao_page.pc_page.applicationList_page import ApplicationListPage
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.form_page import FormPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.popup_form_page import PopupFormPage
from qiqiao_page.pc_page.portal_page import PortalPage
from qiqiao_page.pc_page.process_page import ProcessPage
from util.dateTimeUtil import DateTimeUtil
from util.parseExcel import ParseExcel


class PomAppTest_001(unittest.TestCase):
    '''PC生产运营应用流程操作'''



    def dataPrepare( self ):
        '''数据准备'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        time.sleep(10)
        # 打开生产运营管理应用
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '生产运管系统')
        businessPage = BusinessPage(self.driver)
        # 清除订单管理相关数据
        # 判断列表是否存在数据
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除（临时）')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        # 清除内部订单管理相关数据
        # 判断列表是否存在数据
        businessPage.BusinessPage_LeftMenu_Click('内部订单管理')
        businessPage.BusinessPage_LeftMenu_Click('内部订单管理2')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除（临时）')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        # 清除资源借调信息相关数据
        businessPage.BusinessPage_LeftMenu_Click('资源借调信息')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        # 清除借调结算管理相关数据
        businessPage.BusinessPage_LeftMenu_Click('借调结算管理')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除（临时）')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        # 清除其他结算管理相关数据
        businessPage.BusinessPage_LeftMenu_Click('其他结算管理')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除（临时）')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()

        # 清除项目信息管理相关数据
        businessPage.BusinessPage_LeftMenu_Click('项目信息管理')
        businessPage.BusinessPage_LeftMenu_Click('里程碑信息')
        if (businessPage.ListComponent_GetRecordTotal() >0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        time.sleep(2)
        businessPage.BusinessPage_LeftMenu_Click('项目信息管理2')
        if (businessPage.ListComponent_GetRecordTotal() >= 3):
            businessPage.ListComponent_checkbox_Click(1)
            businessPage.ListComponent_Click_ListHeader_Button('删除（临时）')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        time.sleep(2)
        portalPage.PortalPage_qiqiao_logout()
        self.driver.quit()

    # @classmethod
    # def setUpClass(self):
    #     self.dataPrepare(self)


    def setUp(self):
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        time.sleep(5)




    def test_01( self ):
        '''88'''
        # 打开生产运营管理应用
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_CloseStep2Tip()
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','全员报平安2.2')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('报平安')
        businessPage.ListComponent_Click_ListHeader_Button('添加')
        popFormPage = PopupFormPage(self.driver)
        popFormPage.PopupFormPage_Button_Click('提交')
        time.sleep(10)























