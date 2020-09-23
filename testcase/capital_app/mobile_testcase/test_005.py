# coding=utf-8
import time
import unittest

from public.driver import Driver
from qiqiao_page.mobile_page.mb_business_page import MbBusinessPage
from qiqiao_page.mobile_page.mb_form_page import MbFormPage
from qiqiao_page.mobile_page.mobile_application_page import MbApplicationListPage
from qiqiao_page.mobile_page.mobile_home_page import MbHomePage
from qiqiao_page.mobile_page.mobile_login_page import MbLoginPage
from qiqiao_page.mobile_page.mobile_to_do_page import MbTodoPage
from util.dateTimeUtil import DateTimeUtil


class MbJiXiaoAppTest_005(unittest.TestCase):
    '''移动端绩效管理流程检查'''

    def mbLogin( self,account,password ):
        '''登录移动端'''
        self.driver = Driver().phonedriver()
        self.driver.maximize_window()
        loginpage = MbLoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/mruntime',account,password)
        time.sleep(5)

    def test_01( self ):
        '''【补丁】移动端运行平台--多表关联组件--中间表-单选字段配置仅展示--值传递过来但是仍提示不能为空'''
        self.mbLogin("wujianlun@auto","do1qiqiao")
        homePage = MbHomePage(self.driver)
        homePage.HomePage_BottomNav_Click("待办")
        # 发起流程
        todoPage = MbTodoPage(self.driver)
        todoPage.MbTodoPage_Faqiliucheng('绩效','绩效考核申请')
        formPage = MbFormPage(self.driver)
        formPage.MbDept_MonomialDept_Sendkeys("考核部门","产品规划组",index=1)
        formPage.MbDate_SendKeys("考核日期",DateTimeUtil().Today())
        time.sleep(2)
        formPage.MbMultiForm_AddButton_Click("考核明细")
        formPage.MbMultiForm_BathManagePage_Record_Tick("考核明细",[1])
        formPage.MbMultiForm_BathManagePage_Button_Cick("考核明细","确定选择")
        time.sleep(1)
        formPage.MbForm_Button_Click("提交")
        formPage.MbForm_ProcessHandle_Pop_QuerenButton_Click()  # 点击流程办理弹框确认按钮
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第一个人工任务办理失败")
        time.sleep(2)
        #进行第二个人工任务处理
        self.driver.back()
        todoPage.MbTodoPage_ProcessRecord_Click(1)
        #点击多表关联组件编辑按钮
        formPage.MbMultiForm_edit_Record("考核明细",1)
        formPage.MbNumber_Sendkeys("自评",50)
        formPage.MbForm_Click_Button_InPopup("保存")
        formPage.MbForm_Button_Click("办理")
        formPage.MbForm_ProcessHandle_Pop_QuerenButton_Click()  # 点击流程办理弹框确认按钮
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第二个人工任务办理失败")
        time.sleep(2)
        #进行第三个人工任务处理
        todoPage.MbTodoPage_ProcessRecord_Click(1)
        #点击多表关联组件编辑按钮
        formPage.MbMultiForm_edit_Record("考核明细",1)
        formPage.MbNumber_Sendkeys("领导评分",50)
        formPage.MbSelection_SingleXiala_Senkeys("评价等级","A")
        formPage.MbForm_Click_Button_InPopup("保存")
        formPage.MbForm_Button_Click("办理")
        formPage.MbForm_ProcessHandle_Pop_QuerenButton_Click()  # 点击流程办理弹框确认按钮
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="第三个人工任务办理失败")