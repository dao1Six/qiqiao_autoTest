#日期组件
import time

from selenium import webdriver
from selenium.webdriver import TouchActions

from public.selenium_page import SeleniumPage
from appium.webdriver.common.touch_action import TouchAction

from util.dateTimeUtil import DateTimeUtil


class MbDate(SeleniumPage):
    '''日期组件'''

    dateTxr_loc = "div[title='%s'] div.tx_r"

    icon_loc = "//div[@title='%s']//span[@class='icon']"

    datali_loc = "//div[@class='cube-picker-content']/div[@class='cube-picker-wheel-wrapper']/div[%n]//li[text()='%value']"

    Firstdatali_loc = "//div[@class='cube-picker-content']/div[@class='cube-picker-wheel-wrapper']/div[%n]/ul/li"


    confirm_loc = "//span[@class='cube-picker-confirm']"

    #获取日期字段的值
    def MbDate_GetVale(self,fieldName):
        elem = self.find_elenmInElemsByCSS_visibility_of_any_elements_located(self.dateTxr_loc.replace('%s',fieldName))
        value = elem.text
        return value


    def MbDate_SendKeys( self ,fieldName,key):
        '''日期组件输入值'''
        #点击日期下拉图标
        #点击下拉框
        self.clickElemByXpath_visibility(self.icon_loc.replace('%s',fieldName))
        time.sleep(3)
        action = webdriver.TouchActions(self.driver)


        today = DateTimeUtil().Today()
        todayList = today.split("-")
        keyList = key.split("-")
        #选择年
        yeardiff = int(todayList[0])-int(keyList[0]) #当前年-目标年
        clickYear = todayList[0]
        tyear = keyList[0]
        while (clickYear != tyear):
            if(yeardiff>0):#
                clickYear = str(int(clickYear)+1)
                self.h5_tap_elem(self.find_elemsByXPATH_presence(self.datali_loc.replace('%n', str(1)).
                                                                                                  replace('%value', clickYear))[0]) #往下点击一个元素
                time.sleep(1)
            if (yeardiff < 0):  #
                clickYear = str(int(clickYear) - 1)
                self.h5_tap_elem(self.find_elemsByXPATH_presence(self.datali_loc.replace('%n', str(1)).
                                                                                                  replace('%value', clickYear))[0])  # 往上点击一个元素
                time.sleep(1)
        self.h5_tap_elem(self.find_elemsByXPATH_presence(self.datali_loc.replace('%n',str(1)).replace('%value',tyear))[0])

        #选择月

        cmonthValue = todayList[1] #当前的月份值
        if(len(todayList[1])==2 and list(todayList[1])[0]=="0"):
            cmonthValue = list(todayList[1])[1]
        clickMonth = cmonthValue  # 点击的月份值
        tmonthValue = keyList[1]  #目标月份值
        if(len(keyList[1])==2 and list(keyList[1])[0]=="0"):
            tmonthValue = list(keyList[1])[1]
        #判断的目标月是否可以点击
        if(self.find_elemsByXPATH_visibility(self.datali_loc.replace('%n', str(2)).replace('%value', tmonthValue))!=None):
            self.h5_tap_elem(self.find_elemsByXPATH_presence(self.datali_loc.replace('%n',str(2)).replace('%value',tmonthValue))[0])
        else:
            monthdiff = int(cmonthValue) - int(tmonthValue)
            while (clickMonth != tmonthValue):
                if(monthdiff>0):
                    clickMonth = str(int(clickMonth) - 1)
                    self.h5_tap_elem(self.find_elemsByXPATH_presence(self.datali_loc.replace('%n', str(2)).
                                                                                                      replace('%value', clickMonth))[0])  # 往下点击一个元素
                    time.sleep(1)
                if(monthdiff<0):
                    clickMonth = str(int(clickMonth) + 1)
                    self.h5_tap_elem(self.find_elemsByXPATH_presence(self.datali_loc.replace('%n', str(2)).
                                                                                                      replace('%value', clickMonth))[0])  # 往上点击一个元素
                    time.sleep(1)
                    self.h5_tap_elem(self.find_elenmInElemsByXpath_visibility_of_any_elements_located(
                self.datali_loc.replace('%n',str(2)).replace('%value',tmonthValue)))

        time.sleep(1)
        #选择日
        cdayValue = todayList[2]  #当前日期
        if(len(todayList[2])==2 and list(todayList[2])[0]=="0"):
            cdayValue = list(todayList[2])[1]
        clickDay = cdayValue  # 点击的日值
        tdayValue = keyList[2]
        if(len(keyList[2])==2 and list(keyList[2])[0]=="0"):
            tdayValue = list(keyList[2])[1]
        #判断的目标日期是否可以点击
        if(self.find_elemsByXPATH_visibility(self.datali_loc.replace('%n', str(3)).replace('%value', tdayValue))!=None):
            self.h5_tap_elem(self.find_elemsByXPATH_presence(self.datali_loc.replace('%n',str(3)).replace('%value',tdayValue))[0])
        else:
            daydiff = int(cdayValue) - int(tdayValue)
            while(clickDay!=tdayValue):
                if (daydiff > 0):
                    clickDay = str(int(clickDay) - 1)
                    self.h5_tap_elem(self.find_elemsByXPATH_presence(self.datali_loc.replace('%n', str(3)).
                                                                                                      replace('%value', clickDay))[0])  # 往下点击一个元素
                    time.sleep(1)
                if (daydiff < 0):
                    clickDay = str(int(clickDay) + 1)
                    self.h5_tap_elem(self.find_elemsByXPATH_presence(self.datali_loc.replace('%n', str(3)).
                                                                                                      replace('%value', clickDay))[0]) # 往上点击一个元素
                    time.sleep(1)
            self.h5_tap_elem(self.find_elemsByXPATH_presence(self.datali_loc.replace('%n',str(3)).replace('%value',tdayValue))[0])
        time.sleep(1)
        #点击确定按钮
        self.clickElemByXpath_visibility(self.confirm_loc)
        time.sleep(2)


