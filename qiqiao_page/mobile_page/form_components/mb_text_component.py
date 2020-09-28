#单行文本组件
from public.selenium_page import SeleniumPage


class MbText(SeleniumPage):


    Text_input_loc = "div[title='%s'] input[type='text']"  #单行文本组件字段输入框

    Text_div_loc = "//div[@title='%s']//div[@class='readonly_text']"

    #
    def MbText_Sendkeys(self,fieldName,key,*args):
        '''给单行文本组件输入值
        fieldName：字段标题
        key：文本值
        '''
        self.sendkeysElemByCSS_Presence(self.Text_input_loc.replace('%s',fieldName), key)


    #获取单行文本字段提示信息


    def MbText_IsVisible( self,fieldName ):
        '''单行文本组件是否可见'''
        if(self.find_elemByCSS_visibility(self.Text_input_loc.replace('%s',fieldName),timeout=3)==None):
            return False
        else:
            return True


    def MbText_GetValue_readOnly(self,fieldName):
        '''获取只读状态的单行文本组件值'''
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.Text_div_loc.replace('%s',fieldName))
        return elem.text