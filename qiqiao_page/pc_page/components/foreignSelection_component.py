#外键
from public.selenium_page import SeleniumPage


class ForeignSelection_component(SeleniumPage):

    ForeignSelectionBox_loc = "//div[@data-mark='%title']//input"

    ForeignSelectOption_loc = "//li[@data-mark='option_%s']"

    ChildFormPopup_loc = "//div[@data-mark='子表弹层_%s']"

    ChildFormPopup_ForeignSelectionBox_Input_loc = "//div[@title='%title']//input"

    ChildFormPopup_ForeignSelectionBox_span_loc = "//div[@title='%title']//div[contains(@class,'component_detail')]//div//span"

    def ForeignSelection_Sendkeys(self,fieldName,value,index1=0,index2=0,*args):
        '''外键选择组件输入值
        fieldName：字段标题
        '''
        loc = self.ForeignSelectionBox_loc.replace('%title',fieldName)
        #点击外键的输入框
        self.clickElemByXpath_visibility(loc,index=index1)
        #点击选项
        self.clickElemByXpath_visibility(self.ForeignSelectOption_loc.replace('%s',value),index=index2)


    def ForeignSelection_InPopup_Sendkeys( self,childFormName,fieldName,value,*args ):

        '''子表弹框输入外键值'''

        loc = self.ChildFormPopup_loc.replace('%s',childFormName)+self.ChildFormPopup_ForeignSelectionBox_Input_loc.replace('%title',fieldName)
        #点击外键的输入框
        self.clickElemByXpath_visibility(loc)
        #点击选项
        self.clickElemByXpath_visibility(self.ForeignSelectOption_loc.replace('%s',value))


    def ForeignSelection_GetValue_writable_InPopup( self,childFormName,fieldName ):
        '''表单弹层获取可写状态的外键字段值'''
        loc = self.ChildFormPopup_loc.replace('%s',childFormName) + self.ChildFormPopup_ForeignSelectionBox_Input_loc.replace('%title',fieldName)
        return self.getElemAttrValue(self.find_elenmInElemsByXpath_visibility_of_any_elements_located(loc),'value')



    def ForeignSelection_GetValue_readOnly_InPopup( self,childFormName,fieldName ):
        '''表单弹层获取只读状态的外键字段值'''
        loc = self.ChildFormPopup_loc.replace('%s',childFormName) + self.ChildFormPopup_ForeignSelectionBox_span_loc.replace('%title',fieldName)
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(loc)
        return elem.text