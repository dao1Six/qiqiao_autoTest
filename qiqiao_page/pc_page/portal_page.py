
# 工作台页面

from public.selenium_page import SeleniumPage
from qiqiao_page.pc_page.public_page import PublicPage


class PortalPage(PublicPage):
    """工作台页面"""

    #Action
    PortalPage_headerMenu_loc = "//a[contains(@class,'header_menu_title')and contains(@data-mark,'%menu')]/parent::div"  #工作台顶部菜单栏菜单

    userName_loc = "span.userName"

    logout_loc = "//li[@role='menuitem' and contains(text(),'退出')]"

    commonApplications_loc = "//div[@class='el-card component_commonApplication is-never-shadow']//li[contains(@class,'commonList five')]//p[@class='listName']"

    commonProcess_loc = "//div[@class='el-card component_commonProcess is-never-shadow']//li[contains(@class,'commonList processList five')]//p[@class='listName']"

    commonApplication_btn_more_loc = "//div[@class='el-card component_commonApplication is-never-shadow']//a[@class='btn_more']"

    component_commonProcess_btn_more_loc = "//div[@class='el-card component_commonProcess is-never-shadow']//a[@class='btn_more']"

    def PortalPage_Click_commonAppBtnMore(self,*args):
        """点击常用应用更多按钮"""
        self.clickElemByXpath_clickable(self.commonApplication_btn_more_loc)


    def PortalPage_Click_commonProcessBtnMore(self,*args):
        """点击常用流程更多按钮"""
        self.clickElemByXpath_clickable(self.component_commonProcess_btn_more_loc)

    def PortalPage_GetLoginUserName( self ):
        """获取当前登录用户名"""
        return self.find_elenmInElemsByCSS_visibility_of_any_elements_located(self.userName_loc).text


    def PortalPage_Click_HeaderMenu(self,menu,*args):
        """点击工作台头部菜单
        menu：菜单名
        """
        self.clickElemByXpath_clickable(self.PortalPage_headerMenu_loc.replace('%menu',menu))

    def PortalPage_qiqiao_logout( self ):
        """退出登录"""
        #鼠标悬停在头像位置
        elem = self.find_elenmInElemsByCSS_visibility_of_any_elements_located(self.userName_loc)
        self.move_to_element(elem)
        #等待退出选项可见点击退出
        self.clickElemByXpath_visibility(self.logout_loc)


    def PortalPage_get_commonApplicationList( self ):
        '''工作台获取常用应用列表'''
        commonApplicationList = []
        commonApplications = self.find_elemsByXPATH_visibility(self.commonApplications_loc)
        for commonApplication in commonApplications:
            commonApplicationList.append(self.getElemAttrValue(commonApplication,"title"))
        return commonApplicationList


    def PortalPage_get_commonProcessList( self ):
        '''工作台获取常用流程列表'''
        commonProcessList = []
        commonProcess = self.find_elemsByXPATH_visibility(self.commonProcess_loc)
        for commonP in commonProcess:
            commonProcessList.append(self.getElemAttrValue(commonP,"title"))
        return commonProcessList






    #进入应用页面


    #获取常用应用数


    #获取常用流程数


    #获取