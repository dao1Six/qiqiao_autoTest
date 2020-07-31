# coding=utf-8
import time
import unittest

from public.driver import Driver
from qiqiao_page.pc_page.applicationList_page import ApplicationListPage
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.portal_page import PortalPage
import os

class DataFilterAppTest_001 (unittest.TestCase):
    '''PC端数据过滤应用导出测试'''

    ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"
    downloadPath = ProjectRootPath + '\\file_data\\downloadData'

    def isFileExists(self,path):
        if os.path.exists(path):  # 如果文件存在
            # 删除文件，可使用以下两种方法。
            # os.remove(path)
            return True
        else:
            return False # 则返回文件不存在



    def setUp(self):
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wanghao@auto", "do1qiqiao")
        time.sleep(5)
        #'''删除数据'''
        filePath = self.downloadPath+"//列表.xls"
        if(self.isFileExists(filePath)):
            os.remove(filePath)

    def test_01( self ):
        '''单表导出'''
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','数据过滤测试应用')
        businessPage = BusinessPage(self.driver)
        # businessPage.BusinessPage_LeftMenu_Click('子表')
        businessPage.ListComponent_Click_ListHeader_Button("导出")
        businessPage.ListComponent_dialogfooterButton_Click("确 定")
        time.sleep(15)
        filePath = self.downloadPath + "//列表.xls"
        self.assertTrue(self.isFileExists(filePath))


    def test_02( self ):
        '''子表导出'''
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','数据过滤测试应用')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('子表')
        businessPage.ListComponent_Click_ListHeader_Button("导出")
        businessPage.ListComponent_dialogfooterButton_Click("确 定")
        time.sleep(15)
        filePath = self.downloadPath + "//列表.xls"
        self.assertTrue(self.isFileExists(filePath))