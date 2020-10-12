# coding=utf-8
import time

from public.selenium_page import SeleniumPage


class MbPublicPage(SeleniumPage):
    '''公共区域'''

    Alert_loc = "//div[@class='cube-popup cube-popup_mask cube-toast myToast_correct']//div[@class='cube-toast-tip']"
    # 表单消息弹框

    LoadingAlert_loc = "//div[@class='cube-toast-tip' and text()='加载中']"

    def Public_GetAlertMessage( self ):
        '''获取表单消息提示'''
        #返回弹框文本值
        # self.Public_LoadingAlert_disappear()
        return self.find_elemByXPATH_visibility(self.Alert_loc,timeout=5).text


    def Public_Alert_disappear( self ):
        '''等待消息框消失'''
        self.wait_elem_visible_XPATH(self.Alert_loc)
        self.wait_elem_disappearByXPATH(self.Alert_loc)


    def Public_LoadingAlert_disappear( self ):
        '''等待加载中提示消失'''
        self.wait_elem_visible_XPATH(self.LoadingAlert_loc)
        if(self.wait_elem_disappearByXPATH(self.LoadingAlert_loc)):
            print("加载中提示已经消失")
        else:
            print("加载中提示没有消失")
