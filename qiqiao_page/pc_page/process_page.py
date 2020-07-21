# coding=utf-8
from public.selenium_page import SeleniumPage
from qiqiao_page.pc_page.public_page import PublicPage


class ProcessPage(PublicPage,SeleniumPage):
    '''流程列表页面'''

    process_icon_loc = "//p[@title='%title']/preceding-sibling::div[1]"

    process_menu = "//aside//li[contains(@class,'el-menu-item')]//span[text()='%s']"

    record = "//table[@class='el-table__body']//tr[@class='el-table__row']"

    processTd = "//tbody//tr[%r]//td[%d]/div"


    #流程页面

    #切换左侧菜单
    def ProcessPage_click_process_menu( self,menu ):
        self.clickElemByXpath_visibility(self.process_menu.replace('%s',menu))


    # 发起流程页面
    def ProcessPage_click_process_icon( self,title ):
        '''点击流程图标，发起流程'''
        self.clickElemByXpath_visibility(self.process_icon_loc.replace('%title',title))



    #我的待办页面

    def ProcessPage_click_process_record( self,index ):
        '''打开流程记录'''
        self.clickElemByXpath_visibility(self.record,index=index-1)

    def ProcessPage_get_processTdValue( self,r,d ):
        '''获取流程列表单元格值'''
        return self.find_elemsByXPATH_presence(self.processTd.replace('%r',str(r)).replace('%d',str(d+1)))[0].text




