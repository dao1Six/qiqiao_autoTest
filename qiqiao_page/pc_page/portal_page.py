
# 工作台页面

from public.selenium_page import SeleniumPage
from qiqiao_page.pc_page.public_page import PublicPage


class PortalPage(PublicPage,SeleniumPage):
    '''工作台页面'''

    #Action
    PortalPage_headerMenu_loc = "//a[contains(@class,'header_menu_title')and contains(@data-mark,'%menu')]"  #工作台顶部菜单栏菜单

    userName_loc = "span.userName"

    logout_loc = "//li[@role='menuitem' and contains(text(),'退出')]"

    def PortalPage_GetLoginUserName( self ):
        '''获取当前登录用户名'''
        return self.find_elenmInElemsByCSS_visibility_of_any_elements_located(self.userName_loc).text


    def PortalPage_Click_HeaderMenu(self,menu,*args):
        '''点击工作台头部菜单
        menu：菜单名
        '''
        self.clickElemByXpath_visibility(self.PortalPage_headerMenu_loc.replace('%menu',menu))

    def PortalPage_qiqiao_logout( self ):
        '''退出登录'''
        #鼠标悬停在头像位置
        elem = self.find_elenmInElemsByCSS_visibility_of_any_elements_located(self.userName_loc)
        self.move_to_element(elem)
        #等待退出选项可见点击退出
        self.clickElemByXpath_visibility(self.logout_loc)






    #进入应用页面


    #获取常用应用数


    #获取常用流程数


    #获取