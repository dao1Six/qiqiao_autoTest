#单行文本组件
from public.selenium_page import SeleniumPage


class Text(SeleniumPage):


    Text_input_loc = "[data-mark=%s] input"  #单行文本组件字段输入框

    #
    def sendkeysToText(self,fieldName,key,*args):
        '''给单行文本组件输入值
        fieldName：字段标题
        key：文本值
        '''
        self.sendkeysElemByCSS_Presence(self.Text_input_loc.replace('%s',fieldName), key)




    def getTextValue( self ):
        '''获取单行文本字段提示信息'''
        pass


