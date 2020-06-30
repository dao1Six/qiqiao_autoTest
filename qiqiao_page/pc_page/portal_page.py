
# 工作台页面

from public.selenium_page import SeleniumPage


class PortalPage(SeleniumPage):
    '''工作台页面'''

    #Action
    PortalPage_headerMenu_loc = "//a[contains(@class,'header_menu_title')and contains(@data-mark,'%menu')]"  #工作台顶部菜单栏菜单

    userName_loc = "span.userName"

    def get_loginUser_name( self ):
        '''获取当前登录用户名'''
        return self.find_elenmInElemsByCSS(self.userName_loc).text


    def click_header_menu(self,menu,*args):
        '''点击工作台头部菜单
        menu：菜单名
        '''
        self.clickElemByXpath_visibility(self.PortalPage_headerMenu_loc.replace('%menu',menu))

    def qiqiao_logout( self ):
        '''退出登录'''






    #进入应用页面


    #获取常用应用数


    #获取常用流程数


    #获取