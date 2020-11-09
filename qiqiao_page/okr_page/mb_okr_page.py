# coding=utf-8
import time

from public.selenium_page import SeleniumPage


class MbOkrPage(SeleniumPage):
    '''OKR页面'''

    O_loc = "//*[@id='app']/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/p[1]"

    kr_loc = "//*[@id='app']/div/div/div[2]/div[2]/div/div/div/div[2]/div[%n]/div[2]/p"

    iframeElem = "//iframe"

    def MbOkrPage_switch_iframeElem( self ):
        '''切换进OKR页面的iframe'''
        elem = self.find_elemByXPATH_presence(self.iframeElem)
        if(elem!=None):
            self.switch_to_the_iframe(elem)
        else:
            pass

    def MbOkrPage_get_O( self ):
        '''获取目标'''
        elem = self.find_elemByXPATH_presence(self.O_loc)
        if(elem!=None):
            return elem.text
        return None


    def MbOkrPage_get_KRs(self,krNumber):
        '''获取KRs'''
        elem = self.find_elemByXPATH_presence(self.kr_loc.replace('%n',str(krNumber)))
        if(elem!=None):
            return elem.text
        return None







