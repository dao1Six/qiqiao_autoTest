# coding=utf-8
import time
import unittest


from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.portal_page import PortalPage
from qiqiao_page.pc_page.applicationList_page import ApplicationListPage


class JinXiaoCun(unittest.TestCase):

    def setUp(self):
        self.driver = pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage (self.driver)
        loginpage.user_login ('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@auto", "do1qiqiao")
        self.driver.get("https://qy.do1.com.cn/qiqiao/runtime/?corp_id=ww6b6c5c4fa6f34b16#/application/business?applicationId=d07cc4755a6b4dad97aa5ced0d60c70d&businessModelId=b8e072d41c8c4fc3a2787d461c7d9756")
        # portalpage = PortalPage (self.driver)
        # portalpage.click_header_menu ("应用")
        # applicationListPage = ApplicationListPage(self.driver)
        # time.sleep(2)
        # applicationListPage.click_application("全员报平安2.2")


    def tearDown(self):
        self.driver.quit()


    def test_add_record(self):
        '''应用管理员录入商品信息开发哈哈哈哈'''


        time.sleep(9)


if __name__=="__main__":
    unittest.main()


