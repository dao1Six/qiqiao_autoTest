# coding=utf-8
from public.selenium_page import SeleniumPage
from qiqiao_page.mobile_page.mb_public_page import PublicPage


class TodoPage(PublicPage,SeleniumPage):
    '''移动端待办列表页面'''

    bottom_nav_loc = "//span[contains(@class,'menu_label') and text()='%s']" #底部导航

    add_btn_loc = "//div[@class='add_btn']" #外部发起流程按钮

    faqiliucheng_loc = "//i[contains(@class,'faqiliucheng')]" #内部发起流程按钮

    caogao_loc = "//i[contains(@class,'caogao')]"  # 内部发起流程按钮

    process_icon_loc = "//span[text()='%app']/ancestor::div[@class='commonProcess_container_top']/following-sibling::div//div[@title='%name']"

    record = "//div[@class='item_inner']" #记录

    def TodoPage_BottomNav_Click( self ,buttonName):
        '''首页底部导航菜单点击'''
        self.clickElemByXpath_visibility(self.bottom_nav_loc.replace('%s',buttonName))

    def TodoPage_Faqiliucheng_Click( self ):
        '''待办页面发起流程'''

        #点击发起流程按钮
        self.clickElemByXpath_visibility(self.add_btn_loc)
        #点击内部发起流程按钮
        self.clickElemByXpath_visibility(self.faqiliucheng_loc)

    def TodoPage_Caogao_Click( self ):
        '''待办页面发起草稿'''
        #点击发起流程按钮
        self.clickElemByXpath_visibility(self.add_btn_loc)
        #点击内部发起草稿按钮
        self.clickElemByXpath_visibility(self.caogao_loc)

    def TodoPage_Faqiliucheng( self,app,name):
        '''待办页面发起流程'''
        self.TodoPage_Faqiliucheng_Click()
        self.clickElemByXpath_visibility(self.process_icon_loc.replace('%app',app).replace('%name',name))


    def TodoPage_ProcessRecord_Click( self,index ):
        '''打开流程记录'''
        self.clickElemByXpath_visibility(self.record,index=index-1)
