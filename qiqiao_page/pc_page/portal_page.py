
# 工作台页面

from public.selenium_page import SeleniumPage


class PortalPage(SeleniumPage):
    '''工作台页面'''

    #Action
    PortalPage_headerMenu_loc = "//a[@class='header_menu_title' and text()='%menu']"  #工作台顶部菜单栏菜单


    def click_header_menu(self,menu,*args):
        '''点击工作台头部菜单
        menu：菜单名
        '''
        self.clickElemByXpath_Presence(self.PortalPage_headerMenu_loc.replace('%menu',menu))



    #进入应用页面


    #获取常用应用数


    #获取常用流程数


    #获取