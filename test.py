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


class CapitalAppTest_001(unittest.TestCase):
    '''PC端资产管理应用流程检查'''


    def setUp(self):
        '''登录'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        time.sleep(5)



    def test_01( self ):
        '''资产管理应用领用流程'''
        portalPage = PortalPage(self.driver)
        #打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_get_processTdValue(1,3)
        portalPage.clickElemByXpath_visibility("//div[@class='el-form-item status-other']//input")
        time.sleep(2)
        portalPage.clickElemByXpath_visibility("//span[text()='进行中']")
        time.sleep(2)
        portalPage.clickElemByXpath_visibility("//button[@class='el-button el-button--default']",index=0)
        r = 1
        for i in range(100):
            processPage.ProcessPage_click_process_record(r)
            formPage = FormPage(self.driver)
            if(formPage.FormPage_button_isExistence("终止")==True):
                formPage.Form_Button_Click("终止")
                formPage.clickElemByXpath_visibility("//span[text()='确 定']")   #点击流程办理弹框确认按钮
                formPage.Public_GetAlertMessage()

            else:
                r = r+1
                formPage.clickElemByXpath_visibility("//i[@class='el-icon-close close']")
                while(r>10):
                    r = 1
                    #点击下一页
                    formPage.clickElemByXpath_visibility("//i[@class='el-icon el-icon-arrow-right']")
                    time.sleep(3)

