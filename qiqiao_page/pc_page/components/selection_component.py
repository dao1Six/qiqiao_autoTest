#选择组件


from public.selenium_page import SeleniumPage


class Selection(SeleniumPage):

    Selection_selectionBox_loc = "//div[@data-mark='%title']//input"  #下拉选择组件下拉框

    Selection_multiSelectOption_loc = "li[data-mark=%option]" #下拉多选选项

    Selection_monomialSelectOption_loc = "//li[@data-mark='%value']"  #下拉单选选项

    Selection_Option_loc = "//div[@data-mark='%s']//span[text()='%option']"  #单选多选选项

    Selection_Option_check_loc = "//div[@title='%s']//span[text()='%option']/preceding-sibling::span[@class='el-radio__input is-checked']" #单选多选选项被选中后出来的元素

    SelectionBox_Value_loc = "//div[@data-mark='%s']//div[contains(@class,'component_detail')]//input"   #下拉选择框值

    ChildFormPopup_loc = "//div[@data-mark='子表弹层_%s']"



    #
    def Selection_MultiSelect_Sendkeys(self,fieldName,list,*args):
        '''下拉多选组件输入值
        fieldName：字段标题
        list：下拉选项 list类型
        '''
        loc = self.Selection_selectionBox_loc.replace('%title',fieldName)
        self.clickElemByXpath_visibility(loc)
        for i in list:
            self.clickElemByCSS_Presence(self.Selection_multiSelectOption_loc.replace('%option',i))

    #
    def Selection_MonomialSelect_Sendkeys(self,fieldName,value,*args):
        '''下拉单选组件输入值
        fieldName：字段标题
        option：下拉选项
        '''
        #下拉文本框
        loc = self.Selection_selectionBox_loc.replace('%title',fieldName)
        self.clickElemByXpath_visibility(loc)
        # 点击选项
        self.clickElemByXpath_visibility(self.Selection_monomialSelectOption_loc.replace('%value',value))


    def Selection_MonomialSelect_InChildForm_Sendkeys(self,childFormName,fieldName,value,*args):
        '''在子表里给下拉单选组件输入值
        fieldName：字段标题
        option：下拉选项
        '''
        #下拉文本框
        loc = self.ChildFormPopup_loc.replace('%s',childFormName)+self.Selection_selectionBox_loc.replace('%title',fieldName)
        self.clickElemByXpath_visibility(loc)
        #点击选项
        self.clickElemByXpath_visibility(self.Selection_monomialSelectOption_loc.replace('%value', value))



    def Selection_GetSelectionBoxValue_writable( self,fieldName):
        '''获取可写状态下的下拉框组件值'''
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.SelectionBox_Value_loc.replace('%s', fieldName))
        return self.getElemAttrValue(elem, "value")

    #
    def Selection_RadioSelect_Sendkeys(self,fieldName,option,*args):
        '''给单项选择组件输入值
        fieldName：字段标题
        option：单项选项
        '''
        while(self.find_elemsByXPATH(self.Selection_Option_check_loc.replace('%s',fieldName).replace('%option',option))==None):
            #点击选项
            self.clickElemByXpath_visibility (self.Selection_Option_loc.replace('%s',fieldName).replace('%option',option))

    def Selection_RadioSelect_InChildForm_Sendkeys(self,childFormName,fieldName,option,*args):
        '''在子表单里给单项选择组件输入值
        fieldName：字段标题
        option：单项选项
        '''
        while(self.find_elemsByXPATH(self.Selection_Option_check_loc.replace('%s',fieldName).replace('%option',option))==None):
            #点击选项
            self.clickElemByXpath_visibility (self.ChildFormPopup_loc.replace('%s',childFormName)+self.Selection_Option_loc.replace('%s',fieldName).replace('%option',option))


    #
    def Selection_CheckboxSelect_Sendkeys(self,fieldName,list,*args):
        '''给多项选择组件输入值
        fieldName：字段标题
        list：多项选项 list里存放选项文本值
        '''
        for i in list:
            self.clickElemByXpath_visibility(self.Selection_Option_loc.replace('%s',fieldName).replace('%option',i))