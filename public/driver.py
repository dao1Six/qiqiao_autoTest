# coding=utf-8
import os
import time

from retrying import retry
from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException


class Driver():


    ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0]+"qiqiao_autoTest"

    chromedriverPath = ProjectRootPath+'\\file_data\\chromedriver.exe'

    # chromedriverPath="C:/Users/admin/AppData/Local/Google/Chrome/Application/chromedriver.exe"
    downloadPath = ProjectRootPath+'\\file_data\\downloadData'

    def retry_if_getDriverException(exception ):
        exceptionInfo = str(exception)
        if ("session not created" in exceptionInfo):
            print("SessionNotCreatedException" + exceptionInfo)
            return isinstance(exception, SessionNotCreatedException)


    @retry( retry_on_exception=retry_if_getDriverException,stop_max_attempt_number=3, wait_fixed=1000,
           wrap_exception=True,stop_max_delay=5000)
    def pcdriver(self):
        '''启动浏览器驱动'''
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2 ,"download.default_directory": self.downloadPath}
        chrome_options.add_experimental_option("prefs",prefs)   #禁用谷歌浏览器的通知框
        chrome_options.add_argument('window-size=1920x3000')
        chrome_options.add_argument("–incognito")
        # chrome_options.add_argument('--headless')  # 无头模式
        driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=self.chromedriverPath)
        return driver


    @retry(retry_on_exception=retry_if_getDriverException, stop_max_attempt_number=3, wait_fixed=1000,
           wrap_exception=True, stop_max_delay=5000)
    def phonedriver(self):
        '''phone皮肤启动浏览器驱动'''
        mobile_emulation = {"deviceName":"iPhone X"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('window-size=1920x3000')
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_options.add_argument("–incognito")#无痕模式
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--headless')#无头模式
        # chrome_options.add_argument('--disable-infobars')  # 禁止策略化
        # chrome_options.add_argument('lang=zh_CN.UTF-8')
        chrome_options.add_argument(
            'User-Agent=Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36')
        chrome_options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
        chrome_options.add_experimental_option('w3c',False)

        driver = webdriver.Chrome(chrome_options = chrome_options,executable_path=self.chromedriverPath)
        return driver


if __name__ == '__main__':
    pass
