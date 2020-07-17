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



    def Selection_CheckboxSelect_Sendkeys(self,fieldName,list,*args):
        '''给多项选择组件输入值
        fieldName：字段标题
        list：多项选项 list里存放选项文本值
        '''
        for i in list:
            self.clickElemByXpath_visibility(self.Selection_Option_loc.replace('%s',fieldName).replace('%option',i))

    def MbSelection_Radio_Senkeys( self,fieldName,option):
        '''单选字段输入值'''
        self.clickElemByXpath_visibility(self.Radio_Option_loc.replace('%s',fieldName).replace('%title',option))


    def MbSelection_Xiala_Senkeys( self,fieldName,option):
        '''下拉字段输入值'''

        # 点击选择框
        self.clickElemByXpath_visibility(self.placeholder_loc.replace('%s',fieldName))
        clickElemIndex = 0
        # 当目标元素可见时点击
        while(self.isClickable(self.Xiala_Option_loc.replace('%title',option))!=True):
            clickElemIndex = clickElemIndex+1
            self.h5_tap_elem(self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.Xiala_li_loc,index=clickElemIndex))
        if (self.isClickable(self.Xiala_Option_loc.replace('%title', option)) == True):
            print("目标下拉元素已可见")
            self.h5_tap_elem(self.find_elenmInElemsByXpath_visibility_of_any_elements_located(
                self.Xiala_Option_loc.replace('%title',option)))
        #点击确定按钮
        time.sleep(3)
        self.clickElemByXpath_visibility(self.Xiala_confirm_loc.replace('%s',fieldName))


