#单行文本组件
from public.selenium_page import SeleniumPage


class Text(SeleniumPage):


    Text_input_loc = "//div[@data-mark='%s']//input"  #单行文本组件字段输入框

    Text_label_loc = "//div[@data-mark='%s']/label/span[@title='%s']"

    ChildFormPopup_loc = "//div[@data-mark='子表弹层_%s']"
    #
    def Text_Sendkeys(self,fieldName,key,*args):
        '''给单行文本组件输入值
        fieldName：字段标题
        key：文本值
        '''
        loc = self.Text_input_loc.replace('%s',fieldName)
        self.sendkeysElemByXpath_visibility(loc,key)
        #点击脱离光标
        self.clickElemByXpath_visibility(self.Text_label_loc.replace('%s',fieldName))

    def Text_InChildForm_Sendkeys( self,childFormName,fieldName,key,*args ):

        '''子表弹框输入文本值'''
        loc = self.ChildFormPopup_loc.replace('%s',childFormName)+self.Text_input_loc.replace('%s',fieldName)
        self.sendkeysElemByXpath_visibility(loc,key)
        #点击脱离光标
        self.clickElemByXpath_visibility(self.Text_label_loc.replace('%s',fieldName))



    def Text_GetValue_writable( self,fieldName ):
        '''获取可写状态的单行文本字段值'''

        return self.getElemAttrValue(self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.Text_input_loc.replace('%s',fieldName)),'value')



