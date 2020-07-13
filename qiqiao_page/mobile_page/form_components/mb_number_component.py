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
        self.sendkeysElemByXpath_visibility(self.Number_input_loc.replace('%s',fieldName),key)

    def MbNumber_GetValue_readOnly(self,fieldName):
        '''获取只读状态的数字组件值'''
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.Number_div_loc.replace('%s',fieldName))
        return elem.text

