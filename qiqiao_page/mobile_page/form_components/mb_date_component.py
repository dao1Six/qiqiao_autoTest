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
        yeardiff = int(todayList[0])-int(keyList[0])

        #当目标元素可见时点击
        while(self.isClickable(self.datali_loc.replace('%n',str(1)).replace('%value',keyList[0]))!=True):
            cyear_elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(
                self.Firstdatali_loc.replace('%n',str(1)))
            action.flick_element(cyear_elem, 0, -14*yeardiff,5).perform()
        if(self.isClickable(self.datali_loc.replace('%n',str(1)).replace('%value',keyList[0]))==True):
            self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.datali_loc.replace('%n',str(1)).replace('%value',keyList[0])).click()

        #选择月
        cmonthValue = todayList[1]
        if(len(todayList[1])==2 and list(todayList[1])[0]=="0"):
            cmonthValue = list(todayList[1])[1]
        tmonthValue = keyList[1]
        if(len(keyList[1])==2 and list(keyList[1])[0]=="0"):
            tmonthValue = list(keyList[1])[1]
        monthdiff = int(cmonthValue) - int(tmonthValue)
        #当目标元素可见时点击
        while(self.isClickable(self.datali_loc.replace('%n',str(2)).replace('%value',tmonthValue))!=True):
            cmonth_elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(
                self.Firstdatali_loc.replace('%n',str(2)))
            action.flick_element(cmonth_elem, 0, -14*monthdiff,5).perform()
        if(self.isClickable(self.datali_loc.replace('%n',str(2)).replace('%value',tmonthValue))==True):
            self.find_elenmInElemsByXpath_visibility_of_any_elements_located(
                self.datali_loc.replace('%n',str(2)).replace('%value',tmonthValue)).click()

        #选择日
        cdayValue = todayList[2]
        if(len(todayList[2])==2 and list(todayList[2])[0]=="0"):
            cdayValue = list(todayList[2])[1]
        tdayValue = keyList[2]
        if(len(keyList[2])==2 and list(keyList[2])[0]=="0"):
            tdayValue = list(keyList[2])[1]
        daydiff = int(cdayValue) - int(tdayValue)
        #当目标元素可见时点击
        while(self.isClickable(self.datali_loc.replace('%n',str(3)).replace('%value',tdayValue))!=True):
            cday_elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(
                self.Firstdatali_loc.replace('%n',str(3)))
            action.flick_element(cday_elem, 0, -14*daydiff,5).perform()
        if(self.isClickable(self.datali_loc.replace('%n',str(3)).replace('%value',tdayValue))==True):
            self.find_elenmInElemsByXpath_visibility_of_any_elements_located(
                self.datali_loc.replace('%n',str(3)).replace('%value',tdayValue)).click()

        time.sleep(2)
        #点击确定按钮
        self.clickElemByXpath_visibility(self.confirm_loc)
        time.sleep(2)


