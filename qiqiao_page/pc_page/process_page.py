# coding=utf-8
from public.selenium_page import SeleniumPage


class ProcessPage(SeleniumPage):
    '''工作台页面'''

    process_icon_loc = "//p[@title='%title']/preceding-sibling::div[1]"

    #发起流程列表

    def click_process_icon( self,title ):
        '''点击流程图标，发起流程'''
        self.clickElemByXpath_Presence(self.process_icon_loc.replace('%title',title))