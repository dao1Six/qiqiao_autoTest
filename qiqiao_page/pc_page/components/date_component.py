#日期组件
from public.selenium_page import SeleniumPage


class Date(SeleniumPage):

    Date_input_loc =  "//div[@data-mark='%s']//input[@class='el-input__inner']"  # 日期组件输入框

    Date_label_loc = "div[data-mark='%s']>label>span[title='%title']"  # 日期组件字段标题

    ChildFormPopup_loc = "//div[@data-mark='子表弹层_%s']"


    #给日期组件输入值
    def Date_Sendkeys(self,fieldName,key,isclear=False,*args):
        '''给日期组件输入值
        fieldName：字段标题
        key：日期值 格式：2018-11-22
        '''
        self.sendkeysElemByXpath_visibility(self.Date_input_loc.replace('%s',fieldName),key,isclear=isclear)
        #点击标题名脱离光标
        self.clickElemByCSS_Presence(self.Date_label_loc.replace('%s',fieldName).replace('%title',fieldName))

    def Date_InChildForm_Sendkeys( self,childFormName,fieldName,key,isclear=False,*args ):

        '''子表弹框输入文本值'''
        loc = self.ChildFormPopup_loc.replace('%s',childFormName)+self.Date_input_loc.replace('%s',fieldName)
        self.sendkeysElemByXpath_visibility(loc,key,isclear=isclear)
        # 点击标题名脱离光标
        self.clickElemByCSS_Presence(self.Date_label_loc.replace('%s', fieldName).replace('%title', fieldName))



    #获取可写状态的日期组件的值
    def Date_GetValue_writable( self,fieldName ):
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.Date_input_loc.replace('%s',fieldName))
        return self.getElemAttrValue(elem,"value")