# coding=utf-8
import os
import time
import unittest
from functools import wraps

from public.HTMLTestRunner_cn import _TestResult
from public.driver import Driver
from qiqiao_page.mobile_page.mb_form_page import MbFormPage
from qiqiao_page.mobile_page.mobile_home_page import MbHomePage
from qiqiao_page.mobile_page.mobile_login_page import MbLoginPage
from qiqiao_page.mobile_page.mobile_to_do_page import MbTodoPage
from qiqiao_page.pc_page.applicationList_page import ApplicationListPage
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.form_page import FormPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.portal_page import PortalPage
from qiqiao_page.pc_page.process_page import ProcessPage
from util.dateTimeUtil import DateTimeUtil
from util.parseExcel import ParseExcel


class MbPomAppTest_001(unittest.TestCase):
    '''移动端生产运营应用流程操作'''

    @classmethod
    def setUpClass(self):
        '''清理数据'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        time.sleep(10)
        # 打开生产运营管理应用
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '生产运管系统')
        businessPage = BusinessPage(self.driver)
        # 清除订单管理相关数据
        # 判断列表是否存在数据
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除（临时）')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        # 清除内部订单管理相关数据
        # 判断列表是否存在数据
        businessPage.BusinessPage_LeftMenu_Click('内部订单管理')
        businessPage.BusinessPage_LeftMenu_Click('内部订单管理2')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除（临时）')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        # 清除资源借调信息相关数据
        businessPage.BusinessPage_LeftMenu_Click('资源借调信息')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        # 清除借调结算管理相关数据
        businessPage.BusinessPage_LeftMenu_Click('借调结算管理')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除（临时）')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        # 清除其他结算管理相关数据
        businessPage.BusinessPage_LeftMenu_Click('其他结算管理')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除（临时）')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
            # 清除项目信息管理相关数据
            businessPage.BusinessPage_LeftMenu_Click('项目信息管理')
            businessPage.BusinessPage_LeftMenu_Click('里程碑信息')
            if (businessPage.ListComponent_GetRecordTotal() >0):
                businessPage.ListComponent_SelectAllRecord()
                businessPage.ListComponent_Click_ListHeader_Button('删除')
                businessPage.ListComponent_TooltipButton_Click('确定')
                assert '成功' in businessPage.Public_GetAlertMessage()
            time.sleep(2)
            businessPage.BusinessPage_LeftMenu_Click('项目信息管理2')
            if (businessPage.ListComponent_GetRecordTotal() >= 3):
                businessPage.ListComponent_checkbox_Click(1)
                businessPage.ListComponent_Click_ListHeader_Button('删除（临时）')
                businessPage.ListComponent_TooltipButton_Click('确定')
                assert '成功' in businessPage.Public_GetAlertMessage()
            time.sleep(2)
            portalPage.PortalPage_qiqiao_logout()
            self.driver.quit()





    def setUp(self):
        '''登录'''
        self.mbLogin("wanghao@auto","do1qiqiao")

    def mbLogin(self,account,password):
        '''登录移动端'''
        self.driver = Driver().phonedriver()
        self.driver.maximize_window()
        loginpage = MbLoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/mruntime', account, password)
        time.sleep(5)

    def pcLogin(self,account,password):
        '''登录pc端'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', account, password)
        time.sleep(5)




    def test_01( self ):
        '''移动端道一云生产运营应用，事业一部订单发起 流程'''
        homePage = MbHomePage(self.driver)
        homePage.HomePage_BottomNav_Click("待办")
        # 发起流程
        todoPage = MbTodoPage(self.driver)
        todoPage.MbTodoPage_Faqiliucheng('生产运管系统','事业一部订单发起')
        formPage = MbFormPage(self.driver)
        #第一个人工任务
        orderName ="长江水坝管理系统"
        formPage.MbText_Sendkeys("订单名称",orderName)
        formPage.MbSelection_Xiala_Senkeys("产品/服务类型","代理产品")
        formPage.MbSelection_Xiala_Senkeys("付费类型", "订阅")
        formPage.MbSelection_Xiala_Senkeys("软硬件类型", "软件")

        formPage.MbTextarea_Sendkeys("订单描述","dasdsadasdsadddasdsadsadsadsadasdsadasdas")
        formPage.MbNumber_Sendkeys("订单金额",25555554444)
        formPage.MbSelection_Xiala_Senkeys("战略意义", "标杆作用")

        formPage.MbText_Sendkeys("客户名称", "长江水坝管理局")
        formPage.MbText_Sendkeys("客户类型", "政府")
        formPage.MbText_Sendkeys("合同名称", "大大实打实的的")
        formPage.MbText_Sendkeys("合同编号", "大大实打实的的")
        formPage.MbNumber_Sendkeys("合同金额", 25555554444)
        formPage.MbDate_SendKeys("合同签订时间", DateTimeUtil().Yesterday())
        formPage.MbDate_SendKeys("合同开始时间", DateTimeUtil().Today())
        formPage.MbDate_SendKeys("合同结束时间", DateTimeUtil().Tomorrow())
        #点击开票回款计划添加按钮字段
        formPage.MbChildForm_AddButton_Click("开票回款计划")
        formPage.MbText_Sendkeys("款项", "合同款")
        formPage.MbNumber_Sendkeys("计划开票金额",233333)
        formPage.MbDate_SendKeys("计划开票时间",DateTimeUtil().Today())
        formPage.MbChildForm_Button_Click("保存并继续添加")
        time.sleep(2)
        formPage.MbText_Sendkeys( "款项", "进度款")
        formPage.MbNumber_Sendkeys("计划开票金额",221113333)
        formPage.MbDate_SendKeys("计划开票时间",DateTimeUtil().Tomorrow())
        formPage.MbChildForm_Button_Click("保存")
        time.sleep(2)
        formPage.MbForm_Button_Click("提交")
        formPage.MbForm_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第1个人工任务办理失败")
        #处理第二个人工任务
        time.sleep(3)
        self.driver.back()
        todoPage.MbTodoPage_ProcessRecord_Click(1)
        #选择实施人员
        formPage.MbUser_MonomialUser_Sendkeys("实施负责人","王浩")
        formPage.MbForm_Button_Click("审批通过")
        formPage.MbForm_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第2个人工任务办理失败")
        #处理第三个人工任务
        time.sleep(3)
        todoPage.MbTodoPage_ProcessRecord_Click(1)
        formPage.MbForm_Button_Click("审批通过")
        formPage.MbForm_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第3个人工任务办理失败")
        #处理第四个人工任务
        time.sleep(3)
        todoPage.MbTodoPage_ProcessRecord_Click(1)
        formPage.MbForm_Button_Click("审批通过")
        formPage.MbForm_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第4个人工任务办理失败")
        #处理第五个人工任务
        time.sleep(3)
        todoPage.MbTodoPage_ProcessRecord_Click(1)
        formPage.MbForm_Button_Click("确认")
        formPage.MbForm_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第5个人工任务办理失败")
        #处理第六个人工任务
        time.sleep(3)
        todoPage.MbTodoPage_ProcessRecord_Click(1)
        formPage.MbForm_Button_Click("确认")
        formPage.MbForm_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第6个人工任务办理失败")
        time.sleep(3)
        self.driver.quit()
        #检查流程产生的数据信息
        self.pcLogin("wanghao@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '生产运管系统')
        businessPage = BusinessPage(self.driver)
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1, 8), orderName, msg="订单名称信息错误")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1, 9), "进行中", msg="订单状态信息错误")



    def test_02( self ):
        '''移动端道一云生产运营应用，事业一部内部订单发起 流程'''
        homePage = MbHomePage(self.driver)
        homePage.HomePage_BottomNav_Click("待办")
        # 发起流程
        todoPage = MbTodoPage(self.driver)
        todoPage.MbTodoPage_Faqiliucheng('生产运管系统','事业一部内部订单发起')
        formPage = MbFormPage(self.driver)

        orderName ="长江水坝管理系统内部订单"
        formPage.MbText_Sendkeys("订单名称",orderName)
        time.sleep(2)
        formPage.MbSelection_Xiala_Senkeys("订单来源","外部订单")
        time.sleep(3)
        formPage.MbForeignSelection_Sendkeys("对应订单名称","长江水坝管理系统")
        time.sleep(2)
        formPage.MbDept_MonomialDept_Sendkeys("结算收入一级部门","创新技术中心")
        formPage.MbDept_MonomialDept_Sendkeys("结算收入二级部门", "产品研发二部",index=1)
        formPage.MbSelection_Xiala_Senkeys("订单类型", "项目转包")
        formPage.MbTextarea_Sendkeys("订单说明","dasdsadasdsadddasdsadsadsadsadasdsadasdas")
        formPage.MbNumber_Sendkeys("订单预估金额",25555554444)
        formPage.MbDate_SendKeys("项目开始时间", DateTimeUtil().Today())
        formPage.MbDate_SendKeys("项目结束时间", DateTimeUtil().Tomorrow())

        #点击资源借调信息添加按钮字段
        formPage.MbChildForm_AddButton_Click("资源借调信息")
        formPage.MbUser_MonomialUser_Sendkeys("借调人", "吴健伦")
        formPage.MbDate_SendKeys("借调开始时间",DateTimeUtil().Today())
        formPage.MbDate_SendKeys("借调预计结束时间", DateTimeUtil().Tomorrow())
        formPage.MbNumber_Sendkeys("预计借调天数", 2)
        formPage.MbNumber_Sendkeys("其他费用", 300)
        formPage.MbChildForm_Button_Click("保存并继续添加")
        time.sleep(3)
        formPage.MbUser_MonomialUser_Sendkeys("借调人", "王浩")
        formPage.MbDate_SendKeys("借调开始时间", DateTimeUtil().Today())
        formPage.MbDate_SendKeys("借调预计结束时间", DateTimeUtil().Tomorrow())
        formPage.MbNumber_Sendkeys("预计借调天数", 2)
        formPage.MbNumber_Sendkeys("其他费用", 300)
        formPage.MbChildForm_Button_Click("保存")
        time.sleep(2)
        self.assertEqual(formPage.MbChildForm_GetTdValue("资源借调信息",1,3),"销售",msg="借调人连带职位错误")
        self.assertEqual(formPage.MbChildForm_GetTdValue("资源借调信息", 2, 4), "150", msg="借调人连带预估单价错误")
        formPage.MbForm_Button_Click("提交")
        formPage.MbForm_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第1个人工任务办理失败")
        #处理第二个人工任务
        time.sleep(3)
        self.driver.back()
        todoPage.MbTodoPage_ProcessRecord_Click(1)
        formPage.MbForm_Button_Click("审批通过")
        formPage.MbForm_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第2个人工任务办理失败")
        #处理第三个人工任务
        time.sleep(3)
        todoPage.MbTodoPage_ProcessRecord_Click(1)
        formPage.MbForm_Button_Click("审批通过")
        formPage.MbForm_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第3个人工任务办理失败")
        #处理第四个人工任务
        time.sleep(3)
        todoPage.MbTodoPage_ProcessRecord_Click(1)
        formPage.MbForm_Button_Click("审批通过")
        formPage.MbForm_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第4个人工任务办理失败")
        #处理第五个人工任务
        time.sleep(3)
        todoPage.MbTodoPage_ProcessRecord_Click(1)
        formPage.MbForm_Button_Click("审批通过")
        formPage.MbForm_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第5个人工任务办理失败")
        time.sleep(3)
        self.driver.quit()
        # 检查流程产生的数据信息
        self.pcLogin("wanghao@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','生产运管系统')
        businessPage = BusinessPage(self.driver)
        time.sleep(2)
        businessPage.BusinessPage_LeftMenu_Click('内部订单管理')
        businessPage.BusinessPage_LeftMenu_Click('内部订单管理2')
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1, 5), "进行中", msg="订单状态信息错误")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1, 6), "未结算", msg="订单状态信息错误")
    #




























