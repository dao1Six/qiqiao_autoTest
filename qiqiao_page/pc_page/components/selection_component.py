#选择组件


from public.selenium_page import SeleniumPage


class Selection(SeleniumPage):

    Selection_selectionBox_loc = "//div[@data-mark='%title']//input"  #下拉选择组件下拉框

    Selection_multiSelectOption_loc = "li[data-mark=%option]" #下拉多选选项

    Selection_monomialSelectOption_loc = "//div[@class='el-select-dropdown el-popper %title']//li[@data-mark='%value']"  #下拉单选选项

    Selection_Option_loc = "//div[@title='%s']//span[text()='%option']"  #单选多选选项

    Selection_Option_check_loc = "//div[@title='%s']//span[text()='%option']/preceding-sibling::span[@class='el-radio__input is-checked']" #单选多选选项被选中后出来的元素

    SelectionBox_Value_loc = "//div[@data-mark='%s']//div[contains(@class,'component_detail')]//input"   #下拉选择框值



    #
    def Selection_MultiSelect_Sendkeys(self,fieldName,list,*args):
        '''下拉多选组件输入值
        fieldName：字段标题
        list：下拉选项 list类型
        '''
        loc = self.Selection_selectionBox_loc.replace('%title',fieldName)
        self.clickElemByXpath_Presence(loc)
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
        elems = self.find_elemsByXPATH(loc)
        if(len(elems)>1):
            elem = elems[len(elems)-1]
        #点击输入框
            self.clickElem(elem)
            #点击选项
            self.clickElemByXpath_Presence(self.Selection_monomialSelectOption_loc.replace('%title',fieldName).replace('%value',value),index=1)
        elif(len(elems)==1):
            elem = elems[0]
            self.clickElem(elem)
            #点击选项
            self.clickElemByXpath_Presence(self.Selection_monomialSelectOption_loc.replace('%title',fieldName).replace('%value',value),index=0)

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
            self.clickElemByXpath_Presence (self.Selection_Option_loc.replace('%s',fieldName).replace('%option',option))


    #
    def Selection_CheckboxSelect_Sendkeys(self,fieldName,list,*args):
        '''给多项选择组件输入值
        fieldName：字段标题
        list：多项选项 list类型
        '''
        for i in list:
            self.clickElemByXpath_Presence(self.Selection_Option_loc.replace('%s',fieldName).replace('%option',i))