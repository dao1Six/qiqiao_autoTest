#单行文本组件
from public.selenium_page import SeleniumPage


class Text(SeleniumPage):


    Text_input_loc = "//div[@data-mark='%s']//input"  #单行文本组件字段输入框

    #
    def sendkeysToText(self,fieldName,key,*args):
        '''给单行文本组件输入值
        fieldName：字段标题
        key：文本值
        '''
        loc = self.Text_input_loc.replace('%s',fieldName)
        elems = self.find_elemsByXPATH(loc)
        if(len(elems)>1):
            elem = elems[len(elems)-1]
            self.sendkeysElem(elem,key)
        elif(len(elems)==1):
            elem = elems[0]
            self.sendkeysElem(elem, key)




    def getTextValue_writable( self ):
        '''获取可写状态的单行文本字段值'''
        pass


