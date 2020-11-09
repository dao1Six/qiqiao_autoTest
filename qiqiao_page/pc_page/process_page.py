# coding=utf-8
from Enum.fileTypeEnum import FileTypeEnum
from public.selenium_page import SeleniumPage
from qiqiao_page.pc_page.public_page import PublicPage


class ProcessPage(PublicPage,SeleniumPage):
    '''流程列表页面'''

    process_icon_loc = "//p[@title='%title']/preceding-sibling::div[1]"

    process_menu = "//aside//li[contains(@class,'el-menu-item')]//span[text()='%s']"

    record = "//table[@class='el-table__body']//tr[@class='el-table__row']"

    processTd = "//tbody//tr[%r]//td[%d]/div"

    processCenter_search_input_loc = "//div[@class='processCenter_search']//label[starts-with(text(),'%s')]/following-sibling::div//input"

    processCenter_search_button_loc = "//div[@class='processCenter_panel']//span[text()='%s']/parent::button"
    #流程页面


    def ProcessPage_click_process_menu( self,menu ):
        '''点击流程页面左侧菜单'''
        self.clickElemByXpath_visibility(self.process_menu.replace('%s',menu))


    # 发起流程页面
    def ProcessPage_click_process_icon( self,title ):
        '''点击流程图标，发起流程'''
        self.clickElemByXpath_visibility(self.process_icon_loc.replace('%title',title))



    def ProcessPage_click_process_record( self,index ):
        '''打开流程记录'''
        self.clickElemByXpath_visibility(self.record,index=index-1)

    def ProcessPage_get_processTdValue( self,r,d ):
        '''获取流程列表单元格值'''
        return self.find_elemsByXPATH_presence(self.processTd.replace('%r',str(r)).replace('%d',str(d+1)))[0].text


    def ProcessPage_searchItem_sendkeys( self,lableName,key,FileType):
        '''流程列表搜索框输入值'''
        if(FileType==FileTypeEnum.Text):
            self.sendkeysElemByXpath_visibility(self.processCenter_search_input_loc.replace('%s',lableName),key)
        else:
            raise TypeError('无此字段类型')


    def ProcessPage_searchButton_Click( self,buttonName):
        '''流程列表搜索框输入值'''
        self.clickElemByXpath_visibility(self.processCenter_search_button_loc.replace('%s',buttonName))

    def ProcessPage_IsIn( self):
        '''是否在流程列表页面'''
        if(self.find_elemByXPATH_visibility(self.process_menu.replace('%s','发起流程'))==None):
            return False
        else:
            return True

