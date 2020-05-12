# coding=utf-8
import time
import unittest

from app_page.saysafe_app_page.phone.i_declare_peace_page import IDeclarePeacePage
from public.driver import Driver
from qiqiao_page.mobile_page.mobile_login_page import MobileLoginPage


class SaySafeAppTest(unittest.TestCase):

    driver = Driver().phonedriver()


    def setUp(self):
        self.driver.maximize_window()
        loginpage = MobileLoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/mruntime', "wujianlun@auto", "do1qiqiao")




    #测试添加一条报平安数据
    def test_AddSaySafeRecord( self ):
        #打开“我要报平安页面”
        self.driver.get("https://qy.do1.com.cn/qiqiao/mruntime/#/admin/business/index?businessModelId=eaba256af6474943869011eae6935535&applicationId=d07cc4755a6b4dad97aa5ced0d60c70d&key_1580314921353_88569=%7B%22navName%22%3A%22%E6%88%91%E6%8A%A5%E5%B9%B3%E5%AE%89%22%7D")
        iDeclarePeacePage = IDeclarePeacePage(self.driver)

        #点击我要报平安页面的添加按钮
        iDeclarePeacePage.clickElemByCSS_Presence(iDeclarePeacePage.addButtonLoc)


        time.sleep(5)

