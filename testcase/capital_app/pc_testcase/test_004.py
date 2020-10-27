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
from util.dateTimeUtil import DateTimeUtil


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
        time.sleep(3)

    def test_01( self ):
        '''【补丁】--OA系统中的付款申请流程点击办理时提示按钮执行异常'''
        portalPage = PortalPage(self.driver)
        # 打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(3)
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
        time.sleep(3)


    def test_02( self ):
        '''【补丁】PC运行平台--列表添加按钮发起流程--提示多表关联组件中的字段 值不符合规则'''
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','绩效')
        businessPage = BusinessPage(self.driver)
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage = FormPage(self.driver)
        formPage.Dept_MonomialDept_Sendkeys("考核部门","产品规划组",index=1)
        formPage.Date_Sendkeys("考核日期",DateTimeUtil().Today())
        formPage.MultiForm_BatchManagementButton_Click("考核明细")
        formPage.MultiForm_BathManagePage_Record_Tick("考核明细", [1])
        formPage.MultiForm_BathManagePage_ConfirmButton_Tick("考核明细")
        formPage.Form_Button_Click("发起流程")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()  # 点击流程办理弹框确认按钮
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第一个人工任务办理失败")
        time.sleep(3)
        businessPage.BusinessPage_HeardItem_AllApp_Click()
        portalPage.PortalPage_Click_HeaderMenu("流程")
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.MultiForm_List_click_Td("考核明细",1,7)
        formPage.MultiForm_List_sendkeysTo_Number("考核明细",1,7,50)
        time.sleep(2)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()  # 点击流程办理弹框确认按钮
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第二个人工任务办理失败")
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.MultiForm_List_click_Td("考核明细",1,8)
        formPage.MultiForm_List_sendkeysTo_Number("考核明细",1,8,60)
        formPage.MultiForm_List_sendkeysTo_SingleXiala("考核明细",1,9,"A")
        time.sleep(2)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()  # 点击流程办理弹框确认按钮
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第三个人工任务办理失败")