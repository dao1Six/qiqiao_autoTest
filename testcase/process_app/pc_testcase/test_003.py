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





