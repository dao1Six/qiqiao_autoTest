# coding=utf-8
from public.selenium_page import SeleniumPage
from qiqiao_page.mobile_page.mb_public_page import PublicPage


class MbHomePage(PublicPage,SeleniumPage):
    '''移动端首页'''

    bottom_nav = "//span[contains(@class,'menu_label') and text()='%s']"


    def HomePage_BottomNav_Click( self ,buttonName):
        '''首页底部导航菜单点击'''
        self.clickElemByXpath_visibility(self.bottom_nav.replace('%s',buttonName))