# coding=utf-8
from public.selenium_page import SeleniumPage

#导航组件
class NavigationComponent(SeleniumPage):


    dyListNavigation_item_title = "div.dyListNavigation_container ul li span.item_title"

    def GetNavigationsName( self ):
        NavigationsNameList = []
        for elem in self.find_elemsByCSS(self.dyListNavigation_item_title):
            NavigationsNameList.append(elem.text)
        return NavigationsNameList
