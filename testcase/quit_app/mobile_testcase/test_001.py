# coding=utf-8
import time
import unittest

from public.driver import Driver
from qiqiao_page.mobile_page.mb_business_page import MbBusinessPage
from qiqiao_page.mobile_page.mb_form_page import MbFormPage
from qiqiao_page.mobile_page.mobile_application_page import MbApplicationListPage
from qiqiao_page.mobile_page.mobile_home_page import MbHomePage
from qiqiao_page.mobile_page.mobile_login_page import MbLoginPage
from qiqiao_page.mobile_page.mobile_to_do_page import MbTodoPage



class QuitAppTest_001(unittest.TestCase):
    '''移动端离职人员测试应用检查'''

    def mbLogin(self,account,password):
        '''登录移动端'''
        self.driver = Driver().phonedriver()
        self.driver.maximize_window()
        loginpage = MbLoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/mruntime', account, password)


    def test_01( self ):
        '''检查流程处理人为离职人员时，是否仍然显示'''
        self.mbLogin("wujianlun@A1","qiqiao123")
        homePage = MbHomePage(self.driver)
        homePage.HomePage_BottomNav_Click("待办")
        time.sleep(1)
        self.driver.refresh()
        time.sleep(2)
        #发起流程
        todoPage = MbTodoPage(self.driver)
        todoPage.MbTodoPage_Faqiliucheng('离职人员测试应用','离职人员测试流程')
        formPage = MbFormPage(self.driver)
        formPage.MbText_Sendkeys("单行文本","用户")
        time.sleep(1)
        formPage.MbForm_Button_Click("办理")
        self.assertEqual(formPage.MbForm_Get_ProcessManagers(),["吴健伦"],msg="固定用户人工任务办理者错误")


    def test_02( self ):
        '''检查离职人员列表人员单选查询是否正常'''
        self.mbLogin("wujianlun@A1","qiqiao123")
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('离职人员测试应用','列表数据过滤组')
        mbBusinessPage = MbBusinessPage(self.driver)
        self.assertEqual(mbBusinessPage.MbListComponent_ItemP_Get(1,1),"人员单选：刘言",msg="列表创建人显示离职人员不正确")
        self.assertEqual(mbBusinessPage.MbListComponent_ItemP_Get(1,3),"创建人：刘言",msg="列表创建人显示离职人员不正确")
        self.assertEqual(mbBusinessPage.MbListComponent_ItemP_Get(1,4),"人员多选：刘言,王浩",msg="列表创建人显示离职人员不正确")
        mbBusinessPage.MbListComponent_shaixuanIcoon_Click()
        mbBusinessPage.MbListComponent_QueryItem_Sendkeys("人员单选","刘言",QueryItemType='user')
        mbBusinessPage.MbListComponent_FilterButton_Click("确定")
        time.sleep(3)
        self.assertEqual(mbBusinessPage.MbListComponent_Get_RecoresNumber(),2)


    def test_03( self ):
        '''检查离职人员列表人员多选查询是否正常'''
        self.mbLogin("wujianlun@A1","qiqiao123")
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('离职人员测试应用','列表数据过滤组')
        mbBusinessPage = MbBusinessPage(self.driver)
        mbBusinessPage.MbListComponent_shaixuanIcoon_Click()
        mbBusinessPage.MbListComponent_QueryItem_Sendkeys("人员多选","刘言",QueryItemType='user')
        mbBusinessPage.MbListComponent_FilterButton_Click("确定")
        time.sleep(3)
        self.assertEqual(mbBusinessPage.MbListComponent_Get_RecoresNumber(),2)


    def test_04( self ):
        '''检查离职人员在表单详情中显示是否正确'''
        self.mbLogin("wujianlun@A1","qiqiao123")
        time.sleep(1)
        # self.driver.refresh()
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('离职人员测试应用','列表数据过滤组')
        mbBusinessPage = MbBusinessPage(self.driver)
        mbBusinessPage.MbListComponent_Recore_Click(1)
        formPage = MbFormPage(self.driver)
        formPage.MbForm_Switch_Tab("人员部门类组件")
        self.assertEqual(formPage.MbUser_GetUserValue_readOnly("人员单选"),["刘言"])
        self.assertEqual(formPage.MbUser_GetUserValue_readOnly("人员多选"),['王浩', '刘言'])


    def test_05( self ):
        '''【补丁】移动端运行平台，组织选择器，标签下绑定了部门时，运行平台标签下会显示部门名称'''
        self.mbLogin("wujianlun@A1","qiqiao123")
        time.sleep(1)
        # self.driver.refresh()
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('离职人员测试应用','列表数据过滤组')
        mbBusinessPage = MbBusinessPage(self.driver)
        #点击添加按钮
        mbBusinessPage.MbListComponent_AddButton_Click()
        formPage = MbFormPage(self.driver)
        formPage.MbForm_Switch_Tab("人员部门类组件")
        self.assertEqual(['王浩', '李嘉诚', '王栋一'],formPage.MbUser_Tag_GetUserValue('人员单选','部门加用户'))

