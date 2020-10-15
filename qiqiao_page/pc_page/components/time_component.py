#时间组件
import time

from public.selenium_page import SeleniumPage


class Time(SeleniumPage):

    Time_input_loc = "//div[@data-mark='%s']//input[@class='el-input__inner']"  #时间组件字段输入框

    Time_label_loc = "div[data-mark='%s']>label>span[title='%s']"  #时间组件字段名

    #
    def Time_Sendkeys(self,fieldName,key,*args):
        '''给时间组件输入值
        fieldName：字段标题
        key：时间值  格式：19:20
        '''
        locator = self.Time_input_loc.replace('%s',fieldName)
        self.clickElemByXpath_visibility(locator)
        time.sleep(1)
        self.sendkeysElemByXpath_visibility(locator, key,isclear=True)
        #点击字段标题
        self.clickElemByCSS_visibility(self.Time_label_loc.replace('%s',fieldName))


    def Time_GetValue_writable( self,fieldName ):
        '''获取可写状态的时间组件的值'''
        elem = self.find_elemsByXPATH_presence(self.Time_input_loc.replace('%s',fieldName))[0]
        return self.getElemAttrValue(elem,"value")