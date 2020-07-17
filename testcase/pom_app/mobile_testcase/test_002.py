# coding=utf-8
import time
import unittest

from public.driver import Driver
from qiqiao_page.mobile_page.business_components.mb_list_component import MbListComponent
from qiqiao_page.mobile_page.mb_form_page import MbFormPage
from qiqiao_page.mobile_page.mobile_application_page import MbApplicationListPage
from qiqiao_page.mobile_page.mobile_home_page import MbHomePage
from qiqiao_page.mobile_page.mobile_login_page import MbLoginPage
from qiqiao_page.pc_page.applicationList_page import ApplicationListPage
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.form_page import FormPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.portal_page import PortalPage
from util.dateTimeUtil import DateTimeUtil


class MbPomAppTest_002(unittest.TestCase):
    '''移动端生产运营应用填写工时测试'''


    @classmethod
    def setUpClass(self):
        self.pdate()

    def pdate(self):
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
        self.mbLogin("wujianlun@auto","do1qiqiao")


    def mbLogin(self,account,password):
        '''登录pc端'''
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
        '''移动端填写本周工时'''
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('生产运管系统','填报工时')
        listPage = MbListComponent(self.driver)
        listPage.MbListComponent_AddButton_Click()
        formPage = MbFormPage(self.driver)
        formPage.MbChildForm_AddButton_Click('工时明细')
        daysList = DateTimeUtil().Get_CurrentWeek_Days_UntilNow()
        workingDays = 0
        if (len(daysList)>5):
            workingDays = 5
        else:
            workingDays = len(daysList)
        for i in range(workingDays):
            #添加明细数据
            if (i < 1):
                formPage.MbSelection_Radio_Senkeys("工时类型", "产品研发工作")
                time.sleep(2)
                formPage.MbDate_SendKeys("工时日期", daysList[i])
                formPage.MbForeignSelection_Sendkeys("产品名称", "白云制药厂")
                formPage.MbSelection_Xiala_Senkeys("工作内容", "产品测试")
            elif(i>=1):
                formPage.MbDate_SendKeys("工时日期", daysList[i])
                formPage.MbForeignSelection_Sendkeys("项目名称", "广东")
                formPage.MbSelection_Xiala_Senkeys("工作内容", "测试")
            if(i<workingDays-1):
                formPage.MbChildForm_Button_Click("保存并继续添加")
            else:
                formPage.MbChildForm_Button_Click("保存")
            time.sleep(2)
        self.assertEqual(str((workingDays) * 8),formPage.MbNumber_GetValue_readOnly("本次工时合计"),msg="工时合计不正确")
        formPage.MbForm_Button_Click("提交")
        self.assertIn("成功",formPage.Public_GetAlertMessage(),msg="工时填报提交失败")



