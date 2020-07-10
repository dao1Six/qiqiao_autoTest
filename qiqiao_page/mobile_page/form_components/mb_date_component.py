#日期组件
from public.selenium_page import SeleniumPage


class MbDate(SeleniumPage):
    '''日期组件'''

    dateTxr_loc = "div[title='%s'] div.tx_r"

    icon_loc = "//div[@title='%s']//span[@class='icon']"

    datali_loc = "//div[@class='cube-picker-content']/div[@class='cube-picker-wheel-wrapper']/div[%n]//li[text()='%value']"

    confirm_loc = "//span[@class='cube-picker-confirm']"

    #获取日期字段的值
    def MbDate_GetVale(self,fieldName):
        elem = self.find_elenmInElemsByCSS_visibility_of_any_elements_located(self.dateTxr_loc.replace('%s',fieldName))
        value = elem.text
        return value


    def MbDate_SendKeys( self ,fieldName,key):
        '''日期组件输入值'''
        #点击日期下拉图标
        self.clickElemByXpath_visibility(self.icon_loc.replace('%s',fieldName))
        keyList = key.split("-")
        for i,key in zip(range(1,len(keyList)+1),keyList):
            keyValue = key
            if(len(key)==2 and list(key)[0]=="0" ):
                keyValue = list(key)[1]
            self.clickElemByXpath_visibility(self.datali_loc.replace('%n',str(i)).replace('%value',keyValue))
        #点击确定按钮
        self.clickElemByXpath_visibility(self.confirm_loc)


