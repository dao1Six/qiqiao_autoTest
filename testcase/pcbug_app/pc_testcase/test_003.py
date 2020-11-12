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


    def test_03( self ):
        '''工作台页面点击常用应用更多按钮跳转是否正常'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_commonAppBtnMore()
        applicationListPage=ApplicationListPage(self.driver)
        self.assertTrue(applicationListPage.ApplicationListPage_IsIn(),msg="工作台页面点击常用流程更多按钮跳转不成功")

    def test_04( self ):
        '''【补丁】---pc运行平台，编辑按钮页面，子表单数据，点击编辑第二条子表单数据，编辑页面显示第一条数据'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage=PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage=ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','数据过滤测试应用')
        businessPage=BusinessPage(self.driver)
        time.sleep(2)
        businessPage.BusinessPage_LeftMenu_Click('子表')
        businessPage.ListComponent_Click_ListRow_Button("编辑",1)
        formPage=FormPage(self.driver)
        formPage.ChildForm_Record_Edit("子表单",3)
        self.assertEqual("00230",formPage.SerialNumber_GetValue_readOnly_InPopup("子表单","生成编码"),msg="【补丁】---pc运行平台，编辑按钮页面，子表单数据，点击编辑第二条子表单数据，编辑页面显示第一条数据")
        formPage.Form_Close_Popup("子表单")
        time.sleep(2)
        formPage.ChildForm_Record_Edit("子表单",1)
        self.assertEqual("00209",formPage.SerialNumber_GetValue_readOnly_InPopup("子表单","生成编码"),msg="【补丁】---pc运行平台，编辑按钮页面，子表单数据，点击编辑第二条子表单数据，编辑页面显示第一条数据")



    def test_05( self ):
        '''【补丁】--PC端/移动端--开发平台人员单选配置用户所属部门人员，运行平台通过搜索用户所属部门下的子部门的人员，显示暂无数据'''
        self.pcLogin("pengzheng@A1","qiqiao123")
        portalPage=PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage=ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','补丁应用')
        businessPage=BusinessPage(self.driver)
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage=FormPage(self.driver)
        formPage.User_click_UserSelectBox("人员单选1")
        formPage.User_sendkeys_UserSearch("王栋一")
        self.assertTrue(formPage.User_UserSearchOption_IsExist("王栋一"))


    def test_06( self ):
        '''【补丁】---字段设置外键字段为可用条件外键不等于空值，外键设置可选无，选择“无”时，可用条件失效（“无”为空值）'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage=PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage=ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','PC端补丁收集应用')
        businessPage=BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('外键不为空表单列表')
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage=FormPage(self.driver)
        self.assertFalse(formPage.Form_field_isVisibility("单行文本"))
        formPage.ForeignSelection_Sendkeys("外键选择1","无")
        time.sleep(2)
        self.assertFalse(formPage.Form_field_isVisibility("单行文本"))
        formPage.ForeignSelection_Sendkeys("外键选择1","吴健伦")
        time.sleep(2)
        self.assertTrue(formPage.Form_field_isVisibility("单行文本"))
