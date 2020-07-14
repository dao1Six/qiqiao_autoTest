#人员组件
import time

from public.selenium_page import SeleniumPage


class MbUser(SeleniumPage):


    peopleListName_loc = "div[title='%s'] span.peopleList_name"

    icon_add_new_loc = "//div[@title='%s']//div[@class='icon_add_new']"
    structSelector_searchBar = "//div[@class='structSelector_searchBar']"
    searchInput_loc = "//div[@class='structSelector_main_active']/input"
    searchResult_loc = "//div[@class='structSelector_searchResult']//div[@class='cube-checkbox']//input"
    confirmBtn_loc = "//button[@class='cube-btn fr confirmBtn cube-btn-inline cube-btn-primary']"
    #获取表单人员组件的值
    def GetUserValue( self,fieldName):
        elem = self.find_elenmInElemsByCSS_visibility_of_any_elements_located(self.peopleListName_loc.replace('%s',fieldName))
        value = elem.text
        return value

    def MbUser_MonomialUser_Sendkeys(self,fieldName,userName):
        '''给人员单选组件输入值
        fieldName：字段标题
        userName：人员名称
        '''
        #点击添加选择框
        self.clickElemByXpath_visibility(self.icon_add_new_loc.replace('%s',fieldName))
        #点击搜索框
        self.clickElemByXpath_visibility(self.structSelector_searchBar)
        #输入搜索人
        self.sendkeysElemByXpath_visibility(self.searchInput_loc,userName)
        #点击查询结果
        self.clickElemByXpath_visibility(self.searchResult_loc)
        #点击确定按钮
        self.clickElemByXpath_visibility(self.confirmBtn_loc)

