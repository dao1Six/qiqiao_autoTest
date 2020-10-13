import time

from public.selenium_page import SeleniumPage


class MbDept(SeleniumPage):
    '''移动端部门组件'''

    icon_add_new_loc = "//div[@title='%s']//div[@class='icon_add_new']"
    structSelector_searchBar = "//div[@class='structSelector_searchBar']"
    searchInput_loc = "//div[@class='structSelector_main_active']/input"
    searchResult_loc = "//div[@class='structSelector_searchResult']//div[@class='cube-checkbox']//input"
    confirmBtn_loc = "//button[@class='cube-btn fr confirmBtn cube-btn-inline cube-btn-primary']"

    departmentList_name_loc = "//div[@title='%s']//div[@class='departmentList_name']"
    departmentList_name_span_loc = "//div[@title='%s']//div[@class='departmentList_name']/span"

    ChildFormPopup_dept_divReadonlyValue_loc = "//div[@title='%s']//div[@class='departmentList_name']"


    def MbDept_MonomialDept_Sendkeys( self,fieldName,deptName,index=0,*args):
        '''给部门单选组件输入值'''
         # fieldName：字段标题
         # deptName：部门名称

        # 点击添加选择框
        self.clickElemByXpath_visibility(self.icon_add_new_loc.replace('%s',fieldName))
        # 点击搜索框
        self.clickElemByXpath_visibility(self.structSelector_searchBar)
        # 输入搜索部门
        self.sendkeysElemByXpath_visibility(self.searchInput_loc,deptName)
        time.sleep(2)
        # 点击查询结果
        self.clickElemByXpath_presence(self.searchResult_loc,index=index)
        # 点击确定按钮
        self.clickElemByXpath_visibility(self.confirmBtn_loc)


    def MbDept_MonomialDept_GetValue( self,fieldName,*args):
        '''获取部门单选组件的值
         fieldName：字段标题
         deptName：部门名称
         '''
        return self.find_elenmInElemsByXpath_presence_of_all_elements_located(self.departmentList_name_loc.replace('%s',fieldName)).text + self.find_elenmInElemsByXpath_presence_of_all_elements_located(self.departmentList_name_span_loc.replace('%s',fieldName)).text


    def MbDept_GetValue_readOnly_InPopup( self,fieldName ):
        '''在表单弹窗里获取只读状态下的部门组件值'''
        loc = self.ChildFormPopup_dept_divReadonlyValue_loc.replace('%s',fieldName)
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(loc)
        return elem.text