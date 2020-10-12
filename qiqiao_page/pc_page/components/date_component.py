#日期组件
import time

from public.selenium_page import SeleniumPage


class Date(SeleniumPage):

    Date_input_loc =  "//div[@data-mark='%s']//input[@class='el-input__inner']"  # 日期组件输入框

    Date_label_loc = "div[data-mark='%s']>label>span[title='%title']"  # 日期组件字段标题

    ChildFormPopup_loc = "//div[@data-mark='子表弹层_%s']"

    form_title_loc = "//div[@class='header']/div[@class='title']"

    ChildFormPopup_DateDateIcon_loc = "//div[@data-mark='子表弹层_%s']//div[@data-mark='%f']//i[@class='el-input__icon el-icon-date']"
    ChildFormPopup_DateClearIcon_loc = "//div[@data-mark='子表弹层_%s']//div[@data-mark='%f']//i[@class='el-input__icon el-icon-circle-close']"
    #给日期组件输入值
    def Date_Sendkeys(self,fieldName,key,isclear=False,*args):
        '''给日期组件输入值
        fieldName：字段标题
        key：日期值 格式：2018-11-22
        '''
        self.sendkeysElemByXpath_visibility(self.Date_input_loc.replace('%s',fieldName),key,isclear=isclear)
        #点击表单标题脱离光标
        self.clickElemByXpath_visibility(self.form_title_loc)

    def Date_Sendkeys_InPop( self,childFormName,fieldName,key,isclear=False,*args ):
        '''子表弹框输入日期值'''

        loc = self.ChildFormPopup_loc.replace('%s',childFormName)+self.Date_input_loc.replace('%s',fieldName)
        self.sendkeysElemByXpath_visibility(loc,key,isclear=isclear)
        #点击表单标题脱离光标
        self.clickElemByXpath_visibility(self.form_title_loc,index=1)

    def Date_clearValue_InPop( self,childFormName,fieldName,*args ):
        '''子表弹框清除日期值'''
        elem = self.find_elemByXPATH_visibility(self.ChildFormPopup_DateDateIcon_loc.replace('%s',childFormName).replace('%f',fieldName))
        self.move_to_element(elem)
        closeElem = self.find_elemByXPATH_visibility(self.ChildFormPopup_DateClearIcon_loc.replace('%s',childFormName).replace('%f',fieldName))
        self.clickElem(closeElem)




    #获取可写状态的日期组件的值
    def Date_GetValue_writable( self,fieldName ):
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.Date_input_loc.replace('%s',fieldName))
        return self.getElemAttrValue(elem,"value")