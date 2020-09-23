# coding=utf-8
import time
import unittest

from public.driver import Driver
from qiqiao_page.pc_page.applicationList_page import ApplicationListPage
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.form_page import FormPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.portal_page import PortalPage
from util.dateTimeUtil import DateTimeUtil


class PomAppTest_002(unittest.TestCase):
    '''生产运营应用PC端填写工时测试'''


    @classmethod
    def setUpClass(self):
        '''初始化数据'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        time.sleep(3)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','生产运管系统')
        businessPage = BusinessPage(self.driver)
        #清除领用及相关数据
        businessPage.BusinessPage_LeftMenu_Click('工时管理')
        businessPage.BusinessPage_LeftMenu_Click('本周工时填报')
        # 判断列表是否存在数据
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        self.driver.quit()



    def setUp(self):
        '''登录'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        time.sleep(5)


    def test_01( self ):
        '''填写本周工时'''
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '生产运管系统')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('工时管理')
        businessPage.BusinessPage_LeftMenu_Click('本周工时填报')
        businessPage.ListComponent_Click_ListHeader_Button("添加工时")
        formPage = FormPage(self.driver)
        formPage.ChildForm_AddButton_Click('工时明细')
        daysList = DateTimeUtil().Get_CurrentWeek_Days_UntilNow()
        workingDays = 0
        if (len(daysList)>5):
            workingDays = 5
        else:
            workingDays = len(daysList)
        for i in range(workingDays):
            #添加明细数据
            if (i < 1):
                formPage.Selection_SingleBox_InPopup_Sendkeys("工时明细", "工时类型", "产品研发工作")
                time.sleep(2)
                formPage.Date_InChildForm_Sendkeys("工时明细", "工时日期", daysList[i], isclear=True)
                formPage.ForeignSelection_InPopup_Sendkeys("工时明细", "产品名称", "白云制药厂")
                formPage.Selection_SingleXiala_InPopup_Sendkeys("工时明细", "工作内容", "产品测试")
            elif(i>=1):
                formPage.Date_InChildForm_Sendkeys("工时明细", "工时日期", daysList[i],
                                                   isclear=True)
                formPage.ForeignSelection_InPopup_Sendkeys("工时明细", "项目名称", "广东")
                formPage.Selection_SingleXiala_InPopup_Sendkeys("工时明细", "工作内容", "测试")
            if(i<workingDays-1):
                formPage.click_ChildForm_Button("保存并继续添加")
            else:
                formPage.click_ChildForm_Button("保存")
            time.sleep(2)
        self.assertEqual(str((workingDays) * 8),formPage.Number_GetValue_readOnly("本次工时合计"),msg="工时合计不正确")
        formPage.Form_Button_Click("提交")
        self.assertIn("成功",formPage.Public_GetAlertMessage(),msg="工时填报提交失败")



