#人员组件
import time

from public.selenium_page import SeleniumPage


class User(SeleniumPage):

    User_querenButton_loc = "//div[@class='el-dialog %s']//button[@data-mark='确定按钮']" #人员选择确认按钮

    User_selectBox_loc = "//div[@title='%s']//span[text()='+选择人员']"  #人员选择字段添加按钮

    User_search_loc = "//input[@placeholder='搜索用户']"  #人员选择组织架构搜索框

    User_searchOption_loc = "//li/span[contains(text(),'%s')]"  #人员选择组织架构搜索项

    UserValue_loc = "//div[@data-mark='%s']//div[contains(@class,'component_detail')]//span"  #人员选择组件值元素



    #
    def sendkeysToMonomialUser(self,fieldName,userName):
        '''给人员单选组件输入值
        fieldName：字段标题
        userName：人员名称
        '''
        #点击选择框
        self.clickElemByXpath_Presence(self.User_selectBox_loc.replace('%s',fieldName))
        self.sendkeysElemByXpath_Presence(self.User_search_loc,userName)
        self.clickElemByXpath_Presence(self.User_searchOption_loc.replace('%s',userName))
        self.clickElemByXpath_Presence(self.User_querenButton_loc.replace('%s',fieldName))

    def getMonomialUserValue_readOnly( self,fieldName):
        '''获取只读状态下的人员单选字段的值'''
        return self.find_elenmInElemsByXpath(self.UserValue_loc.replace('%s',fieldName)).text



    def sendkeysToMultiUser(self,fieldName,userNameList,*args):
        ''' 给人员多选组件输入值
        fieldName：字段标题
        userNameList：人员名称集合  list类型
        '''
        #点击选择框
        self.clickElemByXpath_Presence(self.User_selectBox_loc.replace('%s',fieldName))
        self.selectUser(userNameList)

    def selectUser( self,userNameList,fieldName):
        for name in userNameList:
            self.clickElemByXpath_Presence(self.User_search_loc)
            self.sendkeysElemByXpath_Presence(self.User_search_loc,name)
            self.clickElemByXpath_Presence(self.User_searchOption_loc.replace('%s',name),index=1)
        self.clickElemByXpath_Presence(self.User_querenButton_loc.replace('%s',fieldName))





