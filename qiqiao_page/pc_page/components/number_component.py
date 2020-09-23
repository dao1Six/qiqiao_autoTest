#数字组件
from public.selenium_page import SeleniumPage


class Number(SeleniumPage):

    Number_input_loc = "//div[@data-mark='%s']//input"  # 数字组件字段输入框


    Number_div_loc = "//div[@data-mark='%s']//div[@class='component_detail']/div"  #只读状态数字组件显示值

    label_loc = "//div[@data-mark='%s']/label/span[@title='%s']"

    ChildFormPopup_loc = "//div[@data-mark='子表弹层_%s']"
    ChildFormPopup_Number_div_loc = "//div[@title='%title']//div[contains(@class,'component_detail')]//div"
    ChildFormPopup_Number_input_loc = "//div[@title='%title']//input"
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




    def Number_GetValue_readOnly( self,fieldName ):
        '''获取只读状态的数字组件值'''
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.Number_div_loc.replace('%s',fieldName))
        return elem.text



    def Number_GetValue_Writable( self,fieldName ):
        '''获取可写状态的数字组件值'''
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.Number_input_loc.replace('%s',fieldName))
        numberValue =self.getElemAttrValue(elem,'value')
        if(numberValue!=""):
            #判断是否有小数位
            if("." not in numberValue):
                return int(numberValue)
            else:
                return float(numberValue)
        else:
            return None

    def Number_InPopup_Sendkeys( self, childFormName,fieldName, key, *args ):
        '''在表单弹窗给数字组件输入值
        fieldName：字段标题
        key：数值  数字类型
        '''
        loc = self.ChildFormPopup_loc.replace('%s',childFormName)+self.Number_input_loc.replace('%s',fieldName)
        self.sendkeysElemByXpath_visibility(loc,key)
        #点击脱离光标
        self.clickElemByXpath_visibility(self.label_loc.replace('%s',fieldName))

    def Number_GetValue_writable_InPopup( self,childFormName,fieldName ):
        '''表单弹层获取可写状态的数字字段值'''
        loc = self.ChildFormPopup_loc.replace('%s',childFormName) + self.ChildFormPopup_Number_input_loc.replace('%title',fieldName)
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(loc)
        numberValue = self.getElemAttrValue(elem,'value')
        if (numberValue != ""):
            # 判断是否有小数位
            if ("." not in numberValue):
                return int(numberValue)
            else:
                return float(numberValue)
        else:
            return None
        return self.getElemAttrValue(self.find_elenmInElemsByXpath_visibility_of_any_elements_located(loc),'value')

    def Number_GetValue_readOnly_InPopup( self,childFormName,fieldName ):
        '''表单弹层获取只读状态的数字字段值'''
        loc = self.ChildFormPopup_loc.replace('%s',childFormName) + self.ChildFormPopup_Number_div_loc.replace('%title',fieldName)
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(loc)
        return elem.text