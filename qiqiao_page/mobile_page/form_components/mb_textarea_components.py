#多行文本组件

from public.selenium_page import SeleniumPage


class MbTextarea(SeleniumPage):

    Textarea_input_loc = "//div[@title='%s']//textarea"  #多行文本组件字段输入框

    #
    def MbTextarea_Sendkeys(self,fieldName,key,*args):
        '''给多行文本组件输入值
        fieldName：字段标题
        key：文本值
        '''
        self.sendkeysElemByXpath_visibility(self.Textarea_input_loc.replace('%s',fieldName),key)


