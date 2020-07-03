#数字组件
from public.selenium_page import SeleniumPage


class Number(SeleniumPage):

    Number_input_loc = "//div[@data-mark='%s']//input"  # 数字组件字段输入框


    Number_div_loc = "//div[@data-mark='%s']//div[@class='component_detail']/div"  #只读状态数字组件显示值

    label_loc = "//div[@data-mark='%s']/label/span[@title='%s']"

    ChildFormPopup_loc = "//div[@data-mark='子表弹层_%s']"

    #
    def Number_Sendkeys(self,fieldName,key,*args):
        '''给数字组件输入值
        fieldName：字段标题
        key：数值  数字类型
        '''
        a = self.Number_input_loc.replace('%s',fieldName)
        self.sendkeysElemByXpath_visibility(a, key)
        #点击脱离光标
        self.clickElemByXpath_visibility(self.label_loc.replace('%s',fieldName))

    def Number_InChildForm_Sendkeys( self, childFormName,fieldName, key, *args ):
        '''在子表里给数字组件输入值
        fieldName：字段标题
        key：数值  数字类型
        '''
        loc = self.ChildFormPopup_loc.replace('%s',childFormName)+self.Number_input_loc.replace('%s',fieldName)
        self.sendkeysElemByXpath_visibility(loc,key)
        #点击脱离光标
        self.clickElemByXpath_visibility(self.label_loc.replace('%s',fieldName))


    def Number_GetValue_readOnly( self,fieldName ):
        '''获取只读状态的数字组件值'''
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.Number_div_loc.replace('%s',fieldName))
        return elem.text

