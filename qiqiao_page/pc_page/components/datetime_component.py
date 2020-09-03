#日期时间组件
from public.selenium_page import SeleniumPage


class DateTime(SeleniumPage):

    DateTime_input_loc = "//div[@data-mark='%s']//input"  # 日期时间组件输入框
    DateTime_label_loc = "div[title='%s']>label>span[title='%title']"   # 日期时间组件字段标题

    #给日期时间组件输入值
    def DateTime_Sendkeys(self,fieldName,datekey,timekey,*args):
        '''给日期时间组件输入值
        fieldName：字段标题
        datakey：日期值 格式：2018-11-22
        timekey：时间值 格式：19:20
        '''
        locator = self.DateTime_input_loc.replace('%s',fieldName)
        dataElem = self.find_elemsByCSS(locator)[0]
        timeElem = self.find_elemsByCSS(locator)[1]
        dataElem.send_keys(datekey)
        timeElem.send_keys(timekey)
        self.clickElemByCSS_visibility(self.DateTime_label_loc.replace('%s',fieldName).replace('%title',fieldName))


    def DateTime_GetValue_writable( self,fieldName ):
        '''获取可写状态的日期时间组件的值'''
        elem = self.find_elemByXPATH_visibility(self.DateTime_input_loc.replace('%s',fieldName))
        return self.getElemAttrValue(elem,"value")