#表单页面
import time

from selenium.webdriver.common.keys import Keys

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


class FormPage(Grade,PublicPage,Number,Text,Textarea,Date,Time,DateTime,PicUpload,FileUpload,Selection,User,Address,Cascade,ChildForm_component,ChildFormAssociation_component,ForeignSelection_component,MultiFormAssociation,Dept,SerialNumber):
    """PC表单页面"""

    FormPage_submit_button_loc = "//button[@type='button']/span[contains(text(),'提交')]"  #表单提交按钮

    FormPage_button_loc = "//div[@class='header']//span[contains(text(),'%s')]/parent::button[contains(@class,'el-button--small')]"

    select_struct_box ="//span[@class='d_inline_block mr_2 mb_2 text_ellipsis user_add']"#"//div[contains(@class,'select_struct_box')]"

    process_querenButton_loc = "//button[@data-mark='确定按钮']"

    processUser_querenButton_loc = "//button[@data-mark='确定按钮']"

    MoreButton_loc = "//div[@class='header']//span[@class='dropdown_title' and contains(text(),'更多')]"
    bottonInMore_loc = "//ul[@class='el-dropdown-menu el-popper']/li[contains(text(),'%s')]"


    ProcessManagers_loc = "//div[@class='common_select_struct']/span"

    tabName_loc = "//div[@role='tablist']/div[text()='%s']"

    Signature_option_loc = "//span[text()='%s' and @class='el-radio__label']"

    RejectNode_Input_loc = "//input[@placeholder='请选择节点']"
    RejectNode_loc = "//li[@class='el-select-dropdown__item']/span[text()='%s']"

    workflow_info = "//div[@class='workflow-info_row']//span"

    Popup_close_icon = "//div[@data-mark='子表弹层_%s']//i[@class='el-icon-close close']"

    field_label_loc = "//div[@data-mark='%s']//label"

    def Form_scroll( self,number):
        """"""
        js = 'var action=document.documentElement.scrollTop={}'.format(str(number))
        self.driver.execute_script(js)  # 执行脚本


    def Form_field_isVisibility( self,fieldName ):
        """表单字段是否可见"""
        if(self.find_elemByXPATH_visibility(self.field_label_loc.replace("%s",fieldName),timeout=3)!=None):
            return True
        else:
            return False


    def Form_Close_Popup( self,childFormName ):
        """关闭子表弹层"""
        self.clickElemByXpath_visibility(self.Popup_close_icon.replace('%s',childFormName))

    def Form_ButtonInMore_Click( self,buttonName):
        """点击表单更多按钮里的按钮"""
        self.clickElemByXpath_visibility(self.MoreButton_loc)
        time.sleep(2)
        self.clickElemByXpath_visibility(self.bottonInMore_loc.replace('%s',buttonName))

    #提交表单
    def click_submit_button(self,*args):
        self.clickElemByXpath_visibility(self.FormPage_submit_button_loc)

    def Form_Button_Click( self,buttonName ):
        """点击表单按钮"""
        self.clickElemByXpath_visibility(self.FormPage_button_loc.replace('%s',buttonName))

    def FormPage_button_isExistence( self ,buttonName):
        elem = self.find_elemsByXPATH_presence(self.FormPage_button_loc.replace('%s',buttonName),timeout=2)
        if(elem!=None):
            return True
        else:
            return False



    #流程办理弹框相关方法

    def Form_Select_ProcessManager( self,userNameList ):
        """选择流程办理人"""
        # 点击办理人输入框
        self.clickElemByXpath_visibility(self.select_struct_box)
        for name in userNameList:
            self.clickElemByXpath_visibility(self.User_search_loc)
            self.sendkeysElemByXpath_visibility(self.User_search_loc,name)
            self.clickElemByXpath_visibility(self.User_searchOption_loc.replace('%s',name))
        #点击组织选择器确认按钮
        self.clickElemByXpath_visibility(self.processUser_querenButton_loc,index=1)



    def Form_ProcessHandle_Pop_QuerenButton_Click( self ):
        """点击流程办理弹框确认按钮"""
        self.clickElemByXpath_visibility(self.process_querenButton_loc)


    def Form_Get_ProcessManagers( self ):
        """获取流程弹框办理者"""
        UsersName = []
        UsersElem = self.find_elemsByXPATH_presence(self.ProcessManagers_loc)
        for userElem in UsersElem:
            UsersName.append(userElem.text)
        return UsersName

    def Form_Switch_Tab( self ,name):
        """切换表单选项卡"""
        self.clickElemByXpath_visibility(self.tabName_loc.replace('%s',name))

    def Form_Select_Signature( self ,optin):
        """选择加签方式"""
        self.clickElemByXpath_visibility(self.Signature_option_loc.replace('%s',optin))


    def Form_Select_RejectNode( self ,RejectNodeName):
        """选择驳回节点"""
        self.clickElemByXpath_visibility(self.RejectNode_Input_loc)
        time.sleep(1)
        self.clickElemByXpath_visibility(self.RejectNode_loc.replace('%s',RejectNodeName))

    def Form_Get_Sponsor( self):
        """获取表单流程发起人"""
        return self.find_elemsByXPATH_visibility(self.workflow_info)[0].text


    def Form_Get_LaunchTime( self):
        """获取表单流程发起时间"""
        return self.find_elemsByXPATH_visibility(self.workflow_info)[1].text