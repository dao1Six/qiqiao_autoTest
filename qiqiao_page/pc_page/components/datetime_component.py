#日期时间组件
from public.selenium_page import SeleniumPage


class DateTime(SeleniumPage):

    DateTime_input_loc = "//div[@data-mark='%s']//input"  # 日期时间组件输入框
    DateTime_label_loc = "div[data-mark='%s']>label>span[title='%title']"   # 日期时间组件字段标题

    #给日期时间组件输入值
    def DateTime_Sendkeys(self,fieldName,dateTimekey,*args):
        '''给日期时间组件输入值
        fieldName：字段标题
        datakey：日期值 格式：2018-11-22
        timekey：时间值 格式：19:20
        '''
        locator = self.DateTime_input_loc.replace('%s',fieldName)
        self.sendkeysElemByXpath_visibility(locator,dateTimekey)
        # dataElem = self.find_elemsByXPATH_presence(locator)[0]
        # timeElem = self.find_elemsByXPATH_presence(locator)[1]
        # dataElem.send_keys(datekey)
        # timeElem.send_keys(timekey)
        self.clickElemByCSS_visibility(self.DateTime_label_loc.replace('%s',fieldName).replace('%title',fieldName))


    def DateTime_GetValue_writable( self,fieldName ):
        '''获取可写状态的日期时间组件的值'''
        elem = self.find_elemsByXPATH_visibility(self.DateTime_input_loc.replace('%s',fieldName))[0]
        return self.getElemAttrValue(elem,"value")