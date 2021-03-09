# coding=utf-8
import datetime
import time
import traceback
from functools import singledispatch
from logging import exception

import selenium
from retrying import retry
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui


class SeleniumPage (object):
    """
    基础类，用于页面对象类的继承
    """

    def __init__(self, driver):
        self.driver = driver



    def switch_to_the_iframe(self, iframeElem):
        '''切换到指定的iframe页面'''
        self.driver.switch_to.frame(iframeElem)


    def switch_to_default_content( self ):
        '''从frame中切回主文档'''
        #切到frame中之后，我们便不能继续操作主文档的元素，这时如果想操作主文档内容，则需切回主文档。
        self.driver.switch_to.default_content()


    def isClickable( self, locator,timeout = 10):
        """判断元素是否可以点击"""
        try:
            WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable((By.XPATH,locator)))
            return True
        except:
            return False

    def isOperation( self, elem):
        """判断元素是否可以操作"""
        if(elem.is_enabled()):
            return True
        return False


    def open(self, url):
        """打开登录页面"""
        self.driver.get (url)

    def dynamicScroll( self ):
        """动态滚动"""
        js = "document.getElementsByClassName('test')[0].scrollTop=100000"
        for n in range(1,5):
            self.driver.execute_script(js)  # 从上往下滑
            time.sleep(0.5)

    def wait_elem_visible_CSS(self, locator, timeout=5):
        # 一直等待某元素可见，默认超时3秒只做等待动作不返回值
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_any_elements_located((By.CSS_SELECTOR, locator)))
        except TimeoutException as ex:
            print('wait_elem_visible 异常：%s 获取 %s 超时' % (ex, locator))

    def wait_elem_disappearByCSS(self, locator, timeout=3):
        # 一直等待某个元素消失，默认超时3秒只做等待动作不返回值
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException as ex:
            print('wait_elem_visible 异常：%s 获取 %s 超时' % (ex, locator))



    def wait_elem_visible_XPATH(self, locator, timeout=5):
        # 一直等待某元素可见，默认超时3秒只做等待动作不返回值
        try:
            ui.WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located((By.XPATH,locator)))
            return True
        except TimeoutException:
            return False

    def wait_elem_disappearByXPATH(self, locator, timeout=5):
        # 一直等待某个元素消失，默认超时3秒只做等待动作不返回值
        try:
            ui.WebDriverWait(self.driver,timeout).until(EC.invisibility_of_element_located((By.XPATH,locator)))
            return True
        except TimeoutException:
            return False

    #长按元素
    def click_and_hold( self,elem):
        ActionChains(self.driver).click_and_hold(elem).perform()


    #鼠标悬浮
    def move_to_element( self,elem):
        """鼠标悬浮"""
        if(elem==None):
            raise TypeError
        ActionChains(self.driver).move_to_element(elem).perform()

    def h5_scroll(self,elem,x,y):
        """H5以元素为起点以一定速度向下滑动"""
        # 　向下滑动为负数，向上滑动为正数
        Action = TouchActions(self.driver)
        Action.scroll_from_element(elem, x,y).perform()


    def h5_tap_elem( self,elem):
        """H5点击元素"""
        Action = TouchActions(self.driver)
        try:
            Action.tap(elem).perform()
            time.sleep(1)
        except:
            pass





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
        """根据属性名获取元素属性值"""
        if element is not None:
            return element.get_attribute(name)
        else:
            print('page-->get_attr,NoneType没有属性')


    def hide_loadingMask_by_jq(self):
        """通过jq将元素隐藏"""
        script = '$("div.el-loading-mask").hide()'
        self.driver.execute_script(script)


    def hide_alert_by_jq(self):
        """通过jq将元素隐藏"""
        script = '$("div[role="alert"]").hide()'
        self.driver.execute_script(script)


########################################################################点击元素方法

    def retry_if_clickOtherelement(exception ):
        exceptionInfo = str(exception)
        if ("Other element would receive the click" in exceptionInfo):
            print(datetime.datetime.now())
            print("操作的元素被其他元素挡住导致点击失败" + exceptionInfo)
            return isinstance(exception, WebDriverException)
        elif("stale element reference: element is not attached to the page document" in exceptionInfo):
            print(datetime.datetime.now())
            print("页面刷新导致元素点击失败"+exceptionInfo)
            return isinstance(exception, WebDriverException)


    @retry( retry_on_exception=retry_if_clickOtherelement,stop_max_attempt_number=3, wait_fixed=2000,
           wrap_exception=True,stop_max_delay=5000)
    def clickElem(self, elem):
        """给一个存在dom的元素写入值Xpath"""
        #滚动元素至可见位置
        self.driver.execute_script("arguments[0].scrollIntoView();",elem)
        try:
            self.driver.execute_script('window.scrollBy(0, -100)') #向下滚动100像素
        except :
            print("sss")
        finally:
            elem.click()



    def clickElemByXpath_visibility(self, locator, index=0,timeout=5):
        """点击单个可见元素Xpath"""
        #传元素地址
        if(type(locator)==str):
            elems = self.find_elemsByXPATH_visibility(locator,timeout=timeout)
            if(elems==None):
                raise TypeError("elem不能为None")
            else:
                self.clickElem(elems[index])
        #传元素
        elif(type(locator)==selenium.webdriver.remote.webelement.WebElement):
            elem = locator
            self.clickElem(elem)

    def clickElemByXpath_clickable(self, locator):
        """点击单个可见元素Xpath"""
        #传元素地址
        if(type(locator)==str):
            elem = self.find_elemByXPATH_clickable(locator)
            if(elem==None):
                raise TypeError("elem不能为None")
            else:
                self.clickElem(elem)
        #传元素
        elif(type(locator)==selenium.webdriver.remote.webelement.WebElement):
            elem = locator
            self.clickElem(elem)




    def clickElemByXpath_presence(self, locator, index=0,timeout=5):
        """点击单个可见元素Xpath"""
        #传元素地址
        if(type(locator)==str):
            elems = self.find_elemsByXPATH_presence(locator,timeout=timeout)
            if(elems==None):
                raise TypeError("elem不能为None")
            else:
                self.clickElem(elems[index])
        #传元素
        elif(type(locator)==selenium.webdriver.remote.webelement.WebElement):
            elem = locator
            self.clickElem(elem)



    def clickElemByCSS_visibility(self, locator,index = 0):
        """点击单个可见元素CSS"""
        #传元素地址
        if(type(locator)==str):
            elems = self.find_elemsByCSS_visibility(locator)
            if(elems==None):
                raise TypeError("elem不能为None")
            else:
                self.clickElem(elems[index])
        #传元素
        elif(type(locator)==selenium.webdriver.remote.webelement.WebElement):
            elem = locator
            self.clickElem(elem)


    def clickElemByCSS_presence(self, locator,index = 0):
        """点击单个可见元素CSS"""
        #传元素地址
        if(type(locator)==str):
            elems = self.find_elemsByCSS_presence(locator)
            # elem = self.find_elenmInElemsByCSS_visibility_of_any_elements_located(locator,index=index)
            if(elems==None):
                raise TypeError("elem不能为None")
            else:
                self.clickElem(elems[index])
        #传元素
        elif(type(locator)==selenium.webdriver.remote.webelement.WebElement):
            elem = locator
            self.clickElem(elem)




    ####元素写值方法
    @retry (stop_max_attempt_number=3, wait_fixed=1500,wrap_exception=True,stop_max_delay=15000)
    def sendkeysElem(self, elem, key,isclear =False,ENTER=False):
        """给一个存在dom的元素写入值Xpath"""
        if(self.isOperation(elem)==False):
            self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        if(isclear==True):
            elem.clear()
        elem.send_keys (key)
        if(ENTER==True):
            elem.send_keys(Keys.ENTER)


    def sendkeysElemByXpath_visibility(self, locator, key, index=0,isclear=False,ENTER = False):
        """给一个存在dom的元素写入值Xpath"""
        elems = self.find_elemsByXPATH_visibility(locator)
        if (elems == None):
            raise TypeError("elem不能为None")
        else:
            self.sendkeysElem(elems[index], key,isclear=isclear,ENTER=ENTER)

    def sendkeysElemByXpath_presence(self, locator, key, index=0,isclear=False):
        """给一个存在dom的元素写入值Xpath"""
        elems = self.find_elemsByXPATH_presence(locator)
        # elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(locator,index)
        if (elems == None):
            raise TypeError("elem不能为None")
        else:
            self.sendkeysElem(elems[index], key,isclear=isclear)


    def sendkeysElemByCSS_Presence(self, locator, key, index=0,isclear=False):
        """给存在dom里的元素组里的某个元素写入值CSS"""
        elems = self.find_elemsByCSS_presence(locator)
        # elem = self.find_elenmInElemsByCSS_visibility_of_any_elements_located(locator, index)
        if (elems == None):
            raise TypeError("elem不能为None")
        else:
            self.sendkeysElem(elems[index],key,isclear=isclear)


    #################
    # 查找元素方法
#xpath

    def retry_if_findElementException(exception ):
        exceptionInfo = str(exception)
        if("stale element reference: element is not attached to the page document" in exceptionInfo):
            print(datetime.datetime.now())
            print("页面刷新导致元素点击失败"+exceptionInfo)
            return isinstance(exception, WebDriverException)

    @retry( retry_on_exception=retry_if_findElementException,stop_max_attempt_number=3, wait_fixed=1000,
           wrap_exception=True,stop_max_delay=3000)
    def find_elemsByXPATH_presence(self, locator, timeout=5):
        """判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, locator)))
        except:
            print("根据" + locator + "信息在" + str(timeout) + "秒内没有查询到元素")
            return None


    @retry( retry_on_exception=retry_if_findElementException,stop_max_attempt_number=3, wait_fixed=1000,
           wrap_exception=True,stop_max_delay=3000)
    def find_elemsByXPATH_visibility(self, locator, timeout=5):
        """判断页面至少有一个元素可见 visible，
        传入locator，一旦定位就返回 the list of located WebElements；不可见（元素隐藏 或是 完全不存在，一个都没有）返回的是 空列表；"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_any_elements_located((By.XPATH, locator)))
        except:
            print("根据" + locator + "信息在" + str(timeout) + "秒内没有查询到元素")
            return None


    @retry( retry_on_exception=retry_if_findElementException,stop_max_attempt_number=3, wait_fixed=1000,
           wrap_exception=True,stop_max_delay=3000)
    def find_elemByXPATH_clickable(self, locator, timeout=5):
        """判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, locator)))
        except:
            print("根据" + locator + "信息在" + str(timeout) + "秒内没有查询到元素")
            return None

    @retry( retry_on_exception=retry_if_findElementException,stop_max_attempt_number=3, wait_fixed=1000,
           wrap_exception=True,stop_max_delay=3000)
    def find_elemByXPATH_visibility(self, locator, timeout=5):
        """判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, locator)))
        except:
            print("根据" + locator + "信息在" + str(timeout) + "秒内没有查询到元素")
            return None

    @retry( retry_on_exception=retry_if_findElementException,stop_max_attempt_number=3, wait_fixed=1000,
           wrap_exception=True,stop_max_delay=3000)
    def find_elemByXPATH_presence(self, locator, timeout=5):
        """判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, locator)))
        except:
            print("根据" + locator + "信息在" + str(timeout) + "秒内没有查询到元素")
            return None

    @retry( retry_on_exception=retry_if_findElementException,stop_max_attempt_number=3, wait_fixed=1000,
           wrap_exception=True,stop_max_delay=3000)
    def find_elenmInElemsByXpath_visibility_of_any_elements_located(self, locator, index=0,timeout=5):
        """判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located((By.XPATH, locator)))[index]
        except IndexError as e:
            print(e)
            print(locator + "页面无此元素"+"index值为"+str(index))
            return None
        except TimeoutException as t:
            print("根据" + locator + "信息: visibility_of_any_elements_located方式在" + str(timeout) + "秒内没有查询到元素")
            print("visibility_of_any_elements_located方式转presence_of_all_elements_located方式")
            elem = self.find_elenmInElemsByXpath_presence_of_all_elements_located(locator,index=index,timeout=3)
            return elem



    @retry( retry_on_exception=retry_if_findElementException,stop_max_attempt_number=3, wait_fixed=1000,
           wrap_exception=True,stop_max_delay=3000)
    def find_elenmInElemsByXpath_element_to_be_clickable(self, locator, index=0,timeout=5):
        """判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, locator)))[index]
        except IndexError as e:
            print(e)
            print(locator + "页面无此元素"+"index值为"+str(index))
            return None
        except TimeoutException as t:
            print(t)
            print("根据"+locator+"信息在"+str(timeout)+"秒内没有查询到元素")
            return None





    @retry( retry_on_exception=retry_if_findElementException,stop_max_attempt_number=3, wait_fixed=1000,
           wrap_exception=True,stop_max_delay=3000)
    def find_elenmInElemsByXpath_presence_of_all_elements_located(self, locator, index=0,timeout=5):
        """判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, locator)))[index]
        except IndexError as e:
            print(e)
            print(locator + "页面无此元素"+"index值为"+str(index))
            return None
        except TimeoutException as t:
            print(t)
            print("使用presence_of_all_elements_located根据"+locator+"信息在"+str(timeout)+"秒内没有查询到元素")
            return None












###Css
    def find_elemByCSS_visibility(self, locator, timeout=5):
        """判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        except:
            print("根据" + locator + "信息在" + str(timeout) + "秒内没有查询到元素")
            return None


    def find_elemsByCSS_presence(self, locator, timeout=5):
        """判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator)))
        except:
            print("根据" + locator + "信息在" + str(timeout) + "秒内没有查询到元素")
            return None

    def find_elemsByCSS_visibility(self, locator, timeout=5):
        """判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, locator)))
        except:
            print("根据" + locator + "信息在visibility_of_all_elements_located方式下" + str(timeout) + "秒内没有查询到元素")
            return None

    def find_elenmInElemsByCSS_visibility_of_any_elements_located(self, locator, index=0,timeout=5):
        """判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_any_elements_located((By.CSS_SELECTOR, locator)))[index]
        except IndexError as e:
            print(e)
            print(locator + "页面无此元素" + "index值为" + str(index))
            return None
        except TimeoutException as t:
            print(t)
            print("根据" + locator + "信息在" + str(timeout) + "秒内没有查询到元素")
            return None



    def switch_tab( self,num ):
        """浏览器窗口切换"""
        driver = self.driver
        handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
        driver.switch_to.window(handles[num - 1])  # 跳转到第num个窗口






