#表单页面
from qiqiao_page.mobile_page.form_components.cascade_component import Cascade
from qiqiao_page.mobile_page.form_components.datetime_component import DateTime
from qiqiao_page.mobile_page.form_components.dept_component import Dept
from qiqiao_page.mobile_page.form_components.pic_Upload_component import PicUpload
from public.selenium_page import SeleniumPage
from qiqiao_page.mobile_page.form_components.number_component import Number
from qiqiao_page.mobile_page.form_components.text_component import Text
from qiqiao_page.mobile_page.form_components.textarea_components import Textarea
from qiqiao_page.mobile_page.form_components.date_component import Date
from qiqiao_page.mobile_page.form_components.time_component import Time
from qiqiao_page.mobile_page.form_components.file_Upload_component import FileUpload
from qiqiao_page.mobile_page.form_components.selection_component import Selection
from qiqiao_page.mobile_page.form_components.user_component import User
from qiqiao_page.mobile_page.form_components.address_component import Address
from qiqiao_page.mobile_page.form_components.childForm_component import ChildForm_component
from qiqiao_page.mobile_page.form_components.childFormAssociation_component import ChildFormAssociation_component
from qiqiao_page.mobile_page.form_components.foreignSelection_component import ForeignSelection_component
from qiqiao_page.mobile_page.form_components.multiFormAssociation_component import MultiFormAssociation


class FormPage(Number,Text,Textarea,Date,Time,DateTime,PicUpload,FileUpload,Selection,User,Address,Cascade,ChildForm_component,ChildFormAssociation_component,ForeignSelection_component,MultiFormAssociation,Dept):
    '''移动端表单页面'''

    FormPage_submit_button_loc = "//button[@type='button']/span[contains(text(),'提交')]"  #表单提交按钮

    #提交表单
    def click_submit_button(self,*args):
        self.clickElemByXpath_visibility(self.FormPage_submit_button_loc)