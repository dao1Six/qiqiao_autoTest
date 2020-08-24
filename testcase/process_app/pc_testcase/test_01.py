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


class ProcessAppTest_001(unittest.TestCase):
    '''流程应用检查'''



    def setUp(self):
        '''登录'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        time.sleep(5)

    def pcLogin(self,account,password):
        '''登录pc端'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', account, password)
        time.sleep(5)


    def test_01( self ):
        '''资产管理应用领用流程'''
        portalPage = PortalPage(self.driver)
        #打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("领用")
        formPage = FormPage(self.driver)
        formPage.Selection_CheckboxSelect_Sendkeys("设备类别",["平板","手机"])
        formPage.Textarea_Sendkeys("备注","很大很大空间等哈看进度哈大噶还记得噶还记得噶实践活动")
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()   #点击流程办理弹框确认按钮
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第一个人工任务办理失败")
        time.sleep(5)
        #进行第二个人工任务处理
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.MultiForm_BatchManagementButton_Click("领用明细")
        formPage.MultiForm_BathManagePage_Record_Tick("领用明细", [1, 2])
        formPage.MultiForm_BathManagePage_ConfirmButton_Tick("领用明细")
        self.assertEqual("A1002",formPage.MultiForm_GetTdValue("领用明细", 1, 4),msg="领用明细序列号显示不正确")
        self.assertEqual("I5/8G120SSD+500G", formPage.MultiForm_GetTdValue("领用明细", 2, 5),msg="领用明细配置显示不正确")
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第二个人工任务办理失败")
        time.sleep(2)
        #流程跑完，检查系统任务执行是否正确
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '资产管理')
        businessPage = BusinessPage(self.driver)
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1,7),"已借出",msg="系统任务执行失败")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(2, 7), "已借出",msg="系统任务执行失败")
        time.sleep(10)
        print("检查完成，资产管理领用流程测试通过")

