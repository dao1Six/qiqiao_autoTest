# coding=utf-8
import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tqy.do1.net.cn/qa-console")
time.sleep(2)
driver.find_element_by_id("j_username").send_keys("wujianlun@B")
driver.find_element_by_id("j_password").send_keys("qiqiao2019")
driver.find_element_by_id("btn_login").click()

