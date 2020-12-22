# coding=utf-8
#外部表单页面

from public.selenium_page import SeleniumPage


class ExternalFormPage(SeleniumPage):
    """外部表单页面"""

    submit_form_btn = "//button[@class='submit_form_btn']"  #提交按钮
    message_content = "//p[@class='el-message__content']" #消息弹框

    def ExternalFormPage_Click_SubmitBtn(self,*args):
        '''点击提交按钮'''
        self.clickElemByXpath_visibility(self.submit_form_btn)


    def ExternalFormPage_Get_MessageContent(self,*args):
        '''获取外部表单弹框提示信息'''
        return self.find_elemByXPATH_presence(self.message_content).text


