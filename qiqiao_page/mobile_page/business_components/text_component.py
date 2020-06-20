# coding=utf-8
from public.selenium_page import SeleniumPage


class TextComponent(SeleniumPage):


    Text_loc = "div.dyText span"

    #获取文本值
    def GetTextValue( self ):
        return self.find_elenmInElemsByCSS(self.Text_loc).text