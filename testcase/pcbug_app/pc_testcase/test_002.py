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
from qiqiao_page.pc_page.form_page import FormPage
from qiqiao_page.pc_page.portal_page import PortalPage
from qiqiao_page.pc_page.process_page import ProcessPage
from util.dateTimeUtil import DateTimeUtil


class PcBugAppTest_002(unittest.TestCase):
    '''PC端过往补丁应用2'''

    ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"
    excelPath = ProjectRootPath+"\\file_data\\testcase_data\\测试数据.xlsx"

    def pcLogin(self,account,password):
        '''登录pc端'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', account, password)
        time.sleep(5)


    def test_01( self ):
        '''【补丁】——流程配置子父流程字段传递时，系统报错'''
        self.pcLogin("zhangyuejuan@auto","qiqiao123")
        portalPage = PortalPage(self.driver)
        # 打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(3)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("采购申请")
        formPage = FormPage(self.driver)
        formPage.User_MonomialUser_Sendkeys("人员","张月娟")
        formPage.Date_Sendkeys("日期",DateTimeUtil().Today())
        formPage.Text_Sendkeys("客户","吴健伦")
        formPage.Number_Sendkeys("采购金额",12333)
        formPage.Textarea_Sendkeys("采购说明","的话旮角快点哈数据库大厦的卡士达数据库")
        formPage.FileUpload_Sendkeys("合同",self.excelPath)
        time.sleep(2)
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="发起采购合同申请申请人工任务办理失败")
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="审批采购合同申请任务办理失败")
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="审批采购合同用印申请任务办理失败")
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="审批采购付款申请任务办理失败")
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="审批采购付款申请任务办理失败")




    def test_02( self ):
        '''【补丁】——表单设置唯一校验，在流程中不生效'''
        self.pcLogin("zhangyuejuan@auto","qiqiao123")
        portalPage = PortalPage(self.driver)
        # 打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(3)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("唯一性校验流程")
        formPage = FormPage(self.driver)
        formPage.Text_Sendkeys("客户","440783199406116911")
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('[客户]值必须唯一',formPage.Public_GetAlertMessage(),msg="【补丁】——表单设置唯一校验，在流程中不生效")



    def test_03( self ):
        '''【补丁】——PC运行平台--流程管理，发起人和发起时间不显示'''
        self.pcLogin("zhangyuejuan@auto","qiqiao123")
        portalPage = PortalPage(self.driver)
        # 打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_menu("流程管理")
        processPage.ProcessPage_click_process_record(1)
        time.sleep(3)
        formPage = FormPage(self.driver)
        self.assertNotEqual(formPage.Form_Get_Sponsor(),"",msg="发起人信息错误")
        self.assertNotEqual(formPage.Form_Get_LaunchTime(),"发起时间错误")


    def test_04( self ):
        '''【补丁】PC运行平台-跨应用表单，触发事件，筛选条件配置：外键   id   等于  本表   外键   id，报表单id不存在'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','A')
        businessPage = BusinessPage(self.driver)
        businessPage.ListComponent_Click_ListHeader_Button('添加')
        formPage = FormPage(self.driver)
        formPage.Text_Sendkeys('单行文本1',DateTimeUtil().Today())
        formPage.ForeignSelection_Sendkeys('外键选择1',"c")
        time.sleep(2)
        formPage.Form_Button_Click("提交")
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="触发事件执行失败")
        #点击全部应用选项
        businessPage.BusinessPage_HeardItem_AllApp_Click()
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','B')
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1,3),DateTimeUtil().Today())


    def test_05( self ):
        '''【补丁】-PC运行平台-子表单组件。通过“添加一行按钮”添加数据到第10条的时候。需要点击两次才出来。并且添加后第10条的数据不可用字段必填校验不生效'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','生产运管系统')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('项目信息管理')
        businessPage.BusinessPage_LeftMenu_Click('项目信息管理3')
        # businessPage.ListComponent_Click_ListRow_Button('编辑',1)
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage = FormPage(self.driver)
        formPage.ChildForm_AddOneRowButton_Click("项目团队成员")
        formPage.ChildForm_List_Text_sendkeys("项目团队成员",1,"项目编号","2255555")
        formPage.ChildForm_List_Text_sendkeys("项目团队成员",1,"项目编号","2255555")
        # #把子表数据删至8条
        # TotalRecordNumber = formPage.ChildForm_get_TotalRecordNumber("项目团队成员")
        # while(TotalRecordNumber>8):
        #     formPage.ChildForm_Record_Delete("项目团队成员",TotalRecordNumber)
        #     TotalRecordNumber = TotalRecordNumber-1
        #
        # #添加子表数据到15条
        # formPage.ChildForm_AddOneRowButton_Click("项目团队成员")
        # formPage.ChildForm_List_Text_sendkeys("项目团队成员",9,"项目编号","2255555")




