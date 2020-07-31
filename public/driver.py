# coding=utf-8
import os
import time

from selenium import webdriver

class Driver():


    ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0]+"qiqiao_autoTest"

    chromedriverPath = ProjectRootPath+'\\file_data\\chromedriver.exe'

    downloadPath = ProjectRootPath+'\\file_data\\downloadData'

    # 启动浏览器驱动
    def pcdriver(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2 ,"download.default_directory": self.downloadPath}
        chrome_options.add_experimental_option("prefs",prefs)   #禁用谷歌浏览器的通知框
        chrome_options.add_argument("–incognito")
        # chrome_options.add_argument('--headless')  # 无头模式
        driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=self.chromedriverPath)
        return driver

    # phone皮肤启动浏览器驱动
    def phonedriver(self):
        mobile_emulation = {"deviceName":"iPhone X"}
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_options.add_argument("–incognito")
        # chrome_options.add_argument('--headless')#无头模式
        chrome_options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示

        driver = webdriver.Chrome(chrome_options = chrome_options,executable_path=self.chromedriverPath)
        return driver


if __name__ == '__main__':
    pass
