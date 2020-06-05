# coding=utf-8
from public.selenium_page import SeleniumPage


class BottomMenuComponent(SeleniumPage):

    dyBottomNavigation = "div.dyBottomNavigation div.dyBottomNavigation_nav div"

    dyBottomNavigation_item = "//div[@class='dyBottomNavigation']//div[text()='%s']"

    #获取底部菜单内容
    def GetBottomMenus( self ):
        BottomMenus = []
        BottomNavigationElems = self.find_elemsByCSS(self.dyBottomNavigation)
        for Elem in BottomNavigationElems:
            BottomMenus.append(Elem.text)
        return BottomMenus


    #点击某个菜单
    def ClickBottomMenu( self,title ):
        self.clickElemByXpath_Presence(self.dyBottomNavigation_item.replace('%s',title))
