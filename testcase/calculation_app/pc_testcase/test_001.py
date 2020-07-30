# coding=utf-8
import time
import unittest

from public.driver import Driver
from qiqiao_page.pc_page.applicationList_page import ApplicationListPage
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.form_page import FormPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.portal_page import PortalPage
from qiqiao_page.pc_page.process_page import ProcessPage


class CalculationAppTest_001(unittest.TestCase):
    '''PC端公式计算测试应用检查'''



    def setUp(self):
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        time.sleep(5)




    def test_01( self):
        '''PC业务建模公式默认值计算是否生效'''
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '公式计算测试应用')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('子表单')
        time.sleep(5)
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        time.sleep(5)
        formPage = FormPage(self.driver)
        self.assertEqual(formPage.Number_GetValue_Writable("sum"),30.1)
        self.assertEqual(formPage.Number_GetValue_Writable("avg"),7.53)
        self.assertEqual(formPage.Number_GetValue_Writable("乘积"),100)
        self.assertEqual(formPage.Number_GetValue_Writable("公式"),-980)

    def test_02( self):
        '''PC流程公式默认值计算是否生效'''
        portalPage = PortalPage(self.driver)
        # 打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("流程测试")
        formPage = FormPage(self.driver)
        self.assertEqual(formPage.Number_GetValue_Writable("sum"),30.1)
        self.assertEqual(formPage.Number_GetValue_Writable("avg"),7.53)
        self.assertEqual(formPage.Number_GetValue_Writable("乘积"),100)
        self.assertEqual(formPage.Number_GetValue_Writable("公式"),-980)



    def test_03( self):
        '''PC流程子表公式默认值计算是否生效'''
        portalPage = PortalPage(self.driver)
        # 打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("流程测试")
        formPage = FormPage(self.driver)
        self.assertEqual(formPage.Number_GetValue_Writable("sum"),30.1)
        self.assertEqual(formPage.Number_GetValue_Writable("avg"),7.53)
        self.assertEqual(formPage.Number_GetValue_Writable("乘积"),100)
        self.assertEqual(formPage.Number_GetValue_Writable("公式"),-980)
        formPage.ChildForm_AddOneRowButton_Click('子表单')
        time.sleep(2)
        self.assertEqual(formPage.ChildForm_GetTdValue('子表单',1,8),"30.1")
        formPage.ChildForm_List_Text_sendkeys('子表单',1,"整数","30")
        time.sleep(2)
        self.assertEqual(formPage.ChildForm_GetTdValue('子表单',1,8),"50.1")
        formPage.ChildForm_AddOneRowButton_Click('子表单')
        time.sleep(3)
        self.assertEqual(formPage.ChildForm_GetTdValue('子表单',2,8),"30.1")
        formPage.ChildForm_AddOneRowButton_Click('子表单')
        time.sleep(3)
        self.assertEqual(formPage.Number_GetValue_Writable("对子表单整数做计算"),50)
        self.assertEqual(formPage.Number_GetValue_Writable("对子表单小数做计算"),30)
        self.assertEqual(formPage.Number_GetValue_Writable("对子表单金额做计算"),30)
        self.assertEqual(formPage.Number_GetValue_Writable("对子表单百分比做计算"),0.3)
        self.assertEqual(formPage.Number_GetValue_Writable("对子表单公式做计算"),110.3)
        formPage.ChildForm_Record_Delete("子表单",1)
        self.assertEqual(formPage.Number_GetValue_Writable("对子表单整数做计算"),20)
        self.assertEqual(formPage.Number_GetValue_Writable("对子表单小数做计算"),20)
        self.assertEqual(formPage.Number_GetValue_Writable("对子表单金额做计算"),20)
        self.assertEqual(formPage.Number_GetValue_Writable("对子表单百分比做计算"),0.2)
        self.assertEqual(formPage.Number_GetValue_Writable("对子表单公式做计算"),60.3)
