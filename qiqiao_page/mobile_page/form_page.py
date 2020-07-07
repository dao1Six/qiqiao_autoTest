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

    FormPage_button_loc = "//button[@title='%s']"  #表单按钮

    process_querenButton_loc = "//div[@class='workFlowHandle']//button[contains(text(),'提交')]"

    def Form_Button_Click( self,buttonName ):
        '''点击表单按钮'''
        self.clickElemByXpath_visibility(self.FormPage_button_loc.replace('%s',buttonName))


    def Form_ProcessHandle_Pop_QuerenButton_Click( self ):
        '''点击流程办理弹框提交按钮'''
        self.clickElemByXpath_visibility(self.process_querenButton_loc)