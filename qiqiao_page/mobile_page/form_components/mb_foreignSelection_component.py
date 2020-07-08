#外键
from public.selenium_page import SeleniumPage


class MbForeignSelection_component(SeleniumPage):


    def ForeignSelection_Sendkeys(self,fieldName,list,*args):
        '''外键选择组件输入值
        fieldName：字段标题
        list：下拉选项 list类型
        '''
        loc = self.ForeignSelectionBox_loc.replace('%title',fieldName)
        self.clickElemByCSS_visibility(loc)
        for i in list:
            self.clickElemByCSS_visibility(self.ForeignSelectOption_loc.replace('%option',i))