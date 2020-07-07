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
    '''资产管理应用流程检查'''


    @classmethod
    def setUpClass(self):
        '''初始化资产列表数据'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        time.sleep(3)
        #打开资产管理应用，资产列表把所有的资产设置为可借出状态
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','资产管理')
        businessPage = BusinessPage(self.driver)

        businessPage.ListComponent_SelectAllRecord()
        time.sleep(2)
        businessPage.ListComponent_Click_ListHeader_Button('设置为可借出')
        businessPage.ListComponent_TooltipButton_Click('确定')
        time.sleep(2)
        #清除领用及相关数据
        businessPage.BusinessPage_LeftMenu_Click('领用管理')
        businessPage.BusinessPage_LeftMenu_Click('领用单')
        #判断列表是否存在数据
        if(businessPage.ListComponent_GetRecordTotal()>0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功'in  businessPage.Public_GetAlertMessage()

        businessPage.BusinessPage_LeftMenu_Click('领用明细')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        #清除维修管理相关数据
        businessPage.BusinessPage_LeftMenu_Click('维修管理')
        businessPage.BusinessPage_LeftMenu_Click('维修单')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功'in  businessPage.Public_GetAlertMessage()
        businessPage.BusinessPage_LeftMenu_Click('维修明细')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功'in  businessPage.Public_GetAlertMessage()
        #清除归还管理相关数据
        businessPage.BusinessPage_LeftMenu_Click('归还管理')
        businessPage.BusinessPage_LeftMenu_Click('归还单')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功'in  businessPage.Public_GetAlertMessage()
        businessPage.BusinessPage_LeftMenu_Click('归还明细')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功'in  businessPage.Public_GetAlertMessage()
        businessPage.BusinessPage_LeftMenu_Click('更换管理')
        businessPage.BusinessPage_LeftMenu_Click('更换单')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功'in  businessPage.Public_GetAlertMessage()

        time.sleep(2)
        portalPage.PortalPage_qiqiao_logout()
        self.driver.quit()

    def setUp(self):
        '''登录'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        time.sleep(5)

    # def tearDown(self):
    #     '''关闭浏览器'''
    #     self.driver.quit()





    def test_01( self ):
        '''资产管理应用领用流程'''
        portalPage = PortalPage(self.driver)
        #打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.click_process_icon("领用")
        formPage = FormPage(self.driver)
        formPage.Selection_CheckboxSelect_Sendkeys("设备类别",["平板","手机"])
        formPage.Textarea_Sendkeys("备注","很大很大空间等哈看进度哈大噶还记得噶还记得噶实践活动")
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()   #点击流程办理弹框确认按钮
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第一个人工任务办理失败")
        time.sleep(5)
        #进行第二个人工任务处理
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
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

    def test_02( self ):
        '''资产管理应用维修流程'''
        portalPage = PortalPage(self.driver)
        #打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.click_process_icon("维修")
        formPage = FormPage(self.driver)
        formPage.MultiForm_BatchManagementButton_Click("维修明细")
        formPage.MultiForm_BathManagePage_Record_Tick("维修明细", [1, 2])
        formPage.MultiForm_BathManagePage_ConfirmButton_Tick("维修明细")
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第一个人工任务办理失败")
        time.sleep(5)
        #进行第二个人工任务处理
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        formPage.Form_Button_Click("接收设备")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第二个人工任务办理失败")
        time.sleep(2)
        #检查第二个人工任务提交后系统任务执行是否成功
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '资产管理')
        businessPage = BusinessPage(self.driver)
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1, 7), "维修中", msg="第二个人工任务提交后系统任务执行失败")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(2, 7), "维修中", msg="第二个人工任务提交后系统任务执行失败")
        #进行第4个人工任务处理
        businessPage.BusinessPage_HeardItem_AllApp_Click() #点击全部应用菜单
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        formPage.Form_Button_Click("维修完成")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第4个人工任务办理失败")
        time.sleep(2)
        #检查第4个人工任务提交后系统任务执行是否成功
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '资产管理')

        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1, 7), "已借出", msg="第二个人工任务提交后系统任务执行失败")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(2, 7), "已借出", msg="第二个人工任务提交后系统任务执行失败")
        time.sleep(10)
        print("检查完成，资产管理维修流程测试通过")



    def test_03( self ):
        '''资产管理应用更换流程'''
        portalPage = PortalPage(self.driver)
        #打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.click_process_icon("更换")
        formPage = FormPage(self.driver)
        formPage.MultiForm_BatchManagementButton_Click("归还已领设备")
        formPage.MultiForm_BathManagePage_Record_Tick("归还已领设备", [1, 2])
        formPage.MultiForm_BathManagePage_ConfirmButton_Tick("归还已领设备")
        formPage.Selection_CheckboxSelect_Sendkeys("更换设备类型", ["显示器", "笔记本电脑"])
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第一个人工任务办理失败")
        time.sleep(5)
        #进行第二个人工任务处理
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        formPage.MultiForm_BatchManagementButton_Click("新设备明细")
        formPage.MultiForm_BathManagePage_Record_Tick("新设备明细", [2, 4])
        formPage.MultiForm_BathManagePage_ConfirmButton_Tick("新设备明细")
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第二个人工任务办理失败")
        time.sleep(2)
        #检查第二个人工任务提交后系统任务执行是否成功
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '资产管理')
        businessPage = BusinessPage(self.driver)
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1, 7), "可借出", msg="第二个人工任务提交后系统任务执行失败")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(2, 7), "可借出", msg="第二个人工任务提交后系统任务执行失败")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(4, 7), "已借出", msg="第二个人工任务提交后系统任务执行失败")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(6, 7), "已借出", msg="第二个人工任务提交后系统任务执行失败")
        time.sleep(10)
        print("检查完成，资产管理更换流程测试通过")

    def test_04( self ):
        '''资产管理应用归还流程'''
        portalPage = PortalPage(self.driver)
        #打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.click_process_icon("归还")
        formPage = FormPage(self.driver)
        formPage.MultiForm_BatchManagementButton_Click("归还明细")
        formPage.MultiForm_BathManagePage_Record_Tick("归还明细", [1, 2])
        formPage.MultiForm_BathManagePage_ConfirmButton_Tick("归还明细")
        time.sleep(3)
        self.assertEqual("笔记本",formPage.MultiForm_GetTdValue("归还明细", 1, 2),msg="归还明细设备类别显示不正确")
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第一个人工任务办理失败")
        time.sleep(5)
        #进行第二个人工任务处理
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第二个人工任务办理失败")
        time.sleep(2)
        #检查第二个人工任务提交后系统任务执行是否成功
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '资产管理')
        businessPage = BusinessPage(self.driver)
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(4, 7), "可借出", msg="第二个人工任务提交后系统任务执行失败")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(6, 7), "可借出", msg="第二个人工任务提交后系统任务执行失败")
        time.sleep(10)
        print("检查完成，资产管理归还流程测试通过")


    def test_05( self ):
        '''资产管理应用报废流程'''
        portalPage = PortalPage(self.driver)
        #打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.click_process_icon("报废")
        formPage = FormPage(self.driver)
        formPage.MultiForm_BatchManagementButton_Click("报废明细")
        formPage.MultiForm_BathManagePage_Record_Tick("报废明细", [1, 2])
        formPage.MultiForm_BathManagePage_ConfirmButton_Tick("报废明细")
        self.assertEqual("D180734", formPage.MultiForm_GetTdValue("报废明细", 1, 2), msg="报废明细序列号显示不正确")
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第一个人工任务办理失败")
        time.sleep(5)
        #进行第二个人工任务处理
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第二个人工任务办理失败")
        time.sleep(2)
        #检查第二个人工任务提交后系统任务执行是否成功
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '资产管理')
        businessPage = BusinessPage(self.driver)
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(4, 7), "已报废", msg="第二个人工任务提交后系统任务执行失败")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(6, 7), "已报废", msg="第二个人工任务提交后系统任务执行失败")
        time.sleep(10)
        print("检查完成，资产管理报废流程测试通过")