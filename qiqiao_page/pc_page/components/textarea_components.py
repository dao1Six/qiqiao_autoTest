#多行文本组件

from public.selenium_page import SeleniumPage


class Textarea(SeleniumPage):

    Textarea_input_loc = "//div[@data-mark='%s']//textarea"  #多行文本组件字段输入框

    #
    def Textarea_Sendkeys(self,fieldName,key,*args):
        '''给多行文本组件输入值
        fieldName：字段标题
        key：文本值
        '''
        self.sendkeysElemByXpath_visibility(self.Textarea_input_loc.replace('%s',fieldName),key)


    def Textarea_GetValue_Writable( self,fieldName ):
        '''获取可写状态的多行文本组件值'''
        elem = self.find_elemByXPATH_visibility(self.Textarea_input_loc.replace('%s',fieldName))
        TextareaValue =self.getElemAttrValue(elem,'title')
        return TextareaValue


