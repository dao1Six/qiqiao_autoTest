#级联组件
from public.selenium_page import SeleniumPage


class MbCascade(SeleniumPage):

    Cascade_selectionBox_loc = "//div[@title='%s']//span[@class='el-cascader__label']"  # 级联组件字段选择下拉框

    Cascade_selecOption_loc = "//div[@class='el-cascader-menus el-popper']//span[contains(text(),'%s')]"  # 级联选择组件字段选项

    #输入级联组件的值
    def Cascade_Sendkeys(self,fieldName,optionsList,*args):
        '''输入级联组件的值
        fieldName：字段标题
        optionsList：级联选项  list类型
        '''
        self.clickElemByXpath_visibility(self.Cascade_selectionBox_loc.replace('%s', fieldName))
        for i in optionsList:
            self.clickElemByXpath_visibility(self.Cascade_selecOption_loc.replace('%s', i))

    #给级联组件输入值