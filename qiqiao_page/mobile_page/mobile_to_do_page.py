# coding=utf-8
from public.selenium_page import SeleniumPage
from qiqiao_page.mobile_page.mb_public_page import MbPublicPage


class MbTodoPage(MbPublicPage,SeleniumPage):
    '''移动端待办列表页面'''

    bottom_nav_loc = "//span[contains(@class,'menu_label') and text()='%s']" #底部导航

    add_btn_loc = "//div[@class='add_btn']" #外部发起流程按钮

    faqiliucheng_loc = "//i[contains(@class,'faqiliucheng')]" #内部发起流程按钮

    caogao_loc = "//i[contains(@class,'caogao')]"  # 内部发起流程按钮

    process_icon_loc = "//span[text()='%app']/ancestor::div[@class='commonProcess_container_top']/following-sibling::div//div[@title='%name']"

    record = "//div[@class='item_inner']" #记录

    search_input_loc = "//div[@class='search_input']//input"  #搜索框

    item_name_loc = "//ul//div[@class='item_row']//h2[@class='item_name']"  #记录标题

    filterIcon = "//div[@class='filterSearch']//i"

    filterLi = "//h3[text()='%f']/following-sibling::ul//li[contains(text(),'%v')]"

    filterButton = "//button[text()=' %s']"

    def MbTodoPage_filterIcon_Click( self ,buttonName):
        '''点击过滤图标'''
        self.clickElemByXpath_visibility(self.filterIcon)

    def MbTodoPage_filterLi_Click( self ,filterOption,valueOption):
        '''点击过滤选项'''
        self.clickElemByXpath_visibility(self.filterLi.replace('%f',filterOption).replace('%v',valueOption))

    def MbTodoPage_filterButton_Click( self ,buttonName):
        '''点击过滤按钮'''
        self.clickElemByXpath_visibility(self.filterButton.replace('%s',buttonName))

    def MbTodoPage_BottomNav_Click( self ,buttonName):
        '''首页底部导航菜单点击'''
        self.clickElemByXpath_visibility(self.bottom_nav_loc.replace('%s',buttonName))

    def MbTodoPage_Faqiliucheng_Click( self ):
        '''待办页面发起流程'''
        #点击发起流程按钮
        self.clickElemByXpath_visibility(self.add_btn_loc)
        #点击内部发起流程按钮
        self.clickElemByXpath_visibility(self.faqiliucheng_loc)

    def MbTodoPage_Caogao_Click( self ):
        '''待办页面发起草稿'''
        #点击发起流程按钮
        self.clickElemByXpath_visibility(self.add_btn_loc)
        #点击内部发起草稿按钮
        self.clickElemByXpath_visibility(self.caogao_loc)

    def MbTodoPage_Faqiliucheng( self,app,name):
        '''待办页面发起流程'''
        self.MbTodoPage_Faqiliucheng_Click()
        self.clickElemByXpath_visibility(self.process_icon_loc.replace('%app',app).replace('%name',name))


    def MbTodoPage_ProcessRecord_Click( self,index ):
        '''打开流程记录'''
        self.clickElemByXpath_visibility(self.record,index=index-1)

    def MbTodoPage_searchInput_sendkeys( self,key ):
        '''搜索框输入值'''
        self.sendkeysElemByXpath_visibility(self.search_input_loc,key=key)

    def MbTodoPage_Get_RecoreTitleValule( self,index ):
        '''返回当前列表某条记录标题值'''
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.item_name_loc,index=index-1)
        if (elem!=None):
            return elem.text
        else:
            return None


    def MbTodoPage_Get_RecoreTextContents( self,r ):
        '''返回当前列表某条记录标题值'''
        list = []
        elems = self.find_elemsByXPATH_visibility(self.dyCardList_text_content.replace("%r",str(r-1)))
        if (elems!=None):
            for elem in elems:
                list.append(elem.text)
            return list
        else:
            return None