#日期组件
from public.selenium_page import SeleniumPage


class MbDate(SeleniumPage):


    dateTxr_loc = "div[title='%s'] div.tx_r"



    #获取日期字段的值
    def GetDateVale(self,fieldName):
        elem = self.find_elenmInElemsByCSS_visibility_of_any_elements_located(self.dateTxr_loc.replace('%s',fieldName))
        value = elem.text
        return value

