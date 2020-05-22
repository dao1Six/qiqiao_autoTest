# coding=utf-8
import datetime
import os
import time
import unittest

from ddt import ddt, data, unpack
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options

from app_page.saysafe_app_page.phone.i_declare_peace_page_loc import IDeclarePeacePage
from public.driver import Driver
from qiqiao_page.mobile_page.business_modelId_page import BusinessModelldPage
from qiqiao_page.mobile_page.form_page import FormPage
from qiqiao_page.mobile_page.mobile_login_page import MobileLoginPage
from util.parseExcel import ParseExcel


@ddt
class SaySafeAppTest(unittest.TestCase):

    # ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"
    # excelPath = ProjectRootPath+"\\testcase\\testcase_data\\测试数据.xlsx"
    # sheetName = "SaySafeAppTest"
    # excel = ParseExcel(excelPath, sheetName)
    #
    #
    # @data(*excel.getSheetValue())
    # @unpack
    # def test_001( self,a,b,c,d,e ):
    #     "加法运算"
    #     self.assertEquals(a,1)

    def setUp(self):
        self.driver = Driver().phonedriver()
        self.driver.maximize_window()
        loginpage = MobileLoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/mruntime', "wujianlun@auto", "do1qiqiao")
        self.driver.refresh()
        #打开“我要报平安页面”
        self.driver.get("https://qy.do1.com.cn/qiqiao/mruntime/#/admin/business/index?businessModelId=eaba256af6474943869011eae6935535&applicationId=d07cc4755a6b4dad97aa5ced0d60c70d&key_1580314921353_88569=%7B%22navName%22%3A%22%E6%88%91%E6%8A%A5%E5%B9%B3%E5%AE%89%22%7D")



    #测试添加一条报平安数据
    def test_AddSaySafeRecord( self ):
        '''检查报平安表单默认值'''
        iDeclarePeacePage = IDeclarePeacePage(self.driver)

        #点击我要报平安页面的添加按钮
        iDeclarePeacePage.clickElemByCSS_Presence(iDeclarePeacePage.addButtonLoc)

        formPage = FormPage(self.driver)
        # 校验提交日期字段值是否正确
        self.assertEqual(formPage.GetDateVale("提交日期"),datetime.datetime.now().strftime("%Y-%m-%d"))

        #校验员工姓名字段值是否正确
        self.assertEqual(formPage.GetUserValue("员工姓名"),"吴健伦")
        # 校验所属部门字段值是否正确
        self.assertEqual(formPage.GetDeptVale("所属部门"), "产品规划组")
        #校验"体温情况（腋窝测量）"字段 首项是否被选中
        self.assertTrue(formPage.RadioIsSelect("体温情况（腋窝测量）",0))
        # 校验"是否以下症状"字段 默认选中选项是否正确
        self.assertTrue(formPage.CheckboxIsSelect("是否以下症状",[4]))
        # 校验"是否有所接触"字段 默认选中选项是否正确
        self.assertTrue(formPage.CheckboxIsSelect("是否有所接触",[5]))
    #

    def test_ListButtonAuthority( self ):
        '''检查我报平安列表按钮权限'''
        businessModelldPage = BusinessModelldPage(self.driver)
        time.sleep(1)
        businessModelldPage.ClickAndHoleRecore(0)
        #校验列表按钮操作权限
        self.assertListEqual(["编辑","删除","取消"],businessModelldPage.GetRecoreButton())


    def test_ListTextValue( self ):
        '''校验我报平安页面标题语'''
        businessModelldPage = BusinessModelldPage(self.driver)
        time.sleep(1)
        # 校验我报平安页面标题语
        self.assertGreater(len(businessModelldPage.GetTextValue()),30)


    def test_ListTextValue( self ):
        '''校验我报平安页面导航是否显示齐全'''
        businessModelldPage = BusinessModelldPage(self.driver)
        time.sleep(1)
        # 校验我报平安页面导航是否显示齐全
        self.assertEquals(businessModelldPage.GetNavigationsName(),["全员报平安","报表中心"])








    # def tearDown(self):
    #     self.driver.quit()
