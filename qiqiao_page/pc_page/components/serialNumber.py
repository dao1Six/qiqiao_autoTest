#生成编码组件
from public.selenium_page import SeleniumPage


class SerialNumber(SeleniumPage):


    ChildFormPopup_loc="//div[@data-mark='子表弹层_%s']"
    ChildFormPopup_SerialNumber_span_loc="//div[@title='%title']//div[contains(@class,'component_detail')]//span"

    def SerialNumber_GetValue_readOnly_InPopup( self,childFormName,fieldName ):
        """表单弹层获取只读状态的生成编码字段值"""
        loc = self.ChildFormPopup_loc.replace('%s',childFormName) + self.ChildFormPopup_SerialNumber_span_loc.replace('%title',fieldName)
        elem = self.find_elemByXPATH_visibility(loc)
        return elem.text