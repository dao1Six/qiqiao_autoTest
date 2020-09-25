# coding=utf-8
from public.selenium_page import SeleniumPage


class MbBottomMenuComponent(SeleniumPage):
    '''底部菜单'''

    dyBottomNavigation = "div.dyBottomNavigation div.dyBottomNavigation_nav div"

    dyBottomNavigation_item = "//div[@class='dyBottomNavigation']//div[text()='%s']"

    #获取底部菜单内容
    def GetBottomMenus( self ):
        BottomMenus = []
        BottomNavigationElems = self.find_elemsByCSS_presence(self.dyBottomNavigation)
        for Elem in BottomNavigationElems:
            BottomMenus.append(Elem.text)
        return BottomMenus


    #点击某个菜单
    def MbBottomMenuComponent_Click( self,title ):
        self.clickElemByXpath_visibility(self.dyBottomNavigation_item.replace('%s',title))
