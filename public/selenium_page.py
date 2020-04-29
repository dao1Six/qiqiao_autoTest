# coding=utf-8
import time
import traceback
from logging import exception

from retrying import retry
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC


class SeleniumPage (object):
    """
    基础类，用于页面对象类的继承
    """

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """打开登录页面"""
        self.driver.get (url)



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

    ####点击元素方法







    @retry (stop_max_attempt_number=5, wait_fixed=2000)
    def clickElemByXpath_Presence(self, locator, timeout=2):
        """点击单个存在dom的元素Xpath"""
        elem = WebDriverWait (self.driver, timeout).until (EC.presence_of_element_located ((By.XPATH, locator)))
        self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        elem.click ()

    @retry (stop_max_attempt_number=5, wait_fixed=2000)
    def clickElemByCSS_Presence(self, locator, timeout=2):
        """点击单个存在dom的元素CSS"""
        # elem = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        # self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        elem = self.scrollIntoView (locator)
        elem.click ()

    @retry (stop_max_attempt_number=5, wait_fixed=2000)
    def clickElemsByCSS_Presence(self, locator, num=0, timeout=2):
        """点击存在dom里的元素组里的某个元素CSS"""
        elems = WebDriverWait (self.driver, timeout).until (
            EC.presence_of_all_elements_located ((By.CSS_SELECTOR, locator)))
        self.driver.execute_script ("arguments[0].scrollIntoView();", elems[num])
        elems[num].click ()

    ####元素写值方法

    @retry (stop_max_attempt_number=5, wait_fixed=2000)
    def sendkeysElemByXpath_Presence(self, locator, key, timeout=2):
        """给一个存在dom的元素写入值Xpath"""
        elem = WebDriverWait (self.driver, timeout).until (EC.presence_of_element_located ((By.XPATH, locator)))
        self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        elem.send_keys (key)

    @retry (stop_max_attempt_number=5, wait_fixed=2000)
    def sendkeysElemByCSS_Presence(self, locator, key, timeout=2):
        """给存在dom里的元素组里的某个元素写入值CSS"""
        elem = WebDriverWait (self.driver, timeout).until (EC.presence_of_element_located ((By.CSS_SELECTOR, locator)))
        self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        elem.clear ()
        elem.send_keys (key)

    @retry (stop_max_attempt_number=5, wait_fixed=2000)
    def sendkeysElemsByCSS_Presence(self, locator, key, num=0, timeout=2):
        """给存在dom里的元素组里的某个元素写入值CSS"""
        elems = WebDriverWait (self.driver, timeout).until (
            EC.presence_of_all_elements_located ((By.CSS_SELECTOR, locator)))
        self.driver.execute_script ("arguments[0].scrollIntoView();", elems[num])
        elems[num].clear ()
        elems[num].send_keys (key)



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


