#表单页面
from qiqiao_page.pc_page.components.cascade_component import Cascade
from qiqiao_page.pc_page.components.datetime_component import DateTime
from qiqiao_page.pc_page.components.dept_component import Dept
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


class FormPage(Number,Text,Textarea,Date,Time,DateTime,PicUpload,FileUpload,Selection,User,Address,Cascade,ChildForm_component,ChildFormAssociation_component,ForeignSelection_component,MultiFormAssociation,Dept):
    '''PC表单页面'''

    FormPage_submit_button_loc = "//button[@type='button']/span[contains(text(),'提交')]"  #表单提交按钮

    #提交表单
    def click_submit_button(self,*args):
        self.clickElemByXpath_Presence(self.FormPage_submit_button_loc)