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
class ValueAppTest_001(unittest.TestCase):
    '''道一云价值观应用，数据过滤及查询检查，表头筛选查询'''


    def setUp(self):
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        time.sleep(5)
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组', '道一云价值观')

    # def tearDown(self):
    #     self.driver.quit()

    @data(("第一季度",2),("第二季度",2),("第三季度",0))
    @unpack
    def test_01( self,option,result):
        '''道一云价值观 全员价值观明细,季度查询'''
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('全员价值观')
        businessPage.ListComponent_TabsOption_Click(" 全员价值观明细")
        time.sleep(5)
        businessPage.ListComponent_QueryItem_Sendkeys("季度",option,QueryItemType="option")
        businessPage.ListComponent_Click_SerachBtn()
        time.sleep(5)
        self.assertEqual(result,businessPage.ListComponent_GetRecordTotal())


    @data(("王栋一",2),("吴健伦",0))
    @unpack
    def test_02( self,option,result):
        '''道一云价值观 全员价值观明细,创建人查询'''
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('全员价值观')
        businessPage.ListComponent_TabsOption_Click(" 全员价值观明细")
        time.sleep(5)
        businessPage.ListComponent_Click_ExpandBtn()
        businessPage.ListComponent_QueryItem_Sendkeys("创建人",option,QueryItemType="user")
        businessPage.ListComponent_Click_SerachBtn()
        time.sleep(5)
        self.assertEqual(result,businessPage.ListComponent_GetRecordTotal())

    @data(("王栋一",2),("吴健伦",0))
    @unpack
    def test_03( self,option,result):
        '''道一云价值观 全员价值观明细,人员查询'''
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('全员价值观')
        businessPage.ListComponent_TabsOption_Click(" 全员价值观明细")
        time.sleep(5)
        businessPage.ListComponent_QueryItem_Sendkeys("人员",option,QueryItemType="user")
        businessPage.ListComponent_Click_SerachBtn()
        time.sleep(5)
        self.assertEqual(result,businessPage.ListComponent_GetRecordTotal())

    @data(("2020-07-01","2020-07-10",4),("2020-07-05","2020-07-10",0))
    @unpack
    def test_04( self,option1,option2,result):
        '''道一云价值观 全员价值观明细,修改时间查询'''
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('全员价值观')
        businessPage.ListComponent_TabsOption_Click(" 全员价值观明细")
        time.sleep(5)
        businessPage.ListComponent_Click_ExpandBtn()
        businessPage.ListComponent_QueryItem_Sendkeys("修改时间",option1,option2,QueryItemType="date")
        businessPage.ListComponent_Click_SerachBtn()
        time.sleep(5)
        self.assertEqual(result,businessPage.ListComponent_GetRecordTotal())


    @data(("2020",4),("2019",0))
    @unpack
    def test_05( self,option1,result):
        '''道一云价值观 全员价值观明细,年份查询'''
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('全员价值观')
        businessPage.ListComponent_TabsOption_Click(" 全员价值观明细")
        time.sleep(5)
        businessPage.ListComponent_Click_ExpandBtn()
        businessPage.ListComponent_QueryItem_Sendkeys("年度",option1,QueryItemType="datetime")
        businessPage.ListComponent_Click_SerachBtn()
        time.sleep(5)
        self.assertEqual(result,businessPage.ListComponent_GetRecordTotal())

    @data((["客户第一：必须给客户带来惊喜","持续创新：技术驱动，敏捷迭代","追求卓越：目标高远，挑战不可能"],4),
          (["客户第一：必须给客户带来惊喜", "追求卓越：目标高远，挑战不可能"],3),
          (["温情有趣：有温度，有乐趣", "团队协作：胜则举杯相庆 败则拼死相救"], 0))
    @unpack
    def test_06( self,option,result):
        '''道一云价值观 全员价值观明细,价值观查询'''
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('全员价值观')
        businessPage.ListComponent_TabsOption_Click(" 全员价值观明细")
        time.sleep(5)
        businessPage.ListComponent_QueryItem_Sendkeys("价值观",option,QueryItemType="option")
        businessPage.ListComponent_Click_SerachBtn()
        time.sleep(5)
        self.assertEqual(result,businessPage.ListComponent_GetRecordTotal())

    @data(("创新技术中心->产品研发二部->产品规划组",2),("财务管理中心",0))
    @unpack
    def test_07( self,option,result):
        '''道一云价值观 全员价值观明细,部门查询'''
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('全员价值观')
        businessPage.ListComponent_TabsOption_Click(" 全员价值观明细")
        time.sleep(5)
        businessPage.ListComponent_QueryItem_Sendkeys("部门",option,QueryItemType="user")
        businessPage.ListComponent_Click_SerachBtn()
        time.sleep(5)
        self.assertEqual(result,businessPage.ListComponent_GetRecordTotal())

    @data(("人员",1,"王栋一",0,"李嘉诚"),
          ("修改时间",1,"李嘉诚",0,"王栋一"))
    @unpack
    def test_08( self,ColName,sort1,result1,sort2,result2):
        '''道一云价值观 全员价值观表 人员列排序'''
        businessPage = BusinessPage(self.driver)
        businessPage.ListComponent_TabsOption_Click("  全员价值观")
        time.sleep(5)
        businessPage.ListComponent_ColHeader_sort(ColName,sort1)
        time.sleep(3)
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1,7),result1)
        businessPage.ListComponent_ColHeader_sort(ColName,sort2)
        time.sleep(3)
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1,7),result2)


    def test_09( self):
        '''道一云价值观 全员价值观表 季度列筛选'''
        businessPage = BusinessPage(self.driver)
        businessPage.ListComponent_TabsOption_Click("  全员价值观")
        time.sleep(5)
        #先取消全选
        businessPage.ListComponent_ColHeader_search("季度",[1])
        #选择第5，6项
        businessPage.ListComponent_ColHeader_search("季度",[5,6])
        time.sleep(3)
        self.assertIsNone(businessPage.ListComponent_GetTable_Td_Value(1,7))


