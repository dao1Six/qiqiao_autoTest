# coding=utf-8
from public.selenium_page import SeleniumPage


class HelpPage(SeleniumPage):
    """帮助中心页面"""

    h4_link_loc  = "//h4[@id='%s']/a[2]"

    def HelpPage_h4Link_click( self,Name ):
        '''点击H4链接'''
        self.clickElemByXpath_presence(self.h4_link_loc.replace('%s',Name))






