# coding=utf-8
import os
import time
import unittest
from functools import wraps

from Enum.buttonEnum import ButtonEnum
from public.HTMLTestRunner_cn import _TestResult
from public.driver import Driver
from qiqiao_page.pc_page.applicationList_page import ApplicationListPage
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.form_page import FormPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.popup_form_page import PopupFormPage
from qiqiao_page.pc_page.form_page import FormPage
from qiqiao_page.pc_page.portal_page import PortalPage
from qiqiao_page.pc_page.process_page import ProcessPage
from util.dateTimeUtil import DateTimeUtil
from util.excel_xlrd import ExcelReadUtil


class PcBugAppTest_003(unittest.TestCase):
    '''PC端过往补丁应用3'''



    def pcLogin(self,account,password):
        '''登录pc端'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', account, password)
        time.sleep(3)


    def test_01( self ):
        '''【补丁】---PC运行平台--工作台首页常用应用常用流程丢失'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        self.assertEqual(['美安居建材云办公系统', '加特可人事评价模块'],portalPage.PortalPage_get_commonApplicationList(),msg="常用应用显示不对")
        self.assertEqual(['领用', '归还', '维修', '更换', '报废'],portalPage.PortalPage_get_commonProcessList(),msg="常用流程显示不对")


    def test_02( self ):
        '''工作台页面点击常用流程更多按钮跳转是否正常'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_commonProcessBtnMore()
        processPage=ProcessPage(self.driver)
        self.assertTrue(processPage.ProcessPage_IsIn(),msg="工作台页面点击常用流程更多按钮跳转不成功")

