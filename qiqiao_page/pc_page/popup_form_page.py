#表单页面
import time

from selenium.webdriver.common.keys import Keys

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
from qiqiao_page.pc_page.public_page import PublicPage


class PopupFormPage(PublicPage,Number,Text,Textarea,Date,Time,DateTime,PicUpload,FileUpload,Selection,User,Address,Cascade,ChildForm_component,ChildFormAssociation_component,ForeignSelection_component,MultiFormAssociation,Dept):
    '''PC弹窗表单页面'''


    FormPage_button_loc = "//span[contains(text(),'%s')]/parent::button[contains(@class,'el-button--small')]"



    def PopupFormPage_Button_Click( self,buttonName ):
        '''点击弹窗表单按钮'''
        self.clickElemByXpath_visibility(self.FormPage_button_loc.replace('%s',buttonName))

