# coding=utf-8
from public.selenium_page import SeleniumPage
from qiqiao_page.console_page.header_page import HeaderPage


class AppManagePage(HeaderPage):
    """开发平台应用管理页面"""

    tab_0 = "//div[@class='el-tabs__nav-wrap is-top']//div[@id='tab-0']/span"

    appItem = "//div[@class='newApplication_item']//p[@title='%s']"

    def AppManagePage_get_appNumber( self ):
        '''获取应用数'''
        text = self.find_elenmInElemsByXpath_presence_of_all_elements_located(self.tab_0,timeout=5).text
        number = list(text.split("(")[1])[0]
        return int(number)

    def AppManagePage_getAppItemLoc( self,appName):
        return self.find_elenmInElemsByXpath_presence_of_all_elements_located(self.appItem.replace('%s',appName))




