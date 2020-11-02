# coding=utf-8
import time
import unittest

from public.driver import Driver
from qiqiao_page.mobile_page.business_components.mb_list_component import MbListComponent
from qiqiao_page.mobile_page.business_components.mb_navigation_component import MbNavigationComponent
from qiqiao_page.mobile_page.mb_form_page import MbFormPage
from qiqiao_page.mobile_page.mobile_application_page import MbApplicationListPage
from qiqiao_page.mobile_page.mobile_home_page import MbHomePage
from qiqiao_page.mobile_page.mobile_login_page import MbLoginPage
from qiqiao_page.mobile_page.mobile_to_do_page import MbTodoPage
from qiqiao_page.pc_page.applicationList_page import ApplicationListPage
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.form_page import FormPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.portal_page import PortalPage
from util.dateTimeUtil import DateTimeUtil


class MbBugAppTest_001(unittest.TestCase):
    '''移动端过往补丁'''




    def mbLogin(self,account,password):
        '''登录移动端'''
        self.driver = Driver().phonedriver()
        loginpage = MbLoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/mruntime', account, password)
        time.sleep(3)

    def pcLogin(self,account,password):
        '''登录pc端'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', account, password)
        time.sleep(3)

    def test_01( self ):
        '''【补丁】移动端运行平台，分组可见条件无效'''
        self.mbLogin("wujianlun@auto","do1qiqiao")
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('外键数据升级','分组可见')
        listPage = MbListComponent(self.driver)
        listPage.MbListComponent_AddButton_Click()
        formPage = MbFormPage(self.driver)
        formPage.MbSelection_SingleBox_Senkeys("单项选择","选项一")
        self.assertTrue(formPage.MbText_IsVisible("单行文本"))
        formPage.MbSelection_SingleBox_Senkeys("单项选择","选项二")
        time.sleep(1)
        self.assertFalse(formPage.MbText_IsVisible("单行文本"))
        self.assertTrue(formPage.MbNumber_IsVisible("数字"))


    def test_02( self ):
        '''【补丁】移动端运行平台，在组织架构顶部搜索选择人员时，部门选择连带写入无效'''
        self.mbLogin("wujianlun@auto","do1qiqiao")
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('外键数据升级','分组可见')
        self.driver.refresh()
        time.sleep(1)
        listPage = MbListComponent(self.driver)
        listPage.MbListComponent_AddButton_Click()
        formPage = MbFormPage(self.driver)
        formPage.MbUser_MonomialUser_Sendkeys("人员单选","吴健伦")
        time.sleep(1)
        self.assertEqual(formPage.MbDept_MonomialDept_GetValue("部门单选"),'创新技术中心->产品研发二部->产品规划组产品规划组')


    def test_03( self ):
        '''【补丁】移动端运行平台-列表第一个选项卡的显示多少页。第二个选项卡最多也就显示那么多页。导致第二个选项卡数据有可能显示不全'''
        self.mbLogin("wujianlun@auto","do1qiqiao")
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('小蜜蜂','应用首页')
        self.driver.refresh()
        time.sleep(1)
        Navigation = MbNavigationComponent(self.driver)
        Navigation.MbNavigationComponent_Click_Navigation("委外项目")
        listPage = MbListComponent(self.driver)
        listPage.MbListComponent_SwitchTab("已完成")
        listPage.MbListComponent_Scroll_To_Bottom()
        time.sleep(2)
        self.assertEqual(31,listPage.MbListComponent_Get_RecoresNumber(),msg="列表数据显示不全")




    def test_04( self ):
        '''人员信息连带写入'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','PC端补丁收集应用')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('人员部门连带写入')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        self.driver.quit()
        self.mbLogin("wujianlun@auto","do1qiqiao")
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('PC端补丁收集应用','人员部门连带写入')
        listPage = MbListComponent(self.driver)
        listPage.MbListComponent_AddButton_Click()
        formPage = MbFormPage(self.driver)
        formPage.MbForm_Button_Click("提交")
        self.assertIn('成功',formPage.Public_GetAlertMessage())
        self.assertEqual(['部门单选：创新技术中心->产品研发二部->产品规划组', '工号：01783', '账号：wujianlun', '手机号：13025805485'],listPage.MbListComponent_Get_RecoreTextContents(1))


    def test_05( self ):
        '''【补丁】移动端运行平台--多表关联组件--关联表单行文本字段传递配置仅展示，在编辑表单时不显示值【部门、单项选择、数字】也不显示'''
        self.mbLogin("wujianlun@auto","do1qiqiao")
        homePage = MbHomePage(self.driver)
        homePage.HomePage_BottomNav_Click("待办")
        # 发起流程
        todoPage = MbTodoPage(self.driver)
        todoPage.MbTodoPage_Faqiliucheng('绩效','绩效考核申请')
        time.sleep(2)
        self.driver.refresh()
        formPage = MbFormPage(self.driver)
        time.sleep(2)
        formPage.MbMultiForm_AddButton_Click("考核明细")
        formPage.MbMultiForm_BathManagePage_Record_Tick("考核明细",[1])
        formPage.MbMultiForm_BathManagePage_Button_Cick("考核明细","确定选择")
        time.sleep(1)
        #检查多表关联组件数据列表显示
        self.assertEqual("七巧",formPage.MbMultiForm_GetTdValue("考核明细",1,2),msg="用品明细用品名称显示不正确")
        self.assertEqual("创新技术中心->产品研发二部->产品规划组",formPage.MbMultiForm_GetTdValue("考核明细",1,3),msg="用品明细类别显示不正确")
        self.assertEqual("KPI指标",formPage.MbMultiForm_GetTdValue("考核明细",1,4),msg="用品明细库存显示不正确")
        self.assertEqual("50",formPage.MbMultiForm_GetTdValue("考核明细",1,5),msg="用品明细单位显示不正确")
        self.assertEqual("七巧",formPage.MbMultiForm_GetTdValue("考核明细",1,6),msg="用品明细申请数量显示不正确")
        #点击多表关联组件编辑按钮
        formPage.MbMultiForm_edit_Record("考核明细",1)
        time.sleep(2)
        #检查表单弹窗内的数据显示
        self.assertEqual("七巧",formPage.MbForeignSelection_GetValue_readOnly_InPopup("考核项目"),msg="考核项目显示不正确")
        self.assertEqual("KPI指标",formPage.MbSelection_SingleBox_readOnly_InPopup("类型"),msg="用品明细类别显示不正确")
        self.assertEqual("50",formPage.MbNumber_GetValue_readOnly("分值权重(%)"),msg="用品明细库存显示不正确")
        self.assertEqual("七巧",formPage.MbText_GetValue_readOnly("项目名称"),msg="用品明细单位显示不正确")
        self.assertEqual("创新技术中心->产品研发二部->产品规划组",formPage.MbDept_GetValue_readOnly_InPopup("承担部门"))


    def test_06( self ):
        '''【补丁】移动端/PC版企业微信--数字组件小数类型设置数值限制校验为（0-2.5），移动端与PC版企业微信端输入2.3时，显示了校验信息'''
        self.mbLogin("wujianlun@auto","do1qiqiao")
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('补丁转自动化应用','数字组件测试列表')
        listPage = MbListComponent(self.driver)
        self.driver.refresh()
        time.sleep(1)
        listPage.MbListComponent_AddButton_Click()
        formPage = MbFormPage(self.driver)
        formPage.MbNumber_Sendkeys("数字",2.3)
        formPage.MbForm_Button_Click("提交")
        self.assertIn('成功',formPage.Public_GetAlertMessage())

    def test_07( self ):
        '''【补丁】——数字组件sum函数，计算结果数值过大（上亿），提交数据之后，结果失真（1787222333765623.69变为1787222333760000）'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','费用管理测试版')
        businessPage = BusinessPage(self.driver)
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        self.driver.quit()
        self.mbLogin("wujianlun@auto","do1qiqiao")
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('费用管理测试版','888')
        listPage = MbListComponent(self.driver)
        self.driver.refresh()
        time.sleep(1)
        listPage.MbListComponent_AddButton_Click()
        formPage = MbFormPage(self.driver)
        formPage.MbChildForm_AddButton_Click("费用报销明细")
        formPage.MbNumber_Sendkeys("费用金额",1234567891230.34)
        formPage.MbChildForm_Button_Click("保存并继续添加")
        time.sleep(1)
        formPage.MbNumber_Sendkeys("费用金额",1234567891230.34)
        formPage.MbChildForm_Button_Click("保存")
        time.sleep(1)
        self.assertEqual(2469135782460.68,formPage.MbNumber_GetValue_formula("费用总额"),msg="费用总额计算错误")
        formPage.MbForm_Button_Click("提交")
        self.assertEqual(['费用总额：2469135782460.68'],listPage.MbListComponent_Get_RecoreTextContents(1),msg="费用总额列表显示错误")

    def test_08( self ):
        '''【补丁】——外键选择组件设置可用条件为高级函数OR，对另外外键字段值进行判断时不生效'''
        self.mbLogin("wujianlun@auto","do1qiqiao")
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('美安居建材云办公系统','生产任务单明细')
        listPage = MbListComponent(self.driver)
        self.driver.refresh()
        time.sleep(1)
        listPage.MbListComponent_AddButton_Click()
        formPage = MbFormPage(self.driver)
        formPage.MbForeignSelection_Sendkeys("生产机组","生产机组甲")
        self.assertTrue(formPage.MbForm_field_isVisibility("袋装重量"))


    def test_09( self ):
        '''【补丁】——外键选择组件配置关联筛选字段为外键选择时，填写数据之后，关联选项重复'''
        self.mbLogin("wujianlun@auto","do1qiqiao")
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('美安居建材云办公系统','砂浆型号登记表')
        listPage = MbListComponent(self.driver)
        self.driver.refresh()
        time.sleep(1)
        listPage.MbListComponent_AddButton_Click()
        formPage = MbFormPage(self.driver)
        formPage.MbForeignSelection_SelectionBox_Click("砂浆品种")
        time.sleep(1)
        formPage.MbForeignSelection_Option_scrollDown()
        time.sleep(2)
        foreignList = formPage.MbForeignSelection_get_OptionValue("砂浆品种")
        foreignSet = set(foreignList)
        self.assertEqual(len(foreignList),len(foreignSet),msg="【补丁】——外键选择组件配置关联筛选字段为外键选择时，填写数据之后，关联选项重复")
        self.assertEqual(len(foreignSet),26,msg="外键选项数目显示不对")


    def test_10( self ):
        '''【正式环境】在待办搜索数据无效（输入框无法输入文字）'''
        self.mbLogin("wujianlun@auto","do1qiqiao")
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('待办')
        time.sleep(2)
        self.driver.refresh()
        todoPage = MbTodoPage(self.driver)
        todoPage.MbTodoPage_searchInput_sendkeys("王浩")
        time.sleep(2)
        self.assertIn("王浩",todoPage.MbTodoPage_Get_RecoreTitleValule(1))


    def test_11( self ):
        '''移动端详情页面页面内操作按钮检查'''
        self.mbLogin("wujianlun@auto","do1qiqiao")
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('数据过滤测试应用','列表数据过滤组')
        listPage = MbListComponent(self.driver)
        self.driver.refresh()
        time.sleep(1)
        listPage.MbListComponent_Recore_Click(1)
        formPage = MbFormPage(self.driver)
        self.assertEqual(['添加', '编辑', '删除'],formPage.MbForm_Get_buttonGroup(),msg="移动端详情页面页面内操作显示不正确")

