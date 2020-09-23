# coding=utf-8
import os
import time
import unittest

from public.driver import Driver
from qiqiao_page.pc_page.applicationList_page import ApplicationListPage
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.form_page import FormPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.portal_page import PortalPage
from qiqiao_page.pc_page.process_page import ProcessPage


class OAAppTest_004(unittest.TestCase):
    '''OA流程检查'''

    ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"
    excelPath = ProjectRootPath+"\\file_data\\testcase_data\\测试数据.xlsx"

    def setUp( self ):
        '''登录'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime',"wujianlun@auto","do1qiqiao")
        time.sleep(5)

    def test_01( self ):
        '''【补丁】--OA系统中的付款申请流程点击办理时提示按钮执行异常'''
        portalPage = PortalPage(self.driver)
        # 打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("付款申请流程")
        formPage = FormPage(self.driver)
        formPage.Selection_SingleXiala_Sendkeys("付款类型","供应商付款")
        formPage.ForeignSelection_Sendkeys("付款账户","8110901013400680320")
        formPage.FileUpload_Sendkeys("付款凭证",self.excelPath)
        formPage.Text_Sendkeys("付款标题","很大很大空间等哈看进度哈大噶还记得噶还记得噶实践活动")
        formPage.ForeignSelection_Sendkeys("供应商","广州市锌云信息科技有限公司")
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()  # 点击流程办理弹框确认按钮
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第一个人工任务办理失败")
        time.sleep(5)


