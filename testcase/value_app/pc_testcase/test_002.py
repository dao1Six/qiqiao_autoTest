# coding=utf-8
import time
import unittest

from ddt import ddt, data, unpack

from public.driver import Driver
from qiqiao_page.pc_page.applicationList_page import ApplicationListPage
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.portal_page import PortalPage

@ddt
class ValueAppTest_002(unittest.TestCase):
    '''道一云价值观应用，数据过滤检查'''

    def tearDown(self):
        self.driver.quit()



    @data(("diaohuiyun@auto",3),
         ("wanghao@auto",2),
         ("luolinyue@auto",1))
    @unpack
    def test_01( self,account,result):
        '''部门价值观数据检查'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', account, "do1qiqiao")
        time.sleep(5)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '道一云价值观')
        businessPage = BusinessPage(self.driver)
        businessPage.ListComponent_TabsOption_Click(" 部门价值观")
        time.sleep(5)
        self.assertEqual(result, businessPage.ListComponent_GetRecordTotal(),msg="部门价值观数据过滤错误")