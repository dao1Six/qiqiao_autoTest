# coding=utf-8
#外部表单页面

from qiqiao_page.pc_page.components.cascade_component import Cascade
from qiqiao_page.pc_page.components.datetime_component import DateTime
from qiqiao_page.pc_page.components.dept_component import Dept
from qiqiao_page.pc_page.components.grade_component import Grade
from qiqiao_page.pc_page.components.pic_Upload_component import PicUpload
from public.selenium_page import SeleniumPage
from qiqiao_page.pc_page.components.number_component import Number
from qiqiao_page.pc_page.components.text_component import Text
from qiqiao_page.pc_page.components.textarea_components import Textarea
from qiqiao_page.pc_page.components.date_component import Date
from qiqiao_page.pc_page.components.time_component import Time
from qiqiao_page.pc_page.components.file_Upload_component import FileUpload
from qiqiao_page.pc_page.components.selection_component import Selection
from qiqiao_page.pc_page.components.user_component import User
from qiqiao_page.pc_page.components.address_component import Address
from qiqiao_page.pc_page.components.childForm_component import ChildForm_component
from qiqiao_page.pc_page.components.childFormAssociation_component import ChildFormAssociation_component
from qiqiao_page.pc_page.components.foreignSelection_component import ForeignSelection_component
from qiqiao_page.pc_page.components.multiFormAssociation_component import MultiFormAssociation
from qiqiao_page.pc_page.components.serialNumber import SerialNumber
from qiqiao_page.pc_page.public_page import PublicPage


class ExternalFormPage(Grade,PublicPage,Number,Text,Textarea,Date,Time,DateTime,PicUpload,FileUpload,Selection,User,Address,Cascade,ChildForm_component,ChildFormAssociation_component,ForeignSelection_component,MultiFormAssociation,Dept,SerialNumber):
    """外部表单页面"""

    submit_form_btn = "//button[@class='submit_form_btn']"  #提交按钮
    message_content = "//p[@class='el-message__content']" #消息弹框
    field_label_loc="//div[@data-mark='%s']//label"

    def ExternalFormPage_Click_SubmitBtn(self,*args):
        '''点击提交按钮'''
        self.clickElemByXpath_visibility(self.submit_form_btn)


    def ExternalFormPage_Get_MessageContent(self,*args):
        '''获取外部表单弹框提示信息'''
        return self.find_elemByXPATH_presence(self.message_content).text


    def ExternalForm_field_isVisibility( self,fieldName ):
        """表单字段是否可见"""
        if(self.find_elemByXPATH_visibility(self.field_label_loc.replace("%s",fieldName),timeout=3)!=None):
            return True
        else:
            return False