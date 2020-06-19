#外键
from public.selenium_page import SeleniumPage


class ForeignSelection_component(SeleniumPage):

    ForeignSelectionBox_loc = "//div[@title='%title']//input"

    ForeignSelectOption_loc = "//li[@data-mark='option_%s']"

    def sendkeysToForeignSelection(self,fieldName,value,*args):
        '''外键选择组件输入值
        fieldName：字段标题

        '''
        loc = self.ForeignSelectionBox_loc.replace('%title',fieldName)
        #点击外键的输入框
        self.clickElemByXpath_Presence(loc)
        #点击选项
        self.clickElemByXpath_Presence(self.ForeignSelectOption_loc.replace('%s',value))


    def sendkeysTo_ChildForm_ForeignSelection( self ):
        '''子表弹框输入外键值'''
