# coding=utf-8
import os
import time
import unittest
from functools import wraps

from Enum.fileTypeEnum import FileTypeEnum
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


class PcBugAppTest_001(unittest.TestCase):
    """PC端过往补丁应用1"""


    def setUp(self):
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        time.sleep(3)




    def test_01( self ):
        """【补丁】——分组组件中的必填字段，打开方式为弹窗时，不可见的情况下，进行了必填校验"""
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','PC端补丁收集应用')
        businessPage = BusinessPage(self.driver)
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        businessPage.ListComponent_Click_ListHeader_Button('添加')
        popFormPage = PopupFormPage(self.driver)
        popFormPage.PopupFormPage_Button_Click('提交')
        time.sleep(3)
        self.assertEqual(businessPage.ListComponent_GetRecordTotal(),1)

    def test_02( self ):
        """【补丁】——PC端数字公式运算sum函数，计算不出数值(计算字段数量超过20个，就无效，20个以内有效)"""
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','补丁转自动化应用')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('sum函数')
        businessPage.ListComponent_Click_ListHeader_Button('添加')
        formPage = FormPage(self.driver)
        formPage.Grade_Sendkeys("评分1",3)
        formPage.Grade_Sendkeys("评分2",3)
        formPage.Grade_Sendkeys("评分3",3)
        formPage.Grade_Sendkeys("评分4",3)
        formPage.Grade_Sendkeys("评分5",3)
        formPage.Grade_Sendkeys("评分6",3)
        formPage.Grade_Sendkeys("评分7",3)
        formPage.Grade_Sendkeys("评分8",3)
        formPage.Grade_Sendkeys("评分9",3)
        formPage.Grade_Sendkeys("评分10",3)
        formPage.Grade_Sendkeys("评分11",3)
        formPage.Grade_Sendkeys("评分12",3)
        formPage.Grade_Sendkeys("评分13",3)
        formPage.Grade_Sendkeys("评分14",3)
        formPage.Grade_Sendkeys("评分15",3)
        formPage.Grade_Sendkeys("评分16",3)
        formPage.Grade_Sendkeys("评分17",3)
        formPage.Grade_Sendkeys("评分18",3)
        formPage.Grade_Sendkeys("评分19",3)
        formPage.Grade_Sendkeys("评分20",3)
        formPage.Grade_Sendkeys("评分21",3)
        formPage.Grade_Sendkeys("评分22",3)
        time.sleep(3)
        self.assertEqual(formPage.Number_GetValue_Writable("总评分"),66)



    def test_03( self ):
        """PC端多表关联中间表设置默认值无效"""
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','补丁转自动化应用')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('主表')
        businessPage.ListComponent_Click_ListHeader_Button('添加')
        formPage = FormPage(self.driver)
        formPage.MultiForm_AddButton_Click("多表关联")
        self.assertEqual(formPage.MultiForm_GetTdValue("多表关联",1,9),"中国")
        self.assertEqual(formPage.MultiForm_GetTdValue("多表关联",1,19),"刁惠云 , 罗琳月")
        self.assertEqual(formPage.MultiForm_GetTdValue("多表关联",1,21),"创新技术中心 , 财务一部")


    def test_04( self ):
        """PC端外键连带写入不生效"""
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','补丁转自动化应用')
        businessPage = BusinessPage(self.driver)
        businessPage.ListComponent_Click_ListHeader_Button('添加')
        formPage = FormPage(self.driver)
        formPage.Text_Sendkeys("单行文本","1")
        time.sleep(1)
        formPage.ForeignSelection_Sendkeys("外键选择","1")
        time.sleep(3)
        self.assertEqual(formPage.Textarea_GetValue_Writable("多行文本"),"1")
        self.assertEqual(formPage.User_GetUserValue_Writable("人员单选"),["罗静文"])
        self.assertEqual(formPage.User_GetUserValue_Writable("人员多选"),["吴茵婷","周文月"])
        self.assertEqual(formPage.Dept_GetDeptValue_Writable("部门单选"),["事业二部"])
        self.assertEqual(formPage.Dept_GetDeptValue_Writable("部门多选"),["事业一部->业务支持部","事业一部->业务四部"])
        self.assertEqual(formPage.Date_GetValue_writable("日期"),"2020-09-25")
        self.assertEqual(formPage.Time_GetValue_writable("时间"),"16:15")
        self.assertEqual(formPage.DateTime_GetValue_writable("日期时间"),"2020-09-22 06:06")
        self.assertEqual(formPage.Selection_MultiXialaValue_writable("多项下拉"),"奥迪A4L;宝马X6;")





    def test_05( self ):
        """【补丁】--PC运行平台脚本执行异常:低代码获取的documentt没有form对象"""
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','PC端补丁收集应用')
        businessPage = BusinessPage(self.driver)
        businessPage.ListComponent_Click_ListHeader_Button('添加2')
        popFormPage = PopupFormPage(self.driver)
        popFormPage.PopupFormPage_Button_Click('提交')
        self.assertIn("成功",businessPage.Public_GetAlertMessage())


    def test_06( self ):
        """pc运行平台浏览器标题"""
        time.sleep(2)
        title_page = self.driver.title
        self.assertEqual("接口自动化七巧广泛广泛",title_page,msg="浏览器标题不正确")


    def test_07( self ):
        """流程管理打开数据不能滚动"""
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("流程")
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_menu("流程管理")
        processPage.ProcessPage_searchItem_sendkeys("流程名称","事业一部订单发起",FileType=FileTypeEnum.Text)
        processPage.ProcessPage_searchButton_Click("搜索")
        time.sleep(3)
        processPage.ProcessPage_click_process_record(1)
        formPage = FormPage(self.driver)
        formPage.Form_scroll(10000)
        formPage.Form_field_isVisibility("订单状态")



















