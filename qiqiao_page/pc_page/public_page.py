# coding=utf-8
from public.selenium_page import SeleniumPage


class PublicPage(SeleniumPage):
    '''公共区域'''

    Alert_loc = "//div[@role='alert']//p"  # 表单消息弹框

    def Public_GetAlertMessage( self ):
        '''获取表单消息提示'''
        #等待弹框出现
        # self.wait_elem_visible(self.Form_Alert_loc,timeout=10)
        #返回弹框文本值
        return self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.Alert_loc,timeout=10).text
