#人员组件
import time

from public.selenium_page import SeleniumPage


class MbUser(SeleniumPage):


    peopleListName_loc = "div[title='%s'] span.peopleList_name"

    icon_add_new_loc = "//div[@title='%s']//div[@class='icon_add_new']"
    structSelector_searchBar = "//div[@class='structSelector_searchBar']"
    searchInput_loc = "//div[@class='structSelector_main_active']/input"
    # searchResult_loc = "//div[@class='structSelector_searchResult']//div[@class='cube-checkbox']//input"

    searchResult_loc ="//div[@class='structSelector_searchResult']//div[contains(text(),'%s')]/ancestor::label"
    confirmBtn_loc = "//button[@class='cube-btn fr confirmBtn cube-btn-inline cube-btn-primary']"

    UserValue_loc = "//div[@title='%s']//span[@class='peopleList_name']"
    structSelector_tab = "//div[@class='cube-tab-bar bg_wh structSelector_tab']//div[text()='%s']"

    structSelector_dataList_div = "//div[contains(@class,'structSelector_dataList')]//div[contains(text(),'%s')]"

    struct_name_full = "//div[contains(@class,'structSelector_dataList')]//div[@class='struct_name_full']"
    #获取表单人员组件的值
    def GetUserValue( self,fieldName):
        elem = self.find_elenmInElemsByCSS_visibility_of_any_elements_located(self.peopleListName_loc.replace('%s',fieldName))
        value = elem.text
        return value


    def MbUser_MonomialUser_Sendkeys(self,fieldName,userName):
        '''给人员单选组件输入值'''
        #fieldName：字段标题
        #userName：人员名称

        #点击添加选择框
        self.clickElemByXpath_visibility(self.icon_add_new_loc.replace('%s',fieldName))
        #点击搜索框
        self.clickElemByXpath_visibility(self.structSelector_searchBar)
        #输入搜索人
        self.sendkeysElemByXpath_visibility(self.searchInput_loc,userName)
        #点击查询结果
        self.clickElemByXpath_visibility(self.searchResult_loc.replace('%s',userName))
        #点击确定按钮
        self.clickElemByXpath_visibility(self.confirmBtn_loc)

    def MbUser_click_UserSelectBox( self,fieldName ):
        '''点击表单人员字段选择框'''
        self.clickElemByXpath_visibility(self.icon_add_new_loc.replace('%s',fieldName))

    def MbUser_sendkeys_UserSearch( self,userName ):
        '''人员字段搜索框输入值'''
        # 点击搜索框
        self.clickElemByXpath_visibility(self.structSelector_searchBar)
        # 输入搜索人
        self.sendkeysElemByXpath_visibility(self.searchInput_loc,userName)

    def MbUser_UserSearchOption_IsExist( self,userName):
        '''人员字段搜索框输入值'''
        if (self.find_elemByXPATH_visibility(self.searchResult_loc.replace('%s',userName)) != None):
            return True
        else:
            return False


    def MbUser_SelectUser( self,userName ):
        # 点击搜索框
        self.clickElemByXpath_visibility(self.structSelector_searchBar)
        # 输入搜索人
        self.sendkeysElemByXpath_visibility(self.searchInput_loc,userName)
        # 点击查询结果
        self.clickElemByXpath_visibility(self.searchResult_loc.replace('%s',userName))
        # 点击确定按钮
        self.clickElemByXpath_visibility(self.confirmBtn_loc)


    def MbUser_GetUserValue_readOnly( self,fieldName):
        '''获取只读状态下的人员多选字段的值'''
        valus = []
        spans = self.find_elemsByXPATH_visibility(self.UserValue_loc.replace('%s',fieldName))
        for span in spans:
            valus.append(span.text)
        return valus

    def MbUser_Tag_GetUserValue( self,fieldName,TagName):
        '''获取人员字段里某标签的人员数据'''
        userlist = []
        #点击添加选择框
        self.clickElemByXpath_visibility(self.icon_add_new_loc.replace('%s',fieldName))
        #切换至标签
        self.clickElemByXpath_visibility(self.structSelector_tab.replace('%s',"标签"))
        time.sleep(1)
        #点击标签
        self.clickElemByXpath_visibility(self.structSelector_dataList_div.replace('%s',TagName))
        #获取显示人员数据
        users = self.find_elemsByXPATH_visibility(self.struct_name_full)
        for user in users:
            userlist.append(user.text)
        return userlist


