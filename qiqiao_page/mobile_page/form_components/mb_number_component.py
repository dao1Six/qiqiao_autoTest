#数字组件
from public.selenium_page import SeleniumPage


class MbNumber(SeleniumPage):

    Number_input_loc = "//div[@title='%s']//input"  # 数字组件字段输入框
    Number_div_loc = "//div[@title='%s']//div[@class='readonly_text']"



    #
    def MbNumber_Sendkeys(self,fieldName,key,*args):
        '''给数字组件输入值
        fieldName：字段标题
        key：数值  数字类型
        '''
        self.sendkeysElemByXpath_visibility(self.Number_input_loc.replace('%s',fieldName),str(key))

    def MbNumber_GetValue_readOnly(self,fieldName):
        '''获取只读状态的数字组件值'''
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.Number_div_loc.replace('%s',fieldName))
        return elem.text

    def MbNumber_GetValue_formula(self,fieldName):
        '''获取公式类型数字组件值'''
        elem = self.find_elemsByXPATH_presence(self.Number_input_loc.replace('%s',fieldName))[0]
        numberValue = self.getElemAttrValue(elem,'value')
        if (numberValue != ""):
            # 判断是否有小数位
            if ("." not in numberValue):
                return int(numberValue)
            else:
                return float(numberValue)
        else:
            return None


    def MbNumber_IsVisible(self,fieldName):
        '''数字字段是否可见'''
        if(self.find_elemByXPATH_visibility(self.Number_input_loc.replace('%s',fieldName),timeout=3)==None):
            return False
        else:
            return True

    def MbNumber_GetValue_writable_InPopup( self,fieldName ):
        '''表单弹层获取可写状态的数字字段值'''
        loc = self.Number_input_loc.replace('%s',fieldName)
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
        # return self.getElemAttrValue(self.find_elenmInElemsByXpath_visibility_of_any_elements_located(loc),'value')