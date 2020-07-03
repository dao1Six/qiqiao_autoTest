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
from qiqiao_page.pc_page.portal_page import PortalPage
from qiqiao_page.pc_page.process_page import ProcessPage
from util.dateTimeUtil import DateTimeUtil
from util.parseExcel import ParseExcel


class PomAppTest_001(unittest.TestCase):
    '''生产运营应用流程操作'''







    def setUp(self):
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        time.sleep(5)






    def tearDown(self) -> None:
        self.driver.quit()

    def test_01( self ):
        '''道一云生产运营应用，事业一部订单发起 流程'''
        #第一个人工任务
        portalPage = PortalPage(self.driver)
        #打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.click_process_icon("事业一部订单发起")
        formPage = FormPage(self.driver)
        orderName ="长江水坝管理系统"
        formPage.Text_Sendkeys("订单名称",orderName)
        formPage.Selection_MonomialSelect_Sendkeys("产品/服务类型","代理产品")
        formPage.Selection_MonomialSelect_Sendkeys("付费类型", "订阅")
        formPage.Selection_MonomialSelect_Sendkeys("软硬件类型", "软件")

        formPage.Textarea_Sendkeys("订单描述","dasdsadasdsadddasdsadsadsadsadasdsadasdas")
        formPage.Number_Sendkeys("订单金额",25555554444)
        formPage.Selection_MonomialSelect_Sendkeys("战略意义", "标杆作用")
        formPage.Text_Sendkeys("客户名称", "长江水坝管理局")
        formPage.Text_Sendkeys("客户类型", "政府")
        formPage.Text_Sendkeys("合同名称", "大大实打实的的")
        formPage.Text_Sendkeys("合同编号", "大大实打实的的")
        formPage.Number_Sendkeys("合同金额", 25555554444)
        formPage.Date_Sendkeys("合同签订时间", DateTimeUtil().Yesterday())
        formPage.Date_Sendkeys("合同开始时间", DateTimeUtil().Today())
        formPage.Date_Sendkeys("合同结束时间", DateTimeUtil().Tomorrow())
        #点击开票回款计划添加按钮字段
        formPage.ChildForm_AddButton_Click("开票回款计划")
        formPage.Text_InChildForm_Sendkeys("开票回款计划", "款项", "合同款")
        formPage.Number_InChildForm_Sendkeys("开票回款计划", "计划开票金额",233333)
        formPage.Date_InChildForm_Sendkeys("开票回款计划","计划开票时间",DateTimeUtil().Today())
        formPage.click_ChildForm_Button("保存并继续添加")
        formPage.Text_InChildForm_Sendkeys("开票回款计划", "款项", "进度款")
        formPage.Number_InChildForm_Sendkeys("开票回款计划", "计划开票金额",221113333)
        formPage.Date_InChildForm_Sendkeys("开票回款计划","计划开票时间",DateTimeUtil().Tomorrow())
        formPage.click_ChildForm_Button("保存")
        time.sleep(2)
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第1个人工任务办理失败")
        #处理第二个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        #选择实施人员
        formPage.User_MonomialUser_Sendkeys("实施负责人","吴健伦")
        formPage.Form_Button_Click("审批通过")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第2个人工任务办理失败")
        #处理第三个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        formPage.Form_Button_Click("审批通过")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第3个人工任务办理失败")
        #处理第四个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        formPage.Form_Button_Click("审批通过")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第4个人工任务办理失败")
        #处理第五个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        formPage.Form_Button_Click("确认")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第5个人工任务办理失败")
        #处理第六个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        formPage.Form_Button_Click("确认")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第6个人工任务办理失败")
        #检查流程产生的数据信息
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '生产运管系统')
        businessPage = BusinessPage(self.driver)
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1, 8), orderName, msg="订单名称信息错误")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1, 9), "进行中", msg="订单状态信息错误")



    def test_02( self ):
        '''道一云生产运营应用，事业一部内部订单发起 流程'''
        #第一个人工任务
        portalPage = PortalPage(self.driver)
        #打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.click_process_icon("事业一部内部订单发起")
        formPage = FormPage(self.driver)
        orderName ="长江水坝管理系统内部订单"
        formPage.Text_Sendkeys("订单名称",orderName)
        formPage.Selection_MonomialSelect_Sendkeys("订单来源","外部订单")
        formPage.ForeignSelection_Sendkeys("对应订单名称","长江水坝管理系统")
        time.sleep(2)
        self.assertNotEqual(formPage.Text_GetValue_writable("对应订单编号"),"",msg="对应订单编号没有连带写入")

        formPage.Dept_MonomialDept_Sendkeys("结算收入一级部门","创新技术中心")
        formPage.Dept_MonomialDept_Sendkeys("结算收入二级部门", "产品研发二部",index=1)
        formPage.Selection_MonomialSelect_Sendkeys("订单类型", "项目转包")

        formPage.Textarea_Sendkeys("订单说明","dasdsadasdsadddasdsadsadsadsadasdsadasdas")
        formPage.Number_Sendkeys("订单预估金额",25555554444)
        formPage.Date_Sendkeys("项目开始时间", DateTimeUtil().Today())
        formPage.Date_Sendkeys("项目结束时间", DateTimeUtil().Tomorrow())

        #点击资源借调信息添加按钮字段
        formPage.ChildForm_AddButton_Click("资源借调信息")
        formPage.User_MonomialUser_InChildForm_Sendkeys("资源借调信息", "借调人", "吴健伦")
        formPage.Date_InChildForm_Sendkeys("资源借调信息","借调开始时间",DateTimeUtil().Today())
        formPage.Date_InChildForm_Sendkeys("资源借调信息", "借调预计结束时间", DateTimeUtil().Tomorrow())
        formPage.Number_InChildForm_Sendkeys("资源借调信息", "预计借调天数", 2)
        formPage.Number_InChildForm_Sendkeys("资源借调信息", "其他费用", 300)
        formPage.click_ChildForm_Button("保存并继续添加")
        formPage.User_MonomialUser_InChildForm_Sendkeys("资源借调信息", "借调人", "王浩")
        formPage.Date_InChildForm_Sendkeys("资源借调信息", "借调开始时间", DateTimeUtil().Today())
        formPage.Date_InChildForm_Sendkeys("资源借调信息", "借调预计结束时间", DateTimeUtil().Tomorrow())
        formPage.Number_InChildForm_Sendkeys("资源借调信息", "预计借调天数", 2)
        formPage.Number_InChildForm_Sendkeys("资源借调信息", "其他费用", 300)
        formPage.click_ChildForm_Button("保存")
        time.sleep(2)
        self.assertEqual(formPage.ChildForm_GetTdValue("资源借调信息",1,3),"测试",msg="借调人连带职位错误")
        self.assertEqual(formPage.ChildForm_GetTdValue("资源借调信息", 2, 4), "100.00", msg="借调人连带预估单价错误")
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第1个人工任务办理失败")
        #处理第二个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        formPage.Form_Button_Click("审批通过")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第2个人工任务办理失败")

        #处理第三个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        formPage.Form_Button_Click("审批通过")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第3个人工任务办理失败")
        #处理第四个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        formPage.Form_Button_Click("审批通过")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第4个人工任务办理失败")
        #处理第五个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        formPage.Form_Button_Click("审批通过")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第5个人工任务办理失败")
        #检查流程产生的数据信息
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '生产运管系统')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('内部订单管理')
        businessPage.BusinessPage_LeftMenu_Click('内部订单管理2')
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1, 5), "进行中", msg="订单状态信息错误")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1, 5), "未结算", msg="订单状态信息错误")


    def test_03( self ):
        '''道一云生产运营应用，事业一部结算流程'''
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '生产运管系统')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('内部订单管理')
        businessPage.BusinessPage_LeftMenu_Click('内部订单管理2')
        businessPage.ListComponent_Click_ListRow_Button("添加发起结算",1)
        formPage = FormPage(self.driver)
        jiediaoren1 = formPage.ChildForm_GetTdValue("资源借调信息",1,2)
        jiediaoren2 = formPage.ChildForm_GetTdValue("资源借调信息", 2, 2)
        #点击资源借调结算管理添加按钮字段
        formPage.ChildForm_AddButton_Click("资源借调结算管理")
        formPage.ForeignSelection_InChildForm_Sendkeys("资源借调结算管理","借调编号",jiediaoren1)
        formPage.Date_InChildForm_Sendkeys("资源借调结算管理", "工作量开始时间", DateTimeUtil().Today())
        formPage.Date_InChildForm_Sendkeys("资源借调结算管理", "工作量开始时间", DateTimeUtil().Tomorrow())
        formPage.Number_InChildForm_Sendkeys("资源借调结算管理", "工作量天数", 2)
        formPage.click_ChildForm_Button("保存并继续添加")
        formPage.ChildForm_AddButton_Click("资源借调结算管理")
        formPage.ForeignSelection_InChildForm_Sendkeys("资源借调结算管理","借调编号",jiediaoren2)
        formPage.Date_InChildForm_Sendkeys("资源借调结算管理", "工作量开始时间", DateTimeUtil().Today())
        formPage.Date_InChildForm_Sendkeys("资源借调结算管理", "工作量开始时间", DateTimeUtil().Tomorrow())
        formPage.Number_InChildForm_Sendkeys("资源借调结算管理", "工作量天数", 2)
        formPage.click_ChildForm_Button("保存")
        time.sleep(2)
        self.assertEqual(formPage.ChildForm_GetTdValue("资源借调结算管理", 1, 9), "600", msg="结算费用汇总计算错误")
        self.assertEqual(formPage.ChildForm_GetTdValue("资源借调结算管理", 2, 9), "500", msg="结算费用汇总计算错误")
        # 点击其他类型结算管理添加按钮字段
        formPage.ChildForm_AddButton_Click("其他类型结算管理")
        formPage.Number_InChildForm_Sendkeys("其他类型结算管理", "结算金额", 600)
        formPage.click_ChildForm_Button("保存")
        time.sleep(2)








    def test_04( self ):
        '''道一云生产运营应用，立项申请流程(事业二部)流程'''

        portalPage = PortalPage(self.driver)
        self.assertEquals(portalPage.PortalPage_GetLoginUserName(),'王浩')
        #打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.click_process_icon("立项申请流程(事业二部)")

        formPage = FormPage(self.driver)
        formPage.Text_Sendkeys("项目名称","中科信息立项申请")
        formPage.Textarea_Sendkeys("项目简介","中科信息立项申请哈哈哈哈哈哈哈")
        #
        formPage.Dept_MonomialDept_Sendkeys("所属一级部门","企微")
        formPage.Dept_MonomialDept_Sendkeys("所属二级部门", "企微")
        self.assertEquals(formPage.User_GetMonomialUserValue_readOnly("项目经理"),"王浩")

        #点击管理订单添加按钮字段
        formPage.ChildForm_AddButton_Click("关联订单")
        formPage.ForeignSelection_InChildForm_Sendkeys("关联订单","关联订单","电信")
        time.sleep(2)
        formPage.Selection_MonomialSelect_InChildForm_Sendkeys("关联订单","战略意义","标杆作用")
        formPage.Number_Sendkeys("预估成本（人天）",10)
        #点击子表保存按钮
        formPage.click_ChildForm_Button('保存')

        print(formPage.Number_GetValue_readOnly("项目总金额"))
        print(formPage.Number_GetValue_readOnly("项目预估总成本（人天）"))
        print(formPage.Date_GetValue_writable("项目启动时间"))
        print(formPage.Selection_GetSelectionBoxValue_writable("项目类型"))
        time.sleep(1)
        formPage.Selection_MonomialSelect_Sendkeys('项目等级','普通（普）')
        formPage.Date_Sendkeys("预计验收时间","2020-06-22")
        formPage.Text_Sendkeys("客户名称", "李嘉诚")
        formPage.Text_Sendkeys("甲方对接人", "李嘉诚")
        formPage.Text_Sendkeys("联系方式", "13025805485")
        formPage.Textarea_Sendkeys("备注信息", "中科信息立项申请哈哈哈哈哈哈哈")

        # 点击项目里程碑添加按钮字段
        formPage.ChildForm_AddButton_Click("项目里程碑")
        formPage.Text_InChildForm_Sendkeys("项目里程碑","阶段名称", "测试")
        formPage.Date_InChildForm_Sendkeys("项目里程碑","计划完成时间", "2020-06-22")
        time.sleep(2)
        # 点击子表保存按钮
        formPage.click_ChildForm_Button('保存')
        formPage.Form_Button_Click("提交")
        formPage.selectProcessManager(["王浩"])
        time.sleep(5)
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        formPage.Form_Button_Click("审核通过")























