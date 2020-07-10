# coding=utf-8
# coding=utf-8
#应用列表页面
import time

from public.selenium_page import SeleniumPage


class MbApplicationListPage(SeleniumPage):
    '''应用列表页面'''


    menu_loc = "//span[contains(text(),'%appName')]/ancestor::div[@class='apply_content_top']/following-sibling::div[@class='apply_content_bottom']//li[@title='%menu']//i"

    bottom_nav = "//span[contains(@class,'menu_label') and text()='%s']"


    def MbApplicationListPage_BottomNav_Click( self ,buttonName):
        '''首页底部导航菜单点击'''
        self.clickElemByXpath_visibility(self.bottom_nav.replace('%s',buttonName))


    def MbApplicationListPage_Menu_Click(self,appName,menu,*args):
        '''点击应用菜单
        '''
        self.clickElemByXpath_visibility (
            self.menu_loc.replace ('%appName', appName).replace ('%menu', menu))
        time.sleep(2)





