import time
from public.driver import pcdriver
from qiqiao_PublicPage.login_page import LoginPage
from qiqiao_PublicPage.portal_page import PortalPage
from qiqiao_PublicPage.applicationList_page import ApplicationListPage
from AppPage_obj.SaySafePage.fill_data_page import AppFillSafe
from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Projects\qiqiao_autoTest\\file_data\chromedriver.exe")
driver.maximize_window()
loginpage = LoginPage(driver)
loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@do1", "do1qiqiao")
portalpage = PortalPage(driver)
portalpage.click_header_menu("应用")
applicationListPage = ApplicationListPage(driver)
time.sleep(2)
applicationListPage.click_application("全员报平安2.2")
runtime = AppFillSafe(driver)
runtime.click_title("报平安")

runtime.input_picture()