# coding=utf-8
#应用列表页面

from public.selenium_page import SeleniumPage


class ApplicationListPage(SeleniumPage):
    '''应用列表页面'''

    ApplicationListPage_application_loc = "//div[@data-mark='%groupName']//div[@data-mark='%applicationName']/i"  #应用管理页面应用卡片

    ApplicationListPage_searchInput_loc = "[data-mark=应用名称搜索框]"

    openAppGroupLoc = "//span[@class='card_title card_title_blue1']"
    openself = "//p[@title='{appname}']/.."



    def ApplicationListPage_ClickApplicationIcon(self,groupName,title,*args):
        '''点击分组里的应用
        groupName:分组名
        title:应用名称
        '''
        self.clickElemByXpath_visibility (
            self.ApplicationListPage_application_loc.replace ('%groupName', groupName).replace ('%applicationName', title))





