# coding=utf-8
from public.selenium_page import SeleniumPage


class MbTextComponent(SeleniumPage):


    Text_loc = "div.dyText span"

    #获取文本值
    def GetTextValue( self ):
        return self.find_elenmInElemsByCSS_visibility_of_any_elements_located(self.Text_loc).text