#外键
import time

from selenium.webdriver.common.keys import Keys

from Enum.buttonEnum import ButtonEnum
from public.selenium_page import SeleniumPage


class ForeignSelection_component(SeleniumPage):

    ForeignSelectionBox_loc = "//div[@data-mark='%title']//input"

    ForeignSelectOption_loc = "//li[@data-mark='option_%s']"

    foreignSelectOptions_loc = "//li[contains(@data-mark,'option_')]"#"//div[@class='el-select-dropdown el-popper %s']//li[contains(@data-mark,'option_')]"

    foreign_el_popper = "//div[@class='el-select-dropdown el-popper %s']"

    aa = "el-select-dropdown el-popper %s"

    ChildFormPopup_loc = "//div[@data-mark='子表弹层_%s']"

    ChildFormPopup_ForeignSelectionBox_Input_loc = "//div[@title='%title']//input"

    ChildFormPopup_ForeignSelectionBox_span_loc = "//div[@title='%title']//div[contains(@class,'component_detail')]//div//span"

    dialog_span = "//div[@aria-label='选择内容']//tr//td//span"
    dialog_searchinput = "//div[@aria-label='选择内容']//input"

    dialog_SelectOption = "//div[@aria-label='选择内容']//span[@title='%s']"

    dialog_btn_prev = "//div[@aria-label='选择内容']//button[@class='btn-prev']"
    dialog_btn_next = "//div[@aria-label='选择内容']//button[@class='btn-next']"

    def ForeignSelection_Sendkeys(self,fieldName,value,index1=0,index2=0,*args):
        '''外键选择组件输入值'''
        # fieldName：字段标题
        loc = self.ForeignSelectionBox_loc.replace('%title',fieldName)
        #点击外键的输入框
        self.clickElemByXpath_visibility(loc,index=index1)
        #点击选项
        self.clickElemByXpath_visibility(self.ForeignSelectOption_loc.replace('%s',value),index=index2)

    def ForeignSelection_SelectionBox_Click(self,fieldName,index1=0,*args):
        '''外键选择组件输入值'''
        # fieldName：字段标题
        loc = self.ForeignSelectionBox_loc.replace('%title',fieldName)
        #点击外键的输入框
        self.clickElemByXpath_visibility(loc,index=index1)

    def ForeignSelection_SelectOption_isExist(self,value,*args):
        '''外键选项是否存在'''
        elem = self.find_elemByXPATH_visibility(self.ForeignSelectOption_loc.replace('%s',value))
        if(elem!=None):
            return True
        return False


    def ForeignSelection_get_OptionValue(self,fieldName,*args):
        '''获取外键选择组件选项值'''
        list = []
        elems = self.find_elemsByXPATH_presence(self.foreignSelectOptions_loc)#.replace('%s',fieldName)
        if elems == None:
            return list
        for elem in elems:
            list.append(elem.text)
        return list

    def ForeignSelection_Option_scrollDown( self,fieldName,scrollNumber=10):
        '''外键选项滚动至底部'''
        js = "document.getElementsByClassName('%s')[0].children[0].children[0].scrollTop=1000" %fieldName
        for n in range(1,scrollNumber):
            self.driver.execute_script(js)  # 从上往下滑
            time.sleep(0.5)



    def ForeignSelection_InPopup_Sendkeys( self,childFormName,fieldName,value,*args ):
        '''子表弹框输入外键值'''
        loc = self.ChildFormPopup_loc.replace('%s',childFormName)+self.ChildFormPopup_ForeignSelectionBox_Input_loc.replace('%title',fieldName)
        #点击外键的输入框
        self.clickElemByXpath_visibility(loc)
        #点击选项
        self.clickElemByXpath_visibility(self.ForeignSelectOption_loc.replace('%s',value))


    def ForeignSelection_GetValue_writable_InPopup( self,childFormName,fieldName ):
        '''表单弹层获取可写状态的外键字段值'''
        loc = self.ChildFormPopup_loc.replace('%s',childFormName) + self.ChildFormPopup_ForeignSelectionBox_Input_loc.replace('%title',fieldName)
        return self.getElemAttrValue(self.find_elenmInElemsByXpath_visibility_of_any_elements_located(loc),'value')



    def ForeignSelection_GetValue_readOnly_InPopup( self,childFormName,fieldName ):
        '''表单弹层获取只读状态的外键字段值'''
        loc = self.ChildFormPopup_loc.replace('%s',childFormName) + self.ChildFormPopup_ForeignSelectionBox_span_loc.replace('%title',fieldName)
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(loc)
        return elem.text



############
    # 外键弹窗操作
    def ForeignSelection_fanye_InDialog( self,buttonNumber):
        '''外键弹窗点击翻页按钮'''
        if(buttonNumber==ButtonEnum.UP.value):
            self.clickElemByXpath_visibility(self.dialog_btn_prev)
        if(buttonNumber==ButtonEnum.DOWN.value):
            self.clickElemByXpath_visibility(self.dialog_btn_next)
        else:
            raise ValueError('没有此button枚举值：%s' %buttonNumber)



    def ForeignSelection_GetValue_InDialog( self ):
        '''获取外键弹窗当前页的选项值'''
        list = []
        elems = self.find_elemsByXPATH_presence(self.dialog_span)
        if elems == None:
            return list
        for elem in elems:
            list.append(elem.text)
        return list

    def ForeignSelection_SearchaInputSendkeys_InDialog( self,value ):
        '''外键弹窗搜索框输入值'''
        self.sendkeysElemByXpath_visibility(self.dialog_searchinput,key=value)


    def ForeignSelection_ClickOption_InDialog( self,value ):
        '''外键弹窗点击选项'''
        self.clickElemByXpath_visibility(self.dialog_SelectOption.replace("%s",value))




