#部门组件
import time

from public.selenium_page import SeleniumPage


class Dept(SeleniumPage):


    Dept_querenButton_loc = "//div[@class='el-dialog %s']//button[@data-mark='确定按钮']"  #部门选择确认按钮

    Dept_selectBox_loc = "//div[@data-mark='%s']//span[text()='+选择部门']"  #部门选择字段添加按钮


    Dept_search_loc = "[data-mark=组织选择器搜索框] input"  #部门选择组织架构搜索框


    Dept_searchOption_loc = "//ul//span[contains(text(),'%s')]" #部门选择组织架构搜索项

    El_tree_loc = "//div[@id='tree-item']"

    DeptValue_loc = "//div[@data-mark='%s']//div[contains(@class,'component_detail')]//i/following-sibling::span"  # 部门选择组件值元素


    # 给部门单选组件输入值
    def Dept_MonomialDept_Sendkeys(self,fieldName,DeptName,index=0,*args):
        ''' 给部门单选组件输入值
        fieldName：字段标题
        DeptName：部门名称
        '''
        #点击选择框
        self.clickElemByXpath_visibility(self.Dept_selectBox_loc.replace('%s',fieldName))
        #等待组织架构加载
        self.wait_elem_visible_XPATH(self.El_tree_loc)
        self.Dept_Select(DeptName,index)
        #点击确认按钮
        self.clickElemByXpath_visibility(self.Dept_querenButton_loc.replace('%s',fieldName))

    def Dept_Select( self ,DeptName,index):
        '''选择部门'''
        self.clickElemByCSS_visibility(self.Dept_search_loc)
        # 搜索框输入部门名称
        self.sendkeysElemByCSS_Presence(self.Dept_search_loc,DeptName)
        # 点击查询结果
        self.clickElemByXpath_visibility(self.Dept_searchOption_loc.replace('%s',DeptName),index=index)

    # 给部门多选组件输入值
    def Dept_MultiDept_Sendkeys(self,fieldName,DeptNameList,*args):
        ''' 给部门多选组件输入值
        fieldName：字段标题
        DeptNameList：部门名称集合  list类型
        '''
        #点击选择框
        self.clickElemByXpath_visibility(self.Dept_selectBox_loc.replace('%s',fieldName))
        #等待组织架构加载
        self.wait_elem_visible_XPATH(self.El_tree_loc)
        for name,index in DeptNameList.items():
            self.Dept_Select(name,index)
        # 点击确认按钮
        self.clickElemByXpath_visibility(self.Dept_querenButton_loc.replace('%s', fieldName))



    def Dept_GetDeptValue_Writable( self,fieldName):
        '''获取可写状态下的部门字段的值'''
        valus = []
        spans = self.find_elemsByXPATH_presence(self.DeptValue_loc.replace('%s',fieldName))
        for span in spans:
            valus.append(span.text)
        return valus
