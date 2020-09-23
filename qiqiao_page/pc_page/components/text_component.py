#单行文本组件
from public.selenium_page import SeleniumPage


class Text(SeleniumPage):


    Text_input_loc = "//div[@data-mark='%s']//input"  #单行文本组件字段输入框

    Text_label_loc = "//div[@data-mark='%s']/label/span[@title='%s']"

    ChildFormPopup_loc = "//div[@data-mark='子表弹层_%s']"

    ChildFormPopup_Text_div_loc = "//div[@title='%title']//div[contains(@class,'component_detail')]//div"
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

    def Text_InPopup_Sendkeys( self,childFormName,fieldName,key,*args ):

        '''表单弹层输入文本值'''
        loc = self.ChildFormPopup_loc.replace('%s',childFormName)+self.Text_input_loc.replace('%s',fieldName)
        self.sendkeysElemByXpath_visibility(loc,key)
        #点击脱离光标
        self.clickElemByXpath_visibility(self.Text_label_loc.replace('%s',fieldName))


    def Text_GetValue_writable( self,fieldName ):
        '''获取可写状态的单行文本字段值'''
        return self.getElemAttrValue(self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.Text_input_loc.replace('%s',fieldName)),'value')


    def Text_GetValue_writable_InPopup( self,childFormName,fieldName ):
        '''表单弹层获取可写状态的单行文本字段值'''
        loc = self.ChildFormPopup_loc.replace('%s',childFormName) + self.Text_input_loc.replace('%s',fieldName)
        return self.getElemAttrValue(self.find_elenmInElemsByXpath_visibility_of_any_elements_located(loc),'value')

    def Text_GetValue_readOnly_InPopup( self,childFormName,fieldName ):
        '''表单弹层获取只读状态的单行文本字段值'''
        loc = self.ChildFormPopup_loc.replace('%s',childFormName) + self.ChildFormPopup_Text_div_loc.replace('%title',fieldName)
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(loc)
        return elem.text
