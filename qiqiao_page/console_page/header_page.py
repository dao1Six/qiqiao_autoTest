# coding=utf-8
from public.selenium_page import SeleniumPage


class HeaderPage(SeleniumPage):
    """开发平台头部页面"""

    header_topbar_span_loc = "//div[@class='header_topbar']//span[text()='%s']"

    appItem = "//div[@class='newApplication_item']//p[@title='%s']"

    def HeaderPage_topbar_click( self,topbarName ):
        '''点击topbar'''
        self.clickElemByXpath_visibility(self.header_topbar_span_loc.replace('%s',topbarName))






