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


class QuitAppTest_001(unittest.TestCase):
    '''PC端离职人员测试应用检查'''

    def pcLogin(self,account,password):
        '''登录pc端'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', account, password)

    def test_01( self ):
        '''离职人员登录检查'''
        self.pcLogin("liuyan@A1", "qiqiao123")
        loginpage = LoginPage(self.driver)
        self.assertEqual(loginpage.LoginPage_Get_ImMsg(),"账号或密码验证失败")

    def test_02( self ):
        '''检查流程处理人为离职人员时，是否仍然显示'''
        self.pcLogin("wujianlun@A1","qiqiao123")
        portalPage = PortalPage(self.driver)
        # 打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(3)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("离职人员测试流程")
        formPage = FormPage(self.driver)
        formPage.Text_Sendkeys("单行文本","用户")
        formPage.Form_Button_Click("办理")
        self.assertEqual(formPage.Form_Get_ProcessManagers(),["吴健伦"],msg="固定用户人工任务办理者错误")


    def test_03( self ):
        '''检查离职人员列表人员单选查询是否正常'''
        self.pcLogin("wujianlun@A1","qiqiao123")
        time.sleep(5)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','离职人员测试应用')
        businessPage = BusinessPage(self.driver)
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1,3),"刘言",msg="列表人员单选显示离职人员不正确")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1,4),'刘言,王浩',msg="列表人员多选显示离职人员不正确")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1,5),'刘言',msg="列表人员创建人显示离职人员不正确")
        businessPage.ListComponent_QueryItem_Sendkeys("人员单选","刘言",QueryItemType="user")
        businessPage.ListComponent_Click_SerachBtn()
        time.sleep(5)
        self.assertEqual(2,businessPage.ListComponent_GetRecordTotal())

    def test_04( self ):
        '''检查离职人员列表人员多选查询是否正常'''
        self.pcLogin("wujianlun@A1","qiqiao123")
        time.sleep(5)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','离职人员测试应用')
        businessPage = BusinessPage(self.driver)
        businessPage.ListComponent_QueryItem_Sendkeys("人员多选","刘言",QueryItemType="user")
        businessPage.ListComponent_Click_SerachBtn()
        time.sleep(5)
        self.assertEqual(2,businessPage.ListComponent_GetRecordTotal())

    def test_05( self ):
        '''检查离职人员在表单详情中显示是否正确'''
        self.pcLogin("wujianlun@A1","qiqiao123")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','离职人员测试应用')
        time.sleep(2)
        businessPage = BusinessPage(self.driver)
        businessPage.ListComponent_Click_ListRow_Button("详情",1)
        formPage = FormPage(self.driver)
        formPage.Form_Switch_Tab("人员部门类组件")
        self.assertEqual(formPage.User_GetMonomialUserValue_readOnly("人员单选"),"刘言")
        self.assertEqual(formPage.User_GetMultiUserValue_readOnly("人员多选"),["王浩","刘言"])
