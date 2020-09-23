#人员组件
import time

from public.selenium_page import SeleniumPage


class User(SeleniumPage):

    # User_querenButton_loc = "//div[@class='el-dialog %s']//button[@data-mark='确定按钮']" #人员选择确认按钮
    User_querenButton_loc = "//button[@data-mark='确定按钮']"
    User_selectBox_loc = "//div[@data-mark='%s']//span[text()='+选择人员']"  #人员选择字段添加按钮

    User_search_loc = "//input[@placeholder='搜索用户']"  #人员选择组织架构搜索框

    User_searchOption_loc = "//span[contains(text(),'%s')]/parent::li[contains(@class,'el-select-dropdown__item')]"  #人员选择组织架构搜索项


    UserValue_readOnly_loc = "//div[@data-mark='%s']//div[contains(@class,'component_detail')]//li//span"  #人员选择组件值元素

    UserValue_Writable_loc = "//div[@data-mark='%s']//div[contains(@class,'component_detail')]//i/following-sibling::span"

    ChildFormPopup_loc = "//div[@data-mark='子表弹层_%s']"



    #
    def User_MonomialUser_Sendkeys(self,fieldName,userName):
        '''给人员单选组件输入值'''
        # fieldName：字段标题
        # userName：人员名称

        #点击选择框
        self.clickElemByXpath_visibility(self.User_selectBox_loc.replace('%s',fieldName))
        self.sendkeysElemByXpath_visibility(self.User_search_loc,userName)
        self.clickElemByXpath_visibility(self.User_searchOption_loc.replace('%s',userName))
        self.clickElemByXpath_visibility(self.User_querenButton_loc.replace('%s',fieldName))

    def User_MultiUser_Sendkeys(self,fieldName,userNameList,*args):
        ''' 给人员多选组件输入值
        fieldName：字段标题
        userNameList：人员名称集合  list类型
        '''
        #点击选择框
        self.clickElemByXpath_visibility(self.User_selectBox_loc.replace('%s',fieldName))
        self.selectUser(userNameList,fieldName)


    def selectUser( self,userNameList,fieldName):
        '''人员选择'''
        for name in userNameList:
            self.clickElemByXpath_visibility(self.User_search_loc)
            self.sendkeysElemByXpath_visibility(self.User_search_loc,name,isclear=True)
            self.clickElemByXpath_visibility(self.User_searchOption_loc.replace('%s',name))
        self.clickElemByXpath_visibility(self.User_querenButton_loc.replace('%s',fieldName))


    def User_MonomialUser_InChildForm_Sendkeys(self,childFormName,fieldName,userName):
        '''在子表里给人员单选组件输入值
        fieldName：字段标题
        userName：人员名称
        '''
        #点击选择框
        self.clickElemByXpath_visibility(self.ChildFormPopup_loc.replace('%s',childFormName)+self.User_selectBox_loc.replace('%s',fieldName))
        #输入搜索值
        self.sendkeysElemByXpath_visibility(self.User_search_loc,userName)
        #点击搜索项
        self.clickElemByXpath_visibility(self.User_searchOption_loc.replace('%s',userName))
        #点击确定按钮
        self.clickElemByXpath_visibility(self.User_querenButton_loc.replace('%s',fieldName))



    def User_GetMonomialUserValue_readOnly( self,fieldName):
        '''获取只读状态下的人员单选字段的值'''
        return self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.UserValue_readOnly_loc.replace('%s',fieldName)).text


    def User_GetMultiUserValue_readOnly( self,fieldName):
        '''获取只读状态下的人员多选字段的值'''
        valus = []
        spans = self.find_elemsByXPATH_presence(self.UserValue_readOnly_loc.replace('%s',fieldName))
        for span in spans:
            valus.append(span.text)
        return valus


    
    def User_GetUserValue_Writable( self,fieldName):
        '''获取可写状态下的人员字段的值'''
        valus = []
        spans = self.find_elemsByXPATH_presence(self.UserValue_Writable_loc.replace('%s',fieldName))
        for span in spans:
            valus.append(span.text)
        return valus







