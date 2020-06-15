#多行文本组件

from public.selenium_page import SeleniumPage


class Textarea(SeleniumPage):

    Textarea_input_loc = "[data-mark=%title] textarea"  #多行文本组件字段输入框

    #
    def sendkeysToTextarea(self,fieldName,key,*args):
        '''给多行文本组件输入值
        fieldName：字段标题
        key：文本值
        '''
        self.sendkeysElemByCSS_Presence(self.Textarea_input_loc.replace('%title',fieldName),key)


