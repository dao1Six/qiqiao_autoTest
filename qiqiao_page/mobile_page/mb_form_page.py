#表单页面
from qiqiao_page.mobile_page.form_components.mb_cascade_component import MbCascade
from qiqiao_page.mobile_page.form_components.mb_datetime_component import MbDateTime
from qiqiao_page.mobile_page.form_components.mb_dept_component import MbDept
from qiqiao_page.mobile_page.form_components.mb_pic_Upload_component import MbPicUpload
from qiqiao_page.mobile_page.form_components.mb_number_component import     MbNumber
from qiqiao_page.mobile_page.form_components.mb_text_component import MbText
from qiqiao_page.mobile_page.form_components.mb_textarea_components import MbTextarea
from qiqiao_page.mobile_page.form_components.mb_date_component import MbDate
from qiqiao_page.mobile_page.form_components.mb_time_component import MbTime
from qiqiao_page.mobile_page.form_components.mb_file_Upload_component import MbFileUpload
from qiqiao_page.mobile_page.form_components.mb_selection_component import MbSelection
from qiqiao_page.mobile_page.form_components.mb_user_component import MbUser
from qiqiao_page.mobile_page.form_components.mb_address_component import MbAddress
from qiqiao_page.mobile_page.form_components.mb_childForm_component import MbChildForm_component
from qiqiao_page.mobile_page.form_components.mb_childFormAssociation_component import MbChildFormAssociation_component
from qiqiao_page.mobile_page.form_components.mb_foreignSelection_component import MbForeignSelection_component
from qiqiao_page.mobile_page.form_components.mb_multiFormAssociation_component import MbMultiFormAssociation
from qiqiao_page.mobile_page.mb_public_page import MbPublicPage


class MbFormPage(MbPublicPage,MbNumber,MbText,MbTextarea,MbDate,MbTime,MbDateTime,MbPicUpload,MbFileUpload,
                 MbSelection,MbUser,MbAddress,MbCascade,MbChildForm_component,MbChildFormAssociation_component,
                 MbForeignSelection_component,MbMultiFormAssociation,MbDept):
    '''移动端表单页面'''

    FormPage_button_loc = "//button[@title='%s']"  #表单按钮

    process_querenButton_loc = "//div[@class='workFlowHandle']//button[contains(text(),'提交')]"

    def Form_Button_Click( self,buttonName ):
        '''点击表单按钮'''
        self.clickElemByXpath_visibility(self.FormPage_button_loc.replace('%s',buttonName))


    def Form_ProcessHandle_Pop_QuerenButton_Click( self ):
        '''点击流程办理弹框提交按钮'''
        self.clickElemByXpath_visibility(self.process_querenButton_loc)