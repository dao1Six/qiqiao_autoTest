#选择组件


from public.selenium_page import SeleniumPage


class Selection(SeleniumPage):

    Selection_Option_loc = "//div[@title='%s']//span[text()='%option']/parent::label[1]"  # 单选多选选项

    def Selection_CheckboxSelect_Sendkeys(self,fieldName,list,*args):
        '''给多项选择组件输入值
        fieldName：字段标题
        list：多项选项 list里存放选项文本值
        '''
        for i in list:
            self.clickElemByXpath_visibility(self.Selection_Option_loc.replace('%s',fieldName).replace('%option',i))

