# coding=utf-8
#登录页面

from public.selenium_page import SeleniumPage


class LoginPage(SeleniumPage):
    """登录界面"""

    denglu = "//a[text()='账号密码登录']"
    zhanghao = "//input[@title='请输入账号']"
    mima = "//input[@title='请输入密码']"
    anniu = "//button[text()='登录']"
    imMsgBoxMsg_loc = "//p[@id='imMsgBoxMsg']"


    def user_login(self,login_url, username,password,*args):
        """通过用户名密码登录
        username：账号
        password：密码
        """
        self.open(login_url)
        self.clickElemByXpath_visibility(self.denglu)
        self.sendkeysElemByXpath_visibility(self.zhanghao,username)
        self.sendkeysElemByXpath_visibility(self.mima,password)
        self.clickElemByXpath_visibility(self.anniu)

    def LoginPage_Get_ImMsg( self ):
        '''获取登录提示框信息'''
        return self.find_elemByXPATH_visibility(self.imMsgBoxMsg_loc).text
