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
from util.dateTimeUtil import DateTimeUtil


class ProcessAppTest_002(unittest.TestCase):
    '''流程应用检查'''


    def pcLogin(self,account,password):
        '''登录pc端'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', account, password)
        time.sleep(3)


    def test_01( self ):
        '''流程操作检查'''
        #发起流程
        self.pcLogin("diaohuiyun@A1","qiqiao123")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(3)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("处理人设置测试流程")
        formPage = FormPage(self.driver)
        formPage.Text_Sendkeys("单行文本","用户")
        formPage.Form_Switch_Tab("人员部门类组件")
        formPage.User_MonomialUser_Sendkeys("人员单选","张月娟")
        formPage.User_MultiUser_Sendkeys("人员多选",["周子贤","周润泽"])
        formPage.Dept_MonomialDept_Sendkeys("部门单选","产品研发二部",index=1)
        formPage.Dept_MultiDept_Sendkeys("部门多选",{"产品研发二部":1,"产品研发一部":1})
        formPage.Form_Button_Click("办理")
        self.assertEqual(formPage.Form_Get_ProcessManagers(),["吴健伦"],msg="固定用户人工任务办理者错误")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功', formPage.Public_GetAlertMessage(), msg="第1个人工任务办理失败")
        self.driver.quit()
        #流转到固定任务节点办理流程
        self.pcLogin("wujianlun@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        #委托给罗琳月
        formPage.Form_ButtonInMore_Click("委托")
        formPage.Form_Select_ProcessManager(["罗琳月"])
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="委托操作失败")
        self.driver.quit()
        #罗琳月办理
        self.pcLogin("luolinyue@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        self.assertEqual(formPage.Form_Get_ProcessManagers(),['周润泽','张月娟','周子贤'],msg="表单人员字段人工任务办理者错误")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="表单人员字段人工任务办理失败")
        self.driver.quit()
        #流转到表单人员字段人工任务办理
        self.pcLogin("zhangyuejuan@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        #加前签操作
        formPage.Form_ButtonInMore_Click("加签")
        formPage.Form_Select_Signature("加前签")
        formPage.Form_Select_ProcessManager(["王浩","王栋一"])
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('加签办理成功！',formPage.Public_GetAlertMessage(),msg="加前签失败")
        self.driver.quit()
        #加前签人员办理
        self.pcLogin("wanghao@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        self.assertIn('张月娟',formPage.Form_Get_ProcessManagers(),msg="表单人员字段人工任务办理者错误")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="表单人员字段人工任务办理失败")
        self.driver.quit()
        # 加前签人员办理
        self.pcLogin("wangdongyi@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        self.assertIn('张月娟',formPage.Form_Get_ProcessManagers(),msg="表单人员字段人工任务办理者错误")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="表单人员字段人工任务办理失败")
        self.driver.quit()
        #流转回表单人员字段人工任务办理者办理
        self.pcLogin("zhangyuejuan@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        #加会签操作
        formPage.Form_ButtonInMore_Click("加签")
        formPage.Form_Select_ProcessManager(["罗琳月"])
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('加签办理成功！',formPage.Public_GetAlertMessage(),msg="加会签失败")
        time.sleep(5)
        formPage.Form_Button_Click("办理")
        formPage.Form_Select_ProcessManager(["刁惠云"])
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="任意指定人工任务办理失败")
        self.driver.quit()
        #加会签人员办理
        self.pcLogin("luolinyue@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_Select_ProcessManager(["刁惠云"])
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="任意指定人工任务办理失败")
        self.driver.quit()
        #任意指定人工任务办理者驳回
        self.pcLogin("diaohuiyun@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("驳回")
        formPage.Form_Select_RejectNode("表单人员字段")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('流程驳回成功！',formPage.Public_GetAlertMessage(),msg="任意指定人工任务办理失败")
        self.driver.quit()
        # 流转回表单人员字段人工任务办理者办理
        self.pcLogin("zhangyuejuan@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_Select_ProcessManager(["罗琳月"])
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="任意指定人工任务办理失败")
        self.driver.quit()
        # 任意指定人工任务办理者办理
        self.pcLogin("luolinyue@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        print(formPage.Form_Get_ProcessManagers())
        self.assertEqual(formPage.Form_Get_ProcessManagers(),['罗琳月'],msg="上个任务办理者的办理者人工任务办理者错误")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="上个任务办理者的办理者人工任务办理失败")
        #上个任务办理者的办理者人工任务办理
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        print(formPage.Form_Get_ProcessManagers())
        self.assertEqual(formPage.Form_Get_ProcessManagers(),["吴健伦"],msg="上个任务办理者的部门主管人工任务办理者错误")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="上个任务办理者的部门主管人工任务办理失败")
        self.driver.quit()
        #上个任务办理者的部门主管人工任务办理者
        self.pcLogin("wujianlun@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_Select_ProcessManager(["刁惠云"])
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="任意指定人工任务办理失败")
        self.driver.quit()
        #任意指定人工任务办理
        self.pcLogin("diaohuiyun@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        print(formPage.Form_Get_ProcessManagers())
        self.assertEqual(formPage.Form_Get_ProcessManagers(),["吴健伦"],msg="上个任务办理者的上级部门主管人工任务办理者错误")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="上个任务办理者的上级部门主管人工任务办理失败")
        self.driver.quit()
        #上个任务办理者的上级部门主管人工任务办理
        self.pcLogin("wujianlun@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        print(formPage.Form_Get_ProcessManagers())
        self.assertEqual(formPage.Form_Get_ProcessManagers(),["罗琳月"],msg="与指定节点办理者相关人工任务办理者错误")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="与指定节点办理者相关人工任务办理失败")
        self.driver.quit()
        #与指定节点办理者相关人工任务办理
        self.pcLogin("luolinyue@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        print(formPage.Form_Get_ProcessManagers())
        self.assertEqual(formPage.Form_Get_ProcessManagers(),['刁惠云'],msg="流程发起人人工任务办理者错误")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="流程发起人人工任务办理失败")
        self.driver.quit()
        #流程发起人人工任务办理
        self.pcLogin("diaohuiyun@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        print(formPage.Form_Get_ProcessManagers())
        self.assertEqual(formPage.Form_Get_ProcessManagers(),['王栋一'],msg="流程发起人的部门主管人工任务办理者错误")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="流程发起人的部门主管人工任务办理失败")
        self.driver.quit()
        #流程发起人的部门主管人工任务办理
        self.pcLogin("wangdongyi@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        print(formPage.Form_Get_ProcessManagers())
        self.assertEqual(formPage.Form_Get_ProcessManagers(),["吴健伦"],msg="流程发起人的上级部门主管人工任务办理者错误")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="流程发起人的上级部门主管人工任务办理失败")
        self.driver.quit()
        #流程发起人的上级部门主管人工任务办理
        self.pcLogin("wujianlun@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        print(formPage.Form_Get_ProcessManagers())
        self.assertEqual(formPage.Form_Get_ProcessManagers(),['王浩'],msg="人工任务3人工任务办理者错误")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="人工任务3人工任务办理失败")
        self.driver.quit()
        #人工任务3人工任务办理
        self.pcLogin("wanghao@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="人工任务3办理失败")

    def test_02( self ):
        '''【补丁】--PC运行平台--百分比号未显示'''
        # 发起流程
        self.pcLogin("diaohuiyun@A1","qiqiao123")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(2)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("TC员工年度评价流程")
        formPage = FormPage(self.driver)
        formPage.MultiForm_BatchManagementButton_Click("业绩评价")
        formPage.MultiForm_BathManagePage_Record_Tick("业绩评价",[1,2])
        formPage.MultiForm_BathManagePage_ConfirmButton_Tick("业绩评价")
        time.sleep(1)
        self.assertEqual("80.5%",formPage.MultiForm_GetTdValue("业绩评价",1,10),msg="业绩评价权重显示不对")
        self.assertEqual("70%",formPage.MultiForm_GetTdValue("业绩评价",2,10),msg="业绩评价权重显示不对")


    def test_03( self ):
        '''【【补丁】--流程审批节点设置了触发事件后，驳回操作会校验必填字段'''
        self.pcLogin("wujianlun@A1","qiqiao123")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(2)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("换班申请审批")
        formPage = FormPage(self.driver)
        formPage.User_MonomialUser_Sendkeys("拟换值带班人员","张月娟")
        formPage.Date_Sendkeys("换班日期",DateTimeUtil().Today())
        time.sleep(1)
        formPage.Textarea_Sendkeys("换班事由","到拉萨扩大哈十大十大开始打火山")
        time.sleep(1)
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="提交失败")
        self.driver.quit()
        self.pcLogin("zhangyuejuan@A1","qiqiao123")
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage = FormPage(self.driver)
        formPage.Form_Button_Click("驳回")
        time.sleep(1)
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="驳回失败")



    def test_04( self ):
        '''【补丁】--流程中A的待办委托给B，B再委托回给A，这时候A的待办没有数据'''
        self.pcLogin("diaohuiyun@A1","qiqiao123")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(3)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("流程委托测试")
        formPage = FormPage(self.driver)
        formPage.Text_Sendkeys("单行文本","用户")
        formPage.Form_Switch_Tab("人员部门类组件")
        formPage.User_MonomialUser_Sendkeys("人员单选","张月娟")
        formPage.User_MultiUser_Sendkeys("人员多选",["周子贤","周润泽"])
        formPage.Dept_MonomialDept_Sendkeys("部门单选","产品研发二部",index=1)
        formPage.Dept_MultiDept_Sendkeys("部门多选",{"产品研发二部":1,"产品研发一部":1})
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="提交操作失败")
        self.driver.quit()
        self.pcLogin("zhangyuejuan@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_ButtonInMore_Click("委托")
        formPage.Form_Select_ProcessManager(["吴健伦"])
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="委托操作失败")
        self.driver.quit()
        self.pcLogin("wujianlun@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_ButtonInMore_Click("委托")
        formPage.Form_Select_ProcessManager(["张月娟"])
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="委托操作失败")
        self.driver.quit()
        self.pcLogin("zhangyuejuan@A1","qiqiao123")
        formPage = FormPage(self.driver)
        processPage = ProcessPage(self.driver)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        self.assertIn("刁惠云的流程委托测试_",processPage.ProcessPage_get_processTdValue(1,2),msg="【补丁】--流程中A的待办委托给B，B再委托回给A，这时候A的待办没有数据")



