# coding=utf-8
from public.selenium_page import SeleniumPage

#导航组件
class MbNavigationComponent(SeleniumPage):
    '''导航组件'''

    dyListNavigation_item_title = "div.dyListNavigation_container ul li span.item_title"

    dyListNavigation_item = "//div[@class='item_title_container']/span[contains(text(),'%s')]"


    #获取页面导航名
    def MbNavigationComponent_Get_NavigationsName( self ):
        NavigationsNameList = []
        for elem in self.find_elemsByCSS_presence(self.dyListNavigation_item_title):
            NavigationsNameList.append(elem.text)
        return NavigationsNameList

    #点击页面导航图标
    def MbNavigationComponent_Click_Navigation( self,item_title):
        self.clickElemByXpath_visibility(self.dyListNavigation_item.replace('%s', item_title))

