# coding=utf-8
from public.selenium_page import SeleniumPage


class ConsoleLoginPage(SeleniumPage):
    """登录界面"""


    zhanghao = "//input[@class='loginFormTdIpt search-input' and @name='username']"
    mima = "//input[@class='loginFormTdIpt search-input' and @name='password']"
    anniu = "//button[@class='login_btn']"


    def user_login(self,login_url, username,password,*args):
        """通过用户名密码登录
        username：账号
        password：密码
        """
        self.open(login_url)
        self.sendkeysElemByXpath_visibility(self.zhanghao,username)
        self.sendkeysElemByXpath_visibility(self.mima,password)
        self.clickElemByXpath_visibility(self.anniu)