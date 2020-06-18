# coding=utf-8
from public.selenium_page import SeleniumPage


class ProcessPage(SeleniumPage):
    '''工作台页面'''

    process_icon_loc = "//p[@title='%title']/preceding-sibling::div[1]"

    process_menu = "//aside//li[contains(@class,'el-menu-item')]//span[text()='%s']"

    record = "//table[@class='el-table__body']//tr[@class='el-table__row']"

    #流程页面

    #切换左侧菜单
    def click_process_menu( self,menu ):
        self.clickElemByXpath_Presence(self.process_menu.replace('%s',menu))


    # 发起流程页面
    def click_process_icon( self,title ):
        '''点击流程图标，发起流程'''
        self.clickElemByXpath_Presence(self.process_icon_loc.replace('%title',title))






    #我的待办页面

    def click_process_record( self,index ):
        '''打开流程记录'''
        self.clickElemByXpath_Presence(self.record,index=index-1)


