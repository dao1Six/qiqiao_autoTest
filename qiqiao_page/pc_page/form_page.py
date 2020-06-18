#表单页面
import time

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

    FormPage_button_loc = "//button[contains(@class,'el-button')]/span[contains(text(),'%s')]"

    select_struct_box = "//div[@aria-label='办理']//div[contains(@class,'select_struct_box')]"

    process_querenButton_loc = "//div[@aria-label='办理']//button[@data-mark='确定按钮']"

    processUser_querenButton_loc = "//div[@aria-label='选择办理人']//button[@data-mark='确定按钮']"

    #提交表单
    def click_submit_button(self,*args):
        self.clickElemByXpath_Presence(self.FormPage_submit_button_loc)

    def clickFormButton( self,buttonName ):
        '''点击表单按钮'''
        self.clickElemByXpath_Presence(self.FormPage_button_loc.replace('%s',buttonName))



    #流程办理弹框相关方法

    def selectProcessManager( self,userNameList ):
        '''选择流程办理人'''
        # 点击办理人输入框
        self.clickElemByXpath_Presence(self.select_struct_box)
        for name in userNameList:
            self.clickElemByXpath_Presence(self.User_search_loc)
            self.sendkeysElemByXpath_Presence(self.User_search_loc,name)
            self.clickElemByXpath_Presence(self.User_searchOption_loc.replace('%s',name),index=1)
        #点击组织选择器确认按钮
        self.clickElemByXpath_Presence(self.processUser_querenButton_loc)
        time.sleep(1)
        # 点击流程办理框确认按钮
        self.clickElemByXpath_Presence(self.process_querenButton_loc)

