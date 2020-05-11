# coding=utf-8
#登录页面
import time

from public.selenium_page import SeleniumPage


class MobileLoginPage(SeleniumPage):
    """登录界面"""

    mobiledenglu = "//a[text()='账号密码登录']"
    mobilezhanghao = "//input[@title='请输入账号']"
    mobilemima = "//input[@title='请输入密码']"
    mobileanniu = "//button[text()='登录']"


    def user_login(self,login_url, username,password,*args):
        """通过用户名密码登录
        username：账号
        password：密码
        """
        self.open(login_url)
        self.clickElemByXpath_Presence(self.mobiledenglu)
        self.sendkeysElemByXpath_Presence(self.mobilezhanghao,username)
        self.sendkeysElemByXpath_Presence(self.mobilemima,password)
        self.clickElemByXpath_Presence(self.mobileanniu)
        time.sleep(2)

