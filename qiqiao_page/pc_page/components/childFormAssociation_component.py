#子表关联组件
from public.selenium_page import SeleniumPage


class ChildFormAssociation_component(SeleniumPage):


    ChildFormAssociation_AddButton_loc = "//div[@data-mark='%title']//span[@data-mark='button_添加']"
    List_item = "//div[@class='batchManagementDialog_association']//div[@class='el-table__body-wrapper is-scrolling-left']//tr[@class='el-table__row']"
    cancel_btn_loc = "//button[@data-mark='取消按钮']"
    confirm_btn_loc="//button[@data-mark='确定按钮']"

    def ChildFormAssociation_AddButton_Click(self,fileName,*args):
        '''点击子表关联组件添加按钮'''
        self.clickElemByXpath_visibility (self.ChildFormAssociation_AddButton_loc.replace ('%title', fileName))

    def ChildFormAssociation_List_Get_RecoresNumber( self ):
        '''返回当前子表关联列表记录数'''
        elems =self.find_elemsByXPATH_presence(self.List_item,timeout=3)
        if(elems!=None):
            return len(elems)
        else:
            return 0



    def ChildFormAssociation_ManagementDialog_Record_Click(self,*args):
        '''勾选批量管理页面关联表记录'''
        pass


    def ChildFormAssociation_ManagementDialog_ConfirmButton_Click(self,*args):
        '''点击批量管理页面确认按钮'''
        self.clickElemByXpath_visibility(self.confirm_btn_loc)


    def ChildFormAssociation_ManagementDialog_CancelButton_Click(self,*args):
        '''点击批量管理页面取消按钮'''
        self.clickElemByXpath_visibility(self.cancel_btn_loc)
