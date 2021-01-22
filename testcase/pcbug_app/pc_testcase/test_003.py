# coding=utf-8
import os
import time
import unittest
from functools import wraps

from Enum.buttonEnum import ButtonEnum
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
from util.dateTimeUtil import DateTimeUtil
from util.excel_xlrd import ExcelReadUtil
from qiqiao_page.pc_page.externalForm_page import ExternalFormPage


class PcBugAppTest_003(unittest.TestCase):
    '''PC端过往补丁应用3'''

    ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"

    assetsDataPath = ProjectRootPath+"\\file_data\\testcase_data\\资产管理数据.xls"

    assets3DataPath = ProjectRootPath + "\\file_data\\testcase_data\\资产复制3.0.xls"

    assets4DataPath = ProjectRootPath + "\\file_data\\testcase_data\\人员姓名导入.xls"
    def pcLogin(self,account,password):
        '''登录pc端'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', account, password)
        time.sleep(3)


    def test_01( self ):
        '''【补丁】---PC运行平台--工作台首页常用应用常用流程丢失'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        self.assertEqual(['美安居建材云办公系统', '加特可人事评价模块'],portalPage.PortalPage_get_commonApplicationList(),msg="常用应用显示不对")
        self.assertEqual(['领用', '归还', '维修', '更换', '报废'],portalPage.PortalPage_get_commonProcessList(),msg="常用流程显示不对")


    def test_02( self ):
        '''工作台页面点击常用流程更多按钮跳转是否正常'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_commonProcessBtnMore()
        processPage=ProcessPage(self.driver)
        self.assertTrue(processPage.ProcessPage_IsIn(),msg="工作台页面点击常用流程更多按钮跳转不成功")


    def test_03( self ):
        '''工作台页面点击常用应用更多按钮跳转是否正常'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_commonAppBtnMore()
        applicationListPage=ApplicationListPage(self.driver)
        self.assertTrue(applicationListPage.ApplicationListPage_IsIn(),msg="工作台页面点击常用流程更多按钮跳转不成功")

    def test_04( self ):
        '''【补丁】---pc运行平台，编辑按钮页面，子表单数据，点击编辑第二条子表单数据，编辑页面显示第一条数据'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage=PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage=ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','数据过滤测试应用')
        businessPage=BusinessPage(self.driver)
        time.sleep(2)
        businessPage.BusinessPage_LeftMenu_Click('子表')
        businessPage.ListComponent_Click_ListRow_Button("编辑",1)
        formPage=FormPage(self.driver)
        formPage.ChildForm_Record_Edit("子表单",3)
        self.assertEqual("00175",formPage.SerialNumber_GetValue_readOnly_InPopup("子表单","生成编码"),msg="【补丁】---pc运行平台，编辑按钮页面，子表单数据，点击编辑第二条子表单数据，编辑页面显示第一条数据")
        formPage.Form_Close_Popup("子表单")
        time.sleep(2)
        formPage.ChildForm_Record_Edit("子表单",1)
        self.assertEqual("00149",formPage.SerialNumber_GetValue_readOnly_InPopup("子表单","生成编码"),msg="【补丁】---pc运行平台，编辑按钮页面，子表单数据，点击编辑第二条子表单数据，编辑页面显示第一条数据")



    def test_05( self ):
        '''【补丁】--PC端/移动端--开发平台人员单选配置用户所属部门人员，运行平台通过搜索用户所属部门下的子部门的人员，显示暂无数据'''
        self.pcLogin("pengzheng@A1","qiqiao123")
        portalPage=PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage=ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','补丁应用')
        businessPage=BusinessPage(self.driver)
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage=FormPage(self.driver)
        formPage.User_click_UserSelectBox("人员单选1")
        formPage.User_sendkeys_UserSearch("王栋一")
        self.assertTrue(formPage.User_UserSearchOption_IsExist("王栋一"))


    def test_06( self ):
        '''【补丁】---字段设置外键字段为可用条件外键不等于空值，外键设置可选无，选择“无”时，可用条件失效（“无”为空值）'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage=PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage=ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','PC端补丁收集应用')
        businessPage=BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('外键不为空表单列表')
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage=FormPage(self.driver)
        self.assertFalse(formPage.Form_field_isVisibility("单行文本"))
        formPage.ForeignSelection_Sendkeys("外键选择1","无")
        time.sleep(2)
        self.assertFalse(formPage.Form_field_isVisibility("单行文本"))
        formPage.ForeignSelection_Sendkeys("外键选择1","吴健伦")
        time.sleep(2)
        self.assertTrue(formPage.Form_field_isVisibility("单行文本"))

    def test_07( self ):
        '''【补丁】---PC运行平台-导入文件报系统异常'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage=PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage=ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','资产管理')
        businessPage=BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('资产清单测试导入列表')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除数据')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        businessPage.ListComponent_Click_ListHeader_Button('导入')
        businessPage.ListComponent_Import_Data(self.assetsDataPath)
        time.sleep(2)
        self.assertEqual(6,businessPage.ListComponent_GetRecordTotal())

    def test_08( self ):
        '''【补丁】---PC运行平台-导入文件报系统异常'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage=PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage=ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','固定资产管理3.0')
        businessPage=BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('基础管理')
        businessPage.BusinessPage_LeftMenu_Click('资产管理复制表单列表')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        businessPage.ListComponent_Click_ListHeader_Button('导入')
        businessPage.ListComponent_Import_Data(self.assets3DataPath)
        time.sleep(2)
        self.assertEqual(16,businessPage.ListComponent_GetRecordTotal())


    def test_09( self ):
        '''【补丁】---组合页面并排放置两个列表组件时，重叠'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage=PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage=ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','数据过滤测试应用')
        businessPage=BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('组合页面')
        self.assertEqual(330,businessPage.ListComponent_GetRecordTotal_ICP("key_1588733496950_296746"))

    def test_10(self):
        '''【ID1101604】
【补丁】---用户所属一级部门人员返回数据错误'''
        self.pcLogin("wujianlun@auto", "do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '道一云价值观')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('同一级部门人员价值观明细')
        self.assertEqual(3,businessPage.ListComponent_GetRecordTotal())

    def test_11( self ):
        '''PC外部表单添加数据'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        self.driver.get("https://qy.do1.com.cn/qiqiao/runtime/#/2ade557c80d0430d9eee7589b30e4447/2ade0/e8e7124ff51846118f602b349a1a243a/5fdafd1bee96fe000143c54d/externalForm")
        externalformpage = ExternalFormPage(self.driver)
        externalformpage.ExternalFormPage_Click_SubmitBtn()
        self.assertEqual("提交成功！",externalformpage.ExternalFormPage_Get_MessageContent())


    def test_12( self ):
        '''【补丁】---导入按钮导入数据时找不到部门'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage=PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage=ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','PC端补丁收集应用')
        businessPage=BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('人员部门导入')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        businessPage.ListComponent_Click_ListHeader_Button('导入')
        businessPage.ListComponent_Import_Data(self.assets4DataPath)
        time.sleep(4)
        self.assertEqual(2,businessPage.ListComponent_GetRecordTotal())

    def test_13( self ):
        '''【补丁】---选项卡统计列表数据不正确'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage=PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage=ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','PC端补丁收集应用')
        businessPage=BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('选项卡多个选项')
        self.assertEqual(['全部(12)', '选项一(1)', '选项二(1)', '选项三(1)', '选项四(1)', '选项五(1)', '选项六(1)', '选项七(1)', '选项八(1)', '选项九(1)', '选项十(1)', '选项十一(1)', '选项十二(1)'],businessPage.ListComponent_get_tablistValule())


