# coding=utf-8
import time
import unittest

from ddt import ddt,data,unpack

from public.driver import Driver
from qiqiao_page.mobile_page.business_components.mb_list_component import MbListComponent
from qiqiao_page.mobile_page.mb_business_page import MbBusinessPage
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

@ddt
class MbValueAppTest_001(unittest.TestCase):
    """移动端道一云价值观应用数据显示及数据过滤检查"""




    @data(("diaohuiyun@auto",3,"第二季度",['部门：技术委员会', '人员：李嘉诚', '总分：--']),
         ("wanghao@auto",2,"第二季度",['部门：创新技术中心->产品研发二部->研发二组', '人员：庄荣填', '总分：0']),
         ("luolinyue@auto",1,"第一季度",['部门：创新技术中心->产品研发二部->产品规划组', '人员：王栋一', '总分：100']))
    @unpack
    def test_01( self,account,result,result2,result3):
        """移动端部门价值观数据检查"""
        self.driver = Driver().phonedriver()
        self.driver.maximize_window()
        loginpage = MbLoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/mruntime', account,"do1qiqiao")
        time.sleep(3)
        homepage = MbHomePage(self.driver)
        homepage.HomePage_BottomNav_Click('应用')
        applicationListPage = MbApplicationListPage(self.driver)
        applicationListPage.MbApplicationListPage_Menu_Click('道一云价值观','应用首页')
        mbBusinessPage = MbBusinessPage(self.driver)
        #点击底部菜单更多
        mbBusinessPage.MbBottomMenuComponent_Click("更多")
        #点击导航部门价值观
        mbBusinessPage.MbNavigationComponent_Click_Navigation("部门价值观")
        #校验部门记录数
        self.assertEqual(mbBusinessPage.MbListComponent_Get_RecoresNumber(),result)
        #检查记录状态值
        self.assertEqual(mbBusinessPage.MbListComponent_Get_RecoreStatusValule(1),result2)
        #检查记录文本值
        self.assertEqual(mbBusinessPage.MbListComponent_Get_RecoreTextContents(1),result3)
