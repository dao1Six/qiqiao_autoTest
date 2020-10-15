#选择组件
import time

from public.selenium_page import SeleniumPage


class MbSelection(SeleniumPage):

    Selection_Option_loc = "//div[@title='%s']//span[text()='%option']/parent::label[1]"  # 单选多选选项

    Radio_Option_loc ="//div[@title='%s']//span[@class='cube-radio-label' and text()='%title']/parent::label[1]"

    Xiala_Option_loc = "//div[@class='cube-picker-content']/div[@class='cube-picker-wheel-wrapper']/div//li[text()='%title']"

    Xiala_li_loc = "//div[@class='cube-picker-content']/div[@class='cube-picker-wheel-wrapper']/div//ul/li"

    placeholder_loc = "//div[@title='%s']//span[@class='icon']"

    Xiala_confirm_loc = "//h1[text()='%s']/parent::div[1]/preceding-sibling::span[@class='cube-picker-confirm']"

    ChildFormPopup_SingleXiala_divReadonlyValue_loc = "//div[@title='%title']//div[@class='readonly_value']"

    ChildFormPopup_SingleBox_liReadonlyValue_loc = "//div[@title='%title']//li[@class='item_li']"

#单项

    def MbSelection_SingleXiala_Senkeys( self,fieldName,option):
        '''单项下拉字段输入值'''
        #option---字符串，选项值
        # 点击选择框
        self.clickElemByXpath_visibility(self.placeholder_loc.replace('%s',fieldName))
        clickElemIndex = 0
        # 当目标元素可见时点击
        while(self.isClickable(self.Xiala_Option_loc.replace('%title',option),timeout=3)!=True):
            clickElemIndex = clickElemIndex+1
            # self.h5_tap_elem(self.find_elemsByXPATH_presence(self.Xiala_li_loc,index=clickElemIndex))
            self.h5_tap_elem(self.find_elemsByXPATH_visibility(self.Xiala_li_loc)[clickElemIndex])
        if (self.isClickable(self.Xiala_Option_loc.replace('%title', option),timeout=3) == True):
            self.h5_tap_elem(self.find_elemsByXPATH_visibility(
                self.Xiala_Option_loc.replace('%title',option))[0])
        #点击确定按钮
        time.sleep(1)
        self.clickElemByXpath_visibility(self.Xiala_confirm_loc.replace('%s',fieldName))


    def MbSelection_SingleBox_Senkeys( self,fieldName,option):
        '''单项字段输入值'''
        self.clickElemByXpath_visibility(self.Radio_Option_loc.replace('%s',fieldName).replace('%title',option))

    def MbSelection_SingleXiala_readOnly_InPopup( self,fieldName ):
        '''在表单弹窗里获取只读状态下的单项下拉框组件值'''
        loc = self.ChildFormPopup_SingleXiala_divReadonlyValue_loc.replace('%title',fieldName)
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(loc)
        return elem.text

    def MbSelection_SingleBox_readOnly_InPopup( self,fieldName ):
        '''在表单弹窗里获取只读状态下的单项选择框组件值'''
        loc = self.ChildFormPopup_SingleBox_liReadonlyValue_loc.replace('%title',fieldName)
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(loc)
        return elem.text


#多项

    def MbSelection_MultiBox_Sendkeys(self,fieldName,list,*args):
        '''给多项选择组件输入值
        fieldName：字段标题
        list：多项选项 list里存放选项文本值
        '''
        for i in list:
            self.clickElemByXpath_visibility(self.Selection_Option_loc.replace('%s',fieldName).replace('%option',i))







