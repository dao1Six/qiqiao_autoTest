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


class HSEAppTest_003(unittest.TestCase):
    '''HSE管理流程检查'''


    def setUp(self):
        '''登录'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        time.sleep(3)




    def test_01( self ):
        '''【补丁】PC运行平台--多表关联组件配置只读，数据列表不显示外键字段值;  移动端--点击编辑进入表单中间表字段值都不显示'''
        portalPage = PortalPage(self.driver)
        #打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(3)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("防护用品申请")
        formPage = FormPage(self.driver)
        formPage.Selection_SingleXiala_Sendkeys("申请原因","到期更换")
        formPage.Text_Sendkeys("原因说明","很大很大空间等哈看进度哈大噶还记得噶还记得噶实践活动")
        formPage.Selection_SingleBox_Sendkeys("检索类别","个人PPE")
        time.sleep(2)
        formPage.MultiForm_BatchManagementButton_Click("用品明细")
        formPage.MultiForm_BathManagePage_Record_Tick("用品明细", [1])
        formPage.MultiForm_BathManagePage_sendkeysTo_Number("用品明细",1,"申请数量",20)
        formPage.MultiForm_BathManagePage_ConfirmButton_Tick("用品明细")
        #检查多表关联组件数据列表显示
        self.assertEqual("口罩",formPage.MultiForm_GetTdValue("用品明细",1,2),msg="用品明细用品名称显示不正确")
        self.assertEqual("个人PPE",formPage.MultiForm_GetTdValue("用品明细",1,3),msg="用品明细类别显示不正确")
        self.assertEqual("50",formPage.MultiForm_GetTdValue("用品明细",1,4),msg="用品明细库存显示不正确")
        self.assertEqual("道一",formPage.MultiForm_GetTdValue("用品明细",1,5),msg="用品明细单位显示不正确")
        self.assertEqual("20",formPage.MultiForm_GetTdValue("用品明细",1,6),msg="用品明细申请数量显示不正确")
        #点击多表关联组件编辑按钮
        formPage.MultiForm_edit_Record("用品明细",1)
        #检查表单弹窗内的数据显示
        time.sleep(2)
        self.assertEqual("口罩",formPage.ForeignSelection_GetValue_writable_InPopup("用品明细","用品名称"),msg="用品明细用品名称显示不正确")
        self.assertEqual("个人PPE",formPage.Selection_SingleXiala_readOnly_InPopup_GetValue("用品明细","类别"),msg="用品明细类别显示不正确")
        self.assertEqual("50",formPage.Number_GetValue_readOnly_InPopup("用品明细","库存"),msg="用品明细库存显示不正确")
        self.assertEqual("道一",formPage.Text_GetValue_readOnly_InPopup("用品明细","单位"),msg="用品明细单位显示不正确")
        self.assertEqual(20,formPage.Number_GetValue_writable_InPopup("用品明细","申请数量"),msg="用品明细申请数量显示不正确")

        formPage.Form_Close_Popup("用品明细")
        time.sleep(1)
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()  # 点击流程办理弹框确认按钮
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第一个人工任务办理失败")
        time.sleep(3)

        # 进行第二个人工任务处理
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        self.assertEqual("口罩",formPage.MultiForm_GetTdValue("用品明细",1,2),msg="用品明细用品名称显示不正确")
        self.assertEqual("个人PPE",formPage.MultiForm_GetTdValue("用品明细",1,3),msg="用品明细类别显示不正确")
        self.assertEqual("50",formPage.MultiForm_GetTdValue("用品明细",1,4),msg="用品明细库存显示不正确")
        self.assertEqual("道一",formPage.MultiForm_GetTdValue("用品明细",1,5),msg="用品明细单位显示不正确")
        self.assertEqual("20",formPage.MultiForm_GetTdValue("用品明细",1,6),msg="用品明细申请数量显示不正确")
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()  # 点击流程办理弹框确认按钮
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第二个人工任务办理失败")
        
        # 进行第三个人工任务处理
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        self.assertEqual("口罩",formPage.MultiForm_GetTdValue("用品明细",1,2),msg="用品明细用品名称显示不正确")
        self.assertEqual("个人PPE",formPage.MultiForm_GetTdValue("用品明细",1,3),msg="用品明细类别显示不正确")
        self.assertEqual("50",formPage.MultiForm_GetTdValue("用品明细",1,4),msg="用品明细库存显示不正确")
        self.assertEqual("道一",formPage.MultiForm_GetTdValue("用品明细",1,5),msg="用品明细单位显示不正确")
        self.assertEqual("20",formPage.MultiForm_GetTdValue("用品明细",1,6),msg="用品明细申请数量显示不正确")
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()  # 点击流程办理弹框确认按钮
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第三个人工任务办理失败")
        
        
        # 进行第四个人工任务处理
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        self.assertEqual("口罩",formPage.MultiForm_GetTdValue("用品明细",1,2),msg="用品明细用品名称显示不正确")
        self.assertEqual("个人PPE",formPage.MultiForm_GetTdValue("用品明细",1,3),msg="用品明细类别显示不正确")
        self.assertEqual("50",formPage.MultiForm_GetTdValue("用品明细",1,4),msg="用品明细库存显示不正确")
        self.assertEqual("道一",formPage.MultiForm_GetTdValue("用品明细",1,5),msg="用品明细单位显示不正确")
        self.assertEqual("20",formPage.MultiForm_GetTdValue("用品明细",1,6),msg="用品明细申请数量显示不正确")
        #
        formPage.MultiForm_Click_Row("用品明细",1)
        #检查表单弹窗内的数据显示
        self.assertEqual("口罩",formPage.ForeignSelection_GetValue_readOnly_InPopup("用品明细","用品名称"),msg="用品明细用品名称显示不正确")
        self.assertEqual("个人PPE",formPage.Selection_SingleXiala_readOnly_InPopup_GetValue("用品明细","类别"),msg="用品明细类别显示不正确")
        self.assertEqual("50",formPage.Number_GetValue_readOnly_InPopup("用品明细","库存"),msg="用品明细库存显示不正确")
        self.assertEqual("道一",formPage.Text_GetValue_readOnly_InPopup("用品明细","单位"),msg="用品明细单位显示不正确")
        self.assertEqual("20",formPage.Number_GetValue_readOnly_InPopup("用品明细","申请数量"),msg="用品明细申请数量显示不正确")
        formPage.Form_Close_Popup("用品明细")
        time.sleep(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()  # 点击流程办理弹框确认按钮
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第四个人工任务办理失败")
