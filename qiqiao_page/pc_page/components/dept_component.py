#部门组件
import time

from public.selenium_page import SeleniumPage


class Dept(SeleniumPage):


    Dept_querenButton_loc = "//div[@class='el-dialog %s']//button[@data-mark='确定按钮']"  #部门选择确认按钮

    Dept_selectBox_loc = "//div[@data-mark='%s']//span[text()='+选择部门']"  #部门选择字段添加按钮


    Dept_search_loc = "[data-mark=组织选择器搜索框] input"  #部门选择组织架构搜索框


    Dept_searchOption_loc = "//ul//span[contains(text(),'%s')]" #部门选择组织架构搜索项

    El_tree_loc = "//div[@id='tree-item']"


    # 给部门单选组件输入值
    def sendkeysToMonomialDept(self,fieldName,DeptName,*args):
        ''' 给部门单选组件输入值
        fieldName：字段标题
        DeptName：部门名称
        '''
        #点击选择框
        self.clickElemByXpath_Presence(self.Dept_selectBox_loc.replace('%s',fieldName))
        #等待组织架构加载
        self.wait_elem_visible(self.El_tree_loc)
        #搜索框输入部门名称
        self.sendkeysElemByCSS_Presence(self.Dept_search_loc,DeptName)
        #点击查询结果
        self.clickElemByXpath_Presence(self.Dept_searchOption_loc.replace('%s',DeptName))
        #点击确认按钮
        self.clickElemByXpath_Presence(self.Dept_querenButton_loc.replace('%s',fieldName))


    # 给部门多选组件输入值
    def sendkeysToMultiDept(self,fieldName,DeptNameList,*args):
        ''' 给部门多选组件输入值
        fieldName：字段标题
        DeptNameList：部门名称集合  list类型
        '''
        #点击选择框
        self.clickElemByXpath_Presence(self.Dept_selectBox_loc.replace('%s',fieldName))
        for name in DeptNameList:
            self.clickElemByXpath_Presence (self.Dept_search_loc)
            self.sendkeysElemByXpath_Presence(self.Dept_search_loc,name)
            e = self.find_elemByXPATH(self.Dept_searchOption_loc.replace('%s',name))
            e.click()
        # 点击确认按钮
        self.clickElemByXpath_Presence(self.Dept_querenButton_loc.replace('%s', fieldName))

