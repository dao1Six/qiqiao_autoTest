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
from qiqiao_page.pc_page.externalForm_page import ExternalFormPage


class ProcessAppTest_003(unittest.TestCase):
    '''流程应用检查'''


    def pcLogin(self,account,password):
        '''登录pc端'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', account, password)
        time.sleep(3)


    def test_01( self ):
        '''【补丁】——自定义开发按钮，配置脚本批量发起流程时，系统报错（单条数据正常，多条数据报错）'''
        self.pcLogin("wujianlun@A1","qiqiao123")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '数据过滤测试应用')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click("多表组件")
        businessPage.ListComponent_SelectAllRecord()
        businessPage.ListComponent_Click_ListHeader_Button("发起流程")
        businessPage.ListComponent_TooltipButton_Click('确定')
        self.assertIn('成功',businessPage.Public_GetAlertMessage(),msg="列表自定义发起流程失败")
        businessPage.BusinessPage_HeardItem_AllApp_Click()
        portalPage.PortalPage_Click_HeaderMenu("流程")
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_menu("我的待办")
        self.assertIn("吴健伦的自定义按钮发起流程",processPage.ProcessPage_get_processTdValue(1,2))
        self.assertEqual("自定义按钮发起流程",processPage.ProcessPage_get_processTdValue(1,3))
        self.assertIn("吴健伦的自定义按钮发起流程",processPage.ProcessPage_get_processTdValue(2,2))
        self.assertEqual("自定义按钮发起流程",processPage.ProcessPage_get_processTdValue(2,3))
        self.assertIn("吴健伦的自定义按钮发起流程",processPage.ProcessPage_get_processTdValue(3,2))
        self.assertEqual("自定义按钮发起流程",processPage.ProcessPage_get_processTdValue(3,3))
        processPage.ProcessPage_click_process_record(1)
        formPage = FormPage(self.driver)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()  # 点击流程办理弹框确认按钮
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="流程办理失败")




    def test_02( self ):
        '''【补丁】---流程中的触发事件在一个事件里写两个公式运算，结果显示有误'''
        self.pcLogin("wujianlun@A1","qiqiao123")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '安畅费控报销2.0')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click("预算管理")
        businessPage.BusinessPage_LeftMenu_Click("预算明细")
        #判断列表是否存在数据
        if(businessPage.ListComponent_GetRecordTotal()>0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功'in  businessPage.Public_GetAlertMessage()
        businessPage.ListComponent_Click_ListHeader_Button('添加')
        formPage = FormPage(self.driver)
        formPage.ForeignSelection_Sendkeys("预算大类","基础设备费用")
        formPage.Number_Sendkeys("第一季度预算",10000)
        formPage.Number_Sendkeys("第二季度预算", 10000)
        formPage.Number_Sendkeys("第三季度预算", 10000)
        formPage.Number_Sendkeys("第四季度预算", 10000)
        formPage.Number_Sendkeys("可用预算", 10000)
        formPage.Number_Sendkeys("冻结金额", 10000)
        formPage.Form_Button_Click("提交")
        businessPage.ListComponent_Click_ListHeader_Button('添加')
        formPage.ForeignSelection_Sendkeys("预算大类","员工关怀费用")
        formPage.Number_Sendkeys("第一季度预算",10000)
        formPage.Number_Sendkeys("第二季度预算", 10000)
        formPage.Number_Sendkeys("第三季度预算", 10000)
        formPage.Number_Sendkeys("第四季度预算", 10000)
        formPage.Number_Sendkeys("可用预算", 10000)
        formPage.Number_Sendkeys("冻结金额", 10000)
        formPage.Form_Button_Click("提交")
        businessPage.BusinessPage_HeardItem_AllApp_Click()
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("费用报销")
        formPage.ChildForm_AddButton_Click("明细")
        formPage.ForeignSelection_InPopup_Sendkeys("明细","预算大类名称","基础设备费用")
        time.sleep(2)
        formPage.Number_InPopup_Sendkeys("明细","报销金额",2000)
        formPage.click_ChildForm_Button("保存")
        formPage.ChildForm_AddButton_Click("明细")
        formPage.ForeignSelection_InPopup_Sendkeys("明细","预算大类名称","员工关怀费用")
        time.sleep(2)
        formPage.Number_InPopup_Sendkeys("明细","报销金额",1000)
        formPage.click_ChildForm_Button("保存")
        time.sleep(2)
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()   #点击流程办理弹框确认按钮
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第一个人工任务办理失败")
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '安畅费控报销2.0')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click("预算管理")
        businessPage.BusinessPage_LeftMenu_Click("预算明细")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1,12),"11000")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1,16),"-1000")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(2,12),"12000")
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(2,16),"-2000")

    def test_03( self ):
        '''【【补丁】---日期，日期时间，时间字段的可选最早功能自带的校验在审批人提交的节点也会生效】'''
        self.pcLogin("wujianlun@A1","qiqiao123")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(2)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("日期限制流程")
        formPage = FormPage(self.driver)
        formPage.Date_Sendkeys("日期",DateTimeUtil().Today())
        time.sleep(1)
        formPage.Time_Sendkeys("时间",DateTimeUtil().CurrentHM())
        time.sleep(1)
        formPage.DateTime_Sendkeys("日期时间",DateTimeUtil().Today() + " "+DateTimeUtil().CurrentHM())
        time.sleep(1)
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="提交失败")
        time.sleep(60)
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage = FormPage(self.driver)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()  # 点击流程办理弹框确认按钮
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="流程办理失败")

    def test_04( self ):
        '''【补丁】--外部单提交时提示系统任务执行异常'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        self.driver.get("https://qy.do1.com.cn/qiqiao/runtime/#/4b338f97931c4030b71605fa52789e23/4b330/a0ceb629a5894e3db5e8f80e60ab56d7/603df3ead2270900014ab314/externalForm")
        externalformpage = ExternalFormPage(self.driver)
        externalformpage.ExternalFormPage_Click_SubmitBtn()
        self.assertEqual("提交成功,感谢您的参与！",externalformpage.ExternalFormPage_Get_MessageContent())
        time.sleep(2)



