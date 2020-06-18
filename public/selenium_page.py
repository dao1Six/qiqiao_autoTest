# coding=utf-8
import time
import traceback
from functools import singledispatch
from logging import exception

import selenium
from retrying import retry
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class SeleniumPage (object):
    """
    基础类，用于页面对象类的继承
    """

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """打开登录页面"""
        self.driver.get (url)

    def dynamicScroll( self ):
        '''动态滚动'''
        for n in range(1,5):
            self.driver.execute_script('document.querySelector(".myScroll_main").scrollTop = 10000')  # 从上往下滑

    def wait_elem_visible(self, locator, timeout=5):
        # 一直等待某元素可见，默认超时3秒只做等待动作不返回值
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException as ex:
            print('wait_elem_visible 异常：%s 获取 %s 超时' % (ex, locator))

    def wait_elem_disappearByCSS(self, locator, timeout=3):
        # 一直等待某个元素消失，默认超时3秒只做等待动作不返回值
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException as ex:
            print('wait_elem_visible 异常：%s 获取 %s 超时' % (ex, locator))

    #长按元素
    def click_and_hold( self,elem):
        ActionChains(self.driver).click_and_hold(elem).perform()



    def scrollIntoView(self, locator, timeout=2, *args):
        """将元素拖动到可见区域"""
        if args is not None:
            elems = WebDriverWait (self.driver, timeout).until (
                EC.presence_of_all_elements_located ((By.CSS_SELECTOR, locator)))
            self.driver.execute_script ("arguments[0].scrollIntoView();", elems[args])
            return elems[args]
        else:
            elem = WebDriverWait (self.driver, timeout).until (
                EC.presence_of_element_located ((By.CSS_SELECTOR, locator)))
            self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
            return elem


    def getElemAttrValue(self,element,name):
        '''根据属性名获取元素属性值'''
        if element is not None:
            return element.get_attribute(name)
        else:
            print('page-->get_attr,NoneType没有属性')

    ####点击元素方法



    @retry (stop_max_attempt_number=5, wait_fixed=2000)
    def clickElemByXpath_Presence(self, locator, index=0):
        """点击单个存在dom的元素Xpath"""
        if(type(locator)==str):
            elem = self.find_elenmInElemsByXpath(locator,index)
            if(elem is not None and elem.is_displayed()):
                self.clickElem(elem)
            else:
                self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
                self.clickElem(elem)
        elif(type(locator)==selenium.webdriver.remote.webelement.WebElement):
            elem = locator
            if(elem is not None and elem.is_displayed()):
                self.clickElem(elem)
            else:
                self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
                self.clickElem(elem)




    @retry (stop_max_attempt_number=5, wait_fixed=2000)
    def clickElemByCSS_Presence(self, locator,index = 0):
        """点击单个存在dom的元素CSS"""
        elem = self.find_elenmInElemsByCSS(locator,index)
        self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        elem.click ()

    @retry (stop_max_attempt_number=5, wait_fixed=2000)
    def clickElem(self, elem):
        """给一个存在dom的元素写入值Xpath"""
        self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        elem.click()



    ####元素写值方法

    @retry (stop_max_attempt_number=5, wait_fixed=2000)
    def sendkeysElemByXpath_Presence(self, locator, key, index=0):
        """给一个存在dom的元素写入值Xpath"""
        elem = self.find_elenmInElemsByXpath(locator,index)
        self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        elem.clear()
        elem.send_keys (key)

    @retry (stop_max_attempt_number=5, wait_fixed=2000)
    def sendkeysElem(self, elem, key):
        """给一个存在dom的元素写入值Xpath"""
        self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        elem.clear()
        elem.send_keys (key)

    @retry (stop_max_attempt_number=5, wait_fixed=2000)
    def sendkeysElemByCSS_Presence(self, locator, key, index=0):
        """给存在dom里的元素组里的某个元素写入值CSS"""
        elem = self.find_elenmInElemsByCSS(locator, index)
        self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        # elem.clear ()
        elem.send_keys (key)


    #################
    # 查找元素方法
    def find_elemByCSS(self, locator, timeout=5):
        '''判断5s内，定位的元素是否存在dom结构里。存在则返回元素，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        except:
            return None


    def find_elemByXPATH(self, locator, timeout=5):
        '''判断5s内，定位的元素是否存在dom结构里。存在则返回元素，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, locator)))
        except:
            return None


    def find_elemsByCSS(self, locator, timeout=5):
        '''判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator)))
        except:
            return None

    def find_elenmInElemsByCSS(self, locator, index=0,timeout=5):
        '''判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator)))[index]
        except:
            print(locator + "页面无此元素")
            return None

    def find_elenmInElemsByXpath(self, locator, index=0,timeout=5):
        '''判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, locator)))[index]
        except:
            print(locator+"页面无此元素")
            return None

    def find_elemsByXPATH(self, locator, timeout=5):
        '''判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, locator)))
        except:
            return None





##栋一
    @retry (stop_max_attempt_number=5, wait_fixed=2000)
    def addAttributeElemsByXpath_Presence(self, locator, attributename,value, timeout=2):
        """给元素添加属性值，添加人（王栋一）"""
        element = WebDriverWait (self.driver, timeout).until (EC.visibility_of_element_located((By.XPATH, locator)))
        try:
            self.driver.execute_script("arguments[0].%s=arguments[1]" %attributename,element,value)

        except TimeoutException:
            print("等待元素超时！！")
            raise

    @retry (stop_max_attempt_number=5, wait_fixed=2000)
    def refreshCurrentPage(self):
        """刷新当前页面，添加人（王栋一）"""
        time.sleep(1)
        self.driver.refresh()

    @retry(stop_max_attempt_number=5, wait_fixed=2000)
    def waiteElemsByXpath(self, locator,  timeout=2):
        """通过xpath等待元素出现，添加人（王栋一）"""
        element = WebDriverWait (self.driver, timeout).until (EC.visibility_of_element_located((By.XPATH, locator)))
        return element

    @retry(stop_max_attempt_number=5, wait_fixed=2000)
    def findElemsByXpath(self, locator):
        '''通过xpath查看找多个元素，添加人（王栋一）'''
        elements = self.driver.find_elements("xpath", locator)
        return elements

    @retry(stop_max_attempt_number=5, wait_fixed=2000)
    def js(self,js,element):
        '''执行就是脚本，添加人（王栋一）'''
        self.driver.execute_script(js,element)


    def clear(self, css):
        """
        清除输入框的内容.
        用法:
        driver.clear("css=>#el")
        """
        el = self.waiteElemsByXpath(css)
        el.clear()


    def getText(self, css):
        """
        获得元素文本信息
        用法:
        driver.get_text("css=>#el")
        """
        el = self.waiteElemsByXpath(css)
        return el.text


