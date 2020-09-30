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
    '''PC生产运营应用流程操作'''



    def dataPrepare( self ):
        '''数据准备'''
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
        businessPage.BusinessPage_LeftMenu_Click('项目成员信息')
        if (businessPage.ListComponent_GetRecordTotal() >0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        time.sleep(2)
        businessPage.BusinessPage_LeftMenu_Click('固定范围项目进度')
        if (businessPage.ListComponent_GetRecordTotal() >0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        time.sleep(2)
        # portalPage.PortalPage_qiqiao_logout()
        self.driver.quit()

    @classmethod
    def setUpClass(self):
        self.dataPrepare(self)


    def setUp(self):
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wanghao@auto", "do1qiqiao")
        time.sleep(5)



    # def tearDown(self):
    #     self.driver.quit()

    def test_01( self ):
        '''道一云生产运营应用，事业一部订单发起 流程'''
        #第一个人工任务
        portalPage = PortalPage(self.driver)
        #打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("事业一部订单发起")
        formPage = FormPage(self.driver)
        orderName ="长江水坝管理系统"
        formPage.Text_Sendkeys("订单名称",orderName)
        formPage.Selection_SingleXiala_Sendkeys("产品/服务类型","代理产品")
        formPage.Selection_SingleXiala_Sendkeys("付费类型", "订阅")
        formPage.Selection_SingleXiala_Sendkeys("软硬件类型", "软件")

        formPage.Textarea_Sendkeys("订单描述","dasdsadasdsadddasdsadsadsadsadasdsadasdas")
        formPage.Number_Sendkeys("订单金额",25555554444)
        formPage.Selection_SingleXiala_Sendkeys("战略意义", "标杆作用")
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
        formPage.Text_InPopup_Sendkeys("开票回款计划", "款项", "合同款")
        formPage.Number_InPopup_Sendkeys("开票回款计划", "计划开票金额",233333)
        formPage.Date_Sendkeys_InPop("开票回款计划","计划开票时间",DateTimeUtil().Today())
        formPage.click_ChildForm_Button("保存并继续添加")
        formPage.Text_InPopup_Sendkeys("开票回款计划", "款项", "进度款")
        formPage.Number_InPopup_Sendkeys("开票回款计划", "计划开票金额",221113333)
        formPage.Date_Sendkeys_InPop("开票回款计划","计划开票时间",DateTimeUtil().Tomorrow())
        formPage.click_ChildForm_Button("保存")
        time.sleep(2)
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第1个人工任务办理失败")
        #处理第二个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        self.assertEqual(processPage.ProcessPage_get_processTdValue(1,2),"王浩的_"+orderName+"_订单发起审批流程"+DateTimeUtil().Today().replace('-',''),msg="流程标题显示错误")
        self.assertEqual(processPage.ProcessPage_get_processTdValue(1,5),"业务部总监审批",msg="流程当前任务名称显示错误")
        processPage.ProcessPage_click_process_record(1)
        #选择实施人员
        formPage.User_MonomialUser_Sendkeys("实施负责人","王浩")
        formPage.Form_Button_Click("审批通过")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第2个人工任务办理失败")
        #处理第三个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("审批通过")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第3个人工任务办理失败")
        #处理第四个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("审批通过")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第4个人工任务办理失败")
        #处理第五个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("确认")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第5个人工任务办理失败")
        #处理第六个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
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
        businessPage.BusinessPage_LeftMenu_Click('开票回款计划')
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1, 10), "233333", msg="开票回款计划信息错误")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(2, 10), "221113333", msg="开票回款计划信息错误")
        businessPage.BusinessPage_LeftMenu_Click('订单管理2')
        businessPage.ListComponent_Click_ListRow_Button("详情",1)
        time.sleep(2)
        self.assertEqual(formPage.ChildForm_GetTdValue("开票回款计划",1,4),"233333",msg="开票回款计划信息错误")
        self.assertEqual(formPage.ChildForm_GetTdValue("开票回款计划",2,4),"221113333",msg="开票回款计划信息错误")




    def test_02( self ):
        '''道一云生产运营应用，事业一部内部订单发起 流程'''
        #第一个人工任务
        portalPage = PortalPage(self.driver)
        #打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("事业一部内部订单发起")
        formPage = FormPage(self.driver)
        orderName ="长江水坝管理系统内部订单"
        formPage.Text_Sendkeys("订单名称",orderName)
        time.sleep(2)
        formPage.Selection_SingleXiala_Sendkeys("订单来源","外部订单")
        time.sleep(3)
        formPage.ForeignSelection_Sendkeys("对应订单名称","长江水坝管理系统")
        time.sleep(5)
        self.assertNotEqual(formPage.Text_GetValue_writable("对应订单编号"),"",msg="对应订单编号没有连带写入")

        formPage.Dept_MonomialDept_Sendkeys("结算收入一级部门","创新技术中心")
        formPage.Dept_MonomialDept_Sendkeys("结算收入二级部门", "产品研发二部",index=1)
        formPage.Selection_SingleXiala_Sendkeys("订单类型", "项目转包")

        formPage.Textarea_Sendkeys("订单说明","dasdsadasdsadddasdsadsadsadsadasdsadasdas")
        formPage.Number_Sendkeys("订单预估金额",25555554444)
        formPage.Date_Sendkeys("项目开始时间", DateTimeUtil().Today())
        formPage.Date_Sendkeys("项目结束时间", DateTimeUtil().Tomorrow())

        #点击资源借调信息添加按钮字段
        formPage.ChildForm_AddButton_Click("资源借调信息")
        formPage.User_MonomialUser_InChildForm_Sendkeys("资源借调信息", "借调人", "吴健伦")
        time.sleep(3)
        formPage.Date_Sendkeys_InPop("资源借调信息","借调开始时间",DateTimeUtil().Today())
        formPage.Date_Sendkeys_InPop("资源借调信息", "借调预计结束时间", DateTimeUtil().Tomorrow())
        formPage.Number_InPopup_Sendkeys("资源借调信息", "预计借调天数", 2)
        formPage.Number_InPopup_Sendkeys("资源借调信息", "其他费用", 300)
        formPage.click_ChildForm_Button("保存并继续添加")
        formPage.User_MonomialUser_InChildForm_Sendkeys("资源借调信息", "借调人", "王浩")
        time.sleep(3)
        formPage.Date_Sendkeys_InPop("资源借调信息", "借调开始时间", DateTimeUtil().Today())
        formPage.Date_Sendkeys_InPop("资源借调信息", "借调预计结束时间", DateTimeUtil().Tomorrow())
        formPage.Number_InPopup_Sendkeys("资源借调信息", "预计借调天数", 2)
        formPage.Number_InPopup_Sendkeys("资源借调信息", "其他费用", 300)
        formPage.click_ChildForm_Button("保存")
        time.sleep(2)
        self.assertEqual(formPage.ChildForm_GetTdValue("资源借调信息",1,3),"测试",msg="借调人连带职位错误")
        self.assertEqual(formPage.ChildForm_GetTdValue("资源借调信息", 2, 4), "100.00", msg="借调人连带预估单价错误")
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第1个人工任务办理失败")
        #处理第二个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("审批通过")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第2个人工任务办理失败")

        #处理第三个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("审批通过")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第3个人工任务办理失败")
        #处理第四个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("审批通过")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第4个人工任务办理失败")
        #处理第五个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("审批通过")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第5个人工任务办理失败")
        #检查流程产生的数据信息
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '生产运管系统')
        time.sleep(2)
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('内部订单管理')
        businessPage.BusinessPage_LeftMenu_Click('内部订单管理2')
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1, 5), "进行中", msg="订单状态信息错误")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1, 6), "未结算", msg="订单状态信息错误")
        # businessPage.ListComponent_Click_ListRow_Button("详情",1)


    def test_03( self ):
        '''道一云生产运营应用，事业一部结算流程'''
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '生产运管系统')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('内部订单管理')
        time.sleep(2)
        businessPage.BusinessPage_LeftMenu_Click('内部订单管理2')
        businessPage.ListComponent_Click_ListRow_Button("添加发起结算",1)
        formPage = FormPage(self.driver)
        jiediaoren1 = formPage.ChildForm_GetTdValue("资源借调信息",1,2)
        jiediaoren2 = formPage.ChildForm_GetTdValue("资源借调信息", 2, 2)
        #点击资源借调结算管理添加按钮字段
        formPage.ChildForm_AddButton_Click("资源借调结算管理")
        formPage.ForeignSelection_InPopup_Sendkeys("资源借调结算管理","借调编号",jiediaoren1)
        time.sleep(3)
        formPage.Date_Sendkeys_InPop("资源借调结算管理", "工作量开始时间", DateTimeUtil().Today())
        formPage.Date_Sendkeys_InPop("资源借调结算管理", "工作量结束时间", DateTimeUtil().Tomorrow())
        formPage.Number_InPopup_Sendkeys("资源借调结算管理", "工作量天数", 2)
        time.sleep(2)
        formPage.click_ChildForm_Button("保存")
        time.sleep(2)
        formPage.ChildForm_AddOneRowButton_Click("资源借调结算管理")
        formPage.ChildForm_List_ForeignSelection_sendkeys("资源借调结算管理",2,"借调编号",jiediaoren2)
        time.sleep(2)
        formPage.ChildForm_List_Date_sendkeys("资源借调结算管理","工作量开始时间",2,DateTimeUtil().Today())
        formPage.ChildForm_List_Date_sendkeys("资源借调结算管理","工作量结束时间",2,DateTimeUtil().Tomorrow())
        formPage.ChildForm_List_Number_sendkeys("资源借调结算管理","工作量天数",2,2)
        time.sleep(2)
        self.assertEqual("100.00",formPage.ChildForm_GetTdValue("资源借调结算管理", 2, 4),msg="添加一行外键连带写入失败")
        self.assertEqual("王浩",formPage.ChildForm_GetTdValue("资源借调结算管理",2,3),msg="添加一行外键连带写入失败")
        self.assertEqual(formPage.ChildForm_GetTdValue("资源借调结算管理", 1, 9), "600", msg="结算费用汇总计算错误")
        self.assertEqual(formPage.ChildForm_GetTdValue("资源借调结算管理", 2, 9), "500", msg="结算费用汇总计算错误")
        # 点击其他类型结算管理添加按钮字段
        formPage.ChildForm_AddButton_Click("其他类型结算管理")
        formPage.Number_InPopup_Sendkeys("其他类型结算管理", "结算金额", 600)
        formPage.click_ChildForm_Button("保存")
        time.sleep(3)
        formPage.Form_Button_Click("发起结算")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第1个人工任务办理失败")
        # 处理第二个人工任务
        businessPage.BusinessPage_HeardItem_AllApp_Click()
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第2个人工任务办理失败")
        # 处理第三个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第3个人工任务办理失败")
        # 处理第4个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第4个人工任务办理失败")
        # 处理第5个人工任务
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第5个人工任务办理失败")
        #校验流程处理完后的数据
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '生产运管系统')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('内部订单管理')
        businessPage.BusinessPage_LeftMenu_Click('内部订单管理2')
        businessPage.ListComponent_Click_ListRow_Button("详情",1)
        self.assertEqual(formPage.ChildForm_GetTdValue("其他类型结算管理",1,5),DateTimeUtil().Today(),msg="结算支出部门总经理审核任务办理按钮，其他结算时间触发事件失败")
        self.assertEqual(formPage.ChildForm_GetTdValue("资源借调结算管理", 1,12), DateTimeUtil().Today(),
                         msg="结算支出部门总经理审核任务办理按钮，资源结算时间触发事件失败")
        self.assertEqual(formPage.ChildForm_GetTdValue("资源借调结算管理", 2,12), DateTimeUtil().Today(),
                         msg="结算支出部门总经理审核任务办理按钮，资源结算时间触发事件失败")
        self.assertEqual(formPage.ChildForm_GetTdValue("其他类型结算管理", 1, 4), "已结算",
                         msg="结算支出部门总经理审核任务办理按钮，更新结算明细状态触发事件失败")

        self.assertEqual(formPage.ChildForm_GetTdValue("资源借调结算管理", 1,11), "已结算",
                         msg="结算支出部门总经理审核任务办理按钮，更新借调结算触发事件失败")
        self.assertEqual(formPage.ChildForm_GetTdValue("资源借调结算管理", 2,11), "已结算",
                         msg="结算支出部门总经理审核任务办理按钮，更新借调结算触发事件失败")






    def test_04( self ):
        '''道一云生产运营应用，事业一部立项申请流程'''
        portalPage = PortalPage(self.driver)
        #打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("事业一部立项申请")
        formPage = FormPage(self.driver)
        formPage.Text_Sendkeys("项目名称","中科信息立项申请")
        formPage.Textarea_Sendkeys("项目简介","中科信息立项申请哈哈哈哈哈哈哈")
        #
        self.assertEquals(formPage.User_GetMonomialUserValue_readOnly("项目经理"),"王浩")
        formPage.Selection_SingleXiala_Sendkeys("合作部门","仅通用产品部")
        #点击管理订单添加按钮字段
        formPage.ChildForm_AddButton_Click("关联订单")
        formPage.ForeignSelection_InPopup_Sendkeys("关联订单","关联订单","长江水坝管理系统")
        time.sleep(2)
        formPage.Number_InPopup_Sendkeys("关联订单","预估成本（人天）",10)
        #点击子表保存按钮
        formPage.click_ChildForm_Button('保存')
        time.sleep(3)
        self.assertEqual(formPage.Number_GetValue_readOnly("项目总金额"),"25555554444",msg="项目总金额计算错误")
        self.assertEqual(formPage.Number_GetValue_readOnly("项目预估总成本（人天）"),"10",msg="项目预估总成本（人天）错误")
        self.assertEqual(formPage.Date_GetValue_writable("项目启动时间"),DateTimeUtil().Today(),msg="项目启动时间错误")
        time.sleep(1)
        formPage.Selection_SingleXiala_Sendkeys('项目类型','固定范围')
        formPage.Selection_SingleXiala_Sendkeys('项目等级','普通（普）')
        formPage.Date_Sendkeys("预计验收时间",DateTimeUtil().Tomorrow())
        formPage.Text_Sendkeys("客户名称", "李嘉诚")
        formPage.Text_Sendkeys("甲方对接人", "李嘉诚")
        formPage.Text_Sendkeys("联系方式", "13025805485")
        formPage.Textarea_Sendkeys("备注信息", "中科信息立项申请哈哈哈哈哈哈哈")

        # 点击项目里程碑添加按钮字段
        formPage.ChildForm_AddButton_Click("项目里程碑")
        formPage.Text_InPopup_Sendkeys("项目里程碑","阶段名称", "测试")
        formPage.Date_Sendkeys_InPop("项目里程碑","计划完成时间", DateTimeUtil().Tomorrow())
        formPage.Selection_SingleXiala_InPopup_Sendkeys("项目里程碑","里程碑状态","已完成")
        time.sleep(1)
        formPage.Date_Sendkeys_InPop("项目里程碑","实际完成时间", DateTimeUtil().Tomorrow())

        # 点击子表保存按钮
        formPage.click_ChildForm_Button('保存并继续添加')
        time.sleep(2)
        formPage.Text_InPopup_Sendkeys("项目里程碑","阶段名称", "测试")
        formPage.Date_Sendkeys_InPop("项目里程碑","计划完成时间", DateTimeUtil().Tomorrow())
        formPage.click_ChildForm_Button('保存')
        time.sleep(2)
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="流程发起失败")
        time.sleep(2)
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("审核通过")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第二个人工任务办理失败")
        time.sleep(2)
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第三个人工任务办理失败")
        time.sleep(2)
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第四个人工任务办理失败")
        time.sleep(2)
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第五个人工任务办理失败")





    def test_05( self ):
        '''道一云生产运营应用，事业一部项目转让流程'''
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '生产运管系统')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('项目信息管理')
        businessPage.BusinessPage_LeftMenu_Click('项目信息管理2')
        time.sleep(2)
        businessPage.ListComponent_Click_ListRow_Button("团队管理",1)
        formPage = FormPage(self.driver)
        formPage.ChildForm_AddOneRowButton_Click("项目团队成员")
        formPage.ChildForm_List_User_sendkeys("项目团队成员","员工",1,["吴健伦"])
        formPage.ChildForm_List_Text_sendkeys("项目团队成员",1,"岗位","dasdasdas")
        formPage.ChildForm_List_Select_sendkeys("项目团队成员",1,"参与状态",["参与中"])
        formPage.ChildForm_List_Date_sendkeys("项目团队成员","进入项目时间",1,DateTimeUtil().Today())


        formPage.ChildForm_AddOneRowButton_Click("项目团队成员")
        formPage.ChildForm_List_User_sendkeys("项目团队成员","员工",2,["刘言"])
        formPage.ChildForm_List_Text_sendkeys("项目团队成员",2,"岗位","dasdasdas")
        formPage.ChildForm_List_Select_sendkeys("项目团队成员",2,"参与状态",["已退出"])
        formPage.ChildForm_List_Date_sendkeys("项目团队成员","进入项目时间",2,DateTimeUtil().Yesterday())
        formPage.ChildForm_List_Date_sendkeys("项目团队成员","退出项目时间",2,DateTimeUtil().Tomorrow())

        formPage.ChildForm_AddOneRowButton_Click("项目团队成员")
        formPage.ChildForm_List_User_sendkeys("项目团队成员","员工",3,["李嘉诚"])
        formPage.ChildForm_List_Text_sendkeys("项目团队成员",3,"岗位","dasdasdas")
        formPage.ChildForm_List_Select_sendkeys("项目团队成员",3,"参与状态",["参与中"])
        formPage.ChildForm_List_Date_sendkeys("项目团队成员","进入项目时间",3,DateTimeUtil().Tomorrow())
        time.sleep(2)
        formPage.Form_Button_Click('提交')

        businessPage.ListComponent_Click_ListRow_Button("进度管理",1)
        formPage.ChildForm_AddOneRowButton_Click("项目进度管理")
        formPage.ChildForm_List_Date_sendkeys("项目进度管理","更新日期",1,DateTimeUtil().Today())
        formPage.ChildForm_List_Number_sendkeys("项目进度管理","剩余工作量（人天）",1,20)
        formPage.ChildForm_List_Select_sendkeys("项目进度管理",1,"项目阶段",["测试"])
        formPage.ChildForm_List_Textarea_sendkeys("项目进度管理",1,"项目执行情况简述","dasdasdas")
        formPage.ChildForm_List_Date_sendkeys("项目进度管理","预估实际完成时间",1,DateTimeUtil().Tomorrow())

        formPage.ChildForm_AddOneRowButton_Click("项目进度管理")
        formPage.ChildForm_List_Date_sendkeys("项目进度管理","更新日期",2,DateTimeUtil().Yesterday())
        formPage.ChildForm_List_Number_sendkeys("项目进度管理","剩余工作量（人天）",2,20)
        formPage.ChildForm_List_Select_sendkeys("项目进度管理",2,"项目阶段",["测试"])
        formPage.ChildForm_List_Textarea_sendkeys("项目进度管理",2,"项目执行情况简述","dasdasdas")
        formPage.ChildForm_List_Date_sendkeys("项目进度管理","预估实际完成时间",2,DateTimeUtil().Tomorrow())

        formPage.ChildForm_AddOneRowButton_Click("项目进度管理")
        formPage.ChildForm_List_Date_sendkeys("项目进度管理","更新日期",3,DateTimeUtil().Tomorrow())
        formPage.ChildForm_List_Number_sendkeys("项目进度管理","剩余工作量（人天）",3,20)
        formPage.ChildForm_List_Select_sendkeys("项目进度管理",3,"项目阶段",["测试"])
        formPage.ChildForm_List_Textarea_sendkeys("项目进度管理",3,"项目执行情况简述","dasdasdas")
        formPage.ChildForm_List_Date_sendkeys("项目进度管理","预估实际完成时间",3,DateTimeUtil().Tomorrow())
        formPage.Form_Button_Click('提交')
        time.sleep(2)
        businessPage.ListComponent_MoveTo_ListRow_MoreButton(1)
        businessPage.ListComponent_Click_ListRow_Button("转让",1)
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",1,6),DateTimeUtil().Tomorrow())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",2,6),DateTimeUtil().Today())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",3,6),DateTimeUtil().Yesterday())

        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",1,2),DateTimeUtil().Tomorrow())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",2,2),DateTimeUtil().Today())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",3,2),DateTimeUtil().Yesterday())
        formPage.Form_Button_Click("发起流程")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="流程发起失败")
        businessPage.BusinessPage_HeardItem_AllApp_Click()
        portalPage.PortalPage_Click_HeaderMenu("流程")
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",1,6),DateTimeUtil().Yesterday())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",2,6),DateTimeUtil().Today())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",3,6),DateTimeUtil().Tomorrow())

        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",1,2),DateTimeUtil().Tomorrow())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",2,2),DateTimeUtil().Today())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",3,2),DateTimeUtil().Yesterday())
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第二个人工任务办理失败")
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",1,6),DateTimeUtil().Yesterday())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",2,6),DateTimeUtil().Today())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",3,6),DateTimeUtil().Tomorrow())

        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",1,2),DateTimeUtil().Tomorrow())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",2,2),DateTimeUtil().Today())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",3,2),DateTimeUtil().Yesterday())
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第三个人工任务办理失败")
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",1,6),DateTimeUtil().Yesterday())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",2,6),DateTimeUtil().Today())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",3,6),DateTimeUtil().Tomorrow())

        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",1,2),DateTimeUtil().Tomorrow())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",2,2),DateTimeUtil().Today())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",3,2),DateTimeUtil().Yesterday())
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第四个人工任务办理失败")
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第五个人工任务办理失败")
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",1,6),DateTimeUtil().Yesterday())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",2,6),DateTimeUtil().Today())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",3,6),DateTimeUtil().Tomorrow())

        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",1,2),DateTimeUtil().Tomorrow())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",2,2),DateTimeUtil().Today())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",3,2),DateTimeUtil().Yesterday())
        formPage.Form_Button_Click("确认")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第六个人工任务办理失败")
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",1,6),DateTimeUtil().Yesterday())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",2,6),DateTimeUtil().Today())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",3,6),DateTimeUtil().Tomorrow())

        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",1,2),DateTimeUtil().Tomorrow())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",2,2),DateTimeUtil().Today())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",3,2),DateTimeUtil().Yesterday())
        formPage.Form_Button_Click("确认")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第七个人工任务办理失败")
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",1,6),DateTimeUtil().Yesterday())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",2,6),DateTimeUtil().Today())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目团队成员",3,6),DateTimeUtil().Tomorrow())

        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",1,2),DateTimeUtil().Tomorrow())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",2,2),DateTimeUtil().Today())
        self.assertEqual(formPage.ChildForm_GetTdValue("项目进度管理",3,2),DateTimeUtil().Yesterday())
        formPage.Form_Button_Click("确认")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第八个人工任务办理失败")