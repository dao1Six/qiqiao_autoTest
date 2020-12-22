# coding=utf-8
import time
import unittest

from public.driver import Driver
from qiqiao_page.pc_page.applicationList_page import ApplicationListPage
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.portal_page import PortalPage
import os

from util.excel_xlrd import ExcelReadUtil


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
        #'''删除数据'''
        filePath = self.downloadPath+"//列表.xls"
        if(self.isFileExists(filePath)):
            os.remove(filePath)
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wanghao@auto", "do1qiqiao")
        time.sleep(3)


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

    def test_03( self ):
        '''【补丁】-开发平台，子表关联无法导出'''
        filePath = self.downloadPath+"//列表.xls"
        if(self.isFileExists(filePath)):
            os.remove(filePath)
            # 打开生产运营管理应用
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','售后工单系统')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click("工单管理")
        businessPage.ListComponent_Click_ListHeader_Button("导出")
        businessPage.ListComponent_dialogfooterButton_Click("确 定")
        time.sleep(10)
        filePath = self.downloadPath + "//列表.xls"
        self.assertTrue(self.isFileExists(filePath),msg="导出不成功")
        excelReader = ExcelReadUtil()
        sheet = excelReader.getSheetValue(filePath,1)
        rowValues = excelReader.getRowValues(sheet,2)
        print(rowValues)
        self.assertEqual(['1', 'GD-20200924-0001', '员工管理模块', '五福珠宝', '技术支援', '吴先生', '13025806548', '中', '一般', '大苏打撒旦撒旦撒旦', '阿达萨达萨达飒飒大大', '北京/北京市/西城区 大大撒大苏打撒大苏打', '', '', '', 44098.0, '', '', '', '', '', '已受理待指派', '吴健伦', '吴健伦', 44098.72708333333, 44098.73472222222, '吴健伦', 44098.72767361111, 44098.73516203704, '员工评分系统', '员工评分系统', '00023', '00001', '撒旦萨达萨达萨达萨达萨达撒旦大神', '大苏打萨达萨达萨达萨达萨达是', 'GD-20200924-0001'],excelReader.getRowValues(sheet,2))



    def test_04( self ):
        '''【补丁】---PC运行平台---导出数据---导出的数据中含有子表数据，最多只能导出30条子表数据。导致数据缺失'''
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','数据过滤测试应用2')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('子表')
        businessPage.ListComponent_Click_ListHeader_Button("导出")
        businessPage.ListComponent_dialogfooterButton_Click("确 定")
        time.sleep(15)
        filePath = self.downloadPath + "//列表.xls"
        self.assertTrue(self.isFileExists(filePath))
        excelReader = ExcelReadUtil()
        sheet = excelReader.getSheetValue(filePath, 1)
        self.assertEqual(81,excelReader.getRowsClosNum(sheet)[0],msg="导出文件行数不对")
        self.assertEqual(33, excelReader.getRowsClosNum(sheet)[1], msg="导出文件列数不对")


    def test_05( self ):
        '''【补丁】---PC运行平台--导出大量数据超时'''
        filePath = self.downloadPath+"//订单管理列表2.xls"
        if(self.isFileExists(filePath)):
            os.remove(filePath)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','压测应用')
        businessPage = BusinessPage(self.driver)
        businessPage.ListComponent_Click_ListHeader_Button("导出")
        businessPage.ListComponent_dialogfooterButton_Click("确 定")
        time.sleep(20)
        filePath = self.downloadPath + "//订单管理列表2.xls"
        self.assertTrue(self.isFileExists(filePath))
        excelReader = ExcelReadUtil()
        sheet = excelReader.getSheetValue(filePath, 1)
        self.assertGreater(excelReader.getRowsClosNum(sheet)[0],9000,msg="导出文件行数不对")
