#外键
from public.selenium_page import SeleniumPage


class ForeignSelection_component(SeleniumPage):

    ForeignSelectionBox_loc = "//div[@data-mark='%title']//input"

    ForeignSelectOption_loc = "//li[@data-mark='option_%s']"

    ChildFormPopup_loc = "//div[@data-mark='子表弹层_%s']"

    def ForeignSelection_Sendkeys(self,fieldName,value,index1=0,index2=0,*args):
        '''外键选择组件输入值
        fieldName：字段标题
        '''
        loc = self.ForeignSelectionBox_loc.replace('%title',fieldName)
        #点击外键的输入框
        self.clickElemByXpath_visibility(loc,index=index1)
        #点击选项
        self.clickElemByXpath_visibility(self.ForeignSelectOption_loc.replace('%s',value),index=index2)


    def ForeignSelection_InChildForm_Sendkeys( self,childFormName,fieldName,value,*args ):

        '''子表弹框输入外键值'''

        loc = self.ChildFormPopup_loc.replace('%s',childFormName)+self.ForeignSelectionBox_loc.replace('%title',fieldName)
        #点击外键的输入框
        self.clickElemByXpath_visibility(loc)
        #点击选项
        self.clickElemByXpath_visibility(self.ForeignSelectOption_loc.replace('%s',value))


