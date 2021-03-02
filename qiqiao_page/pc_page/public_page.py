# coding=utf-8
from public.selenium_page import SeleniumPage


class PublicPage(SeleniumPage):
    """公共区域"""

    Alert_loc = "//div[@role='alert']//p"  # 表单消息弹框

    def Public_GetAlertMessage( self ):
        """获取表单消息提示"""
        #等待弹框出现
        # self.wait_elem_visible_CSS(self.Form_Alert_loc,timeout=5)
        #返回弹框文本值
        return self.find_elemByXPATH_visibility(self.Alert_loc,timeout=10).text
