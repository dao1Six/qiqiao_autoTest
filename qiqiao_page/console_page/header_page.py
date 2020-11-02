# coding=utf-8
import time

from public.selenium_page import SeleniumPage


class HeaderPage(SeleniumPage):
    """开发平台头部页面"""

    header_topbar_span_loc = "//div[@class='header_topbar']//span[text()='%s']"

    appItem = "//div[@class='newApplication_item']//p[@title='%s']"

    imgUserAvatar = "//div[@class='header_topbar']//img[@class='imgUserAvatar mini']"
    header_user_info = "//div[@class='header_user_info']//div"

    def HeaderPage_topbar_click( self,topbarName ):
        '''点击topbar'''
        self.clickElemByXpath_visibility(self.header_topbar_span_loc.replace('%s',topbarName))


    def HeaderPage_get_userInfo( self ):
        '''开发平台获取租户信息'''
        self.HeaderPage_move_to_imgUserAvatar()
        time.sleep(1)
        valus = []
        spans = self.find_elemsByXPATH_visibility(self.header_user_info)
        for span in spans:
            valus.append(span.text)
        return valus


    def HeaderPage_move_to_imgUserAvatar( self ):
        '''悬浮在租户头像上'''
        elem = self.find_elemByXPATH_visibility(self.imgUserAvatar)
        self.move_to_element(elem)





