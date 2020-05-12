# coding=utf-8
import os
import time

from selenium import webdriver

class Driver():

    chromedriverPath = os.path.abspath(os.path.join(os.getcwd(), "../.."))+'\\file_data\\chromedriver.exe'
    # 启动浏览器驱动
    def pcdriver(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)   #禁用谷歌浏览器的通知框
    #     chrome_options.add_argument("--disable-popup-blocking")    #设置谷歌浏览器允许弹出窗口

        driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=self.chromedriverPath)

    #     driver = webdriver.Firefox()
        return driver

    # phone皮肤启动浏览器驱动
    def phonedriver(self):
        mobile_emulation = {"deviceName":"iPhone X"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome(chrome_options = chrome_options,executable_path=self.chromedriverPath)
        return driver


if __name__ == '__main__':
    pass
