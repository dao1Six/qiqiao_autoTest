#子表关联组件
import time

from public.selenium_page import SeleniumPage


class MbChildFormAssociation_component(SeleniumPage):


    MbChildFormAssociation_AddButton_loc = "//div[@title='%title']//div[@class='dyFormChildFormAssociation_add']"  # 添加按钮元素
    searchBar_i = "//div[@class='searchBar_search_input']//i"
    searchBar_input = "//div[@class='searchBar_search_input']//input"

    fieldSelect_i = "//div[@class='searchBar_search_fieldSelect']//i"
    fieldSelect_Item = "//div[contains(@class,'searchBar_leftDrawer_item') and contains(text(),'%s')]"

    List_item = "//div[@class='childFormAssociation_tableContainer lockScroll']//div[@class='el-table__body-wrapper is-scrolling-left']//tr[@class='el-table__row']"

    cancel_btn_loc = "//button[@class='cube-btn cancel_btn cube-btn-inline cube-btn-outline']"

    confirm_btn_loc="//button[@class='cube-btn confirm_btn cube-btn-inline']"

    def MbChildFormAssociation_AddButton_Click(self,fileName,*args):
        '''点击子表关联组件添加按钮'''
        self.clickElemByXpath_visibility (self.MbChildFormAssociation_AddButton_loc.replace ('%title', fileName))


    def MbChildFormAssociation_List_Get_RecoresNumber( self ):
        '''返回当前子表关联列表记录数'''
        elems =self.find_elemsByXPATH_presence(self.List_item,timeout=3)
        if(elems!=None):
            return len(elems)
        else:
            return 0

    def MbChildFormAssociation_List_searchInput_Sendkeys( self,key ):
        '''子表关联列表搜索框输入值'''
        self.clickElemByXpath_visibility(self.searchBar_i)
        self.sendkeysElemByXpath_visibility(self.searchBar_input,key)

    def MbChildFormAssociation_List_searchItem_Switch( self,Item ):
        '''子表关联列表切换搜索项'''
        self.clickElemByXpath_visibility(self.fieldSelect_i)
        time.sleep(1)
        self.clickElemByXpath_visibility(self.fieldSelect_Item.replace("%s",Item))



    def ChildFormAssociation_ManagementDialog_Record_Click(self,*args):
        '''勾选批量管理页面关联表记录'''
        pass


    def ChildFormAssociation_ManagementDialog_ConfirmButton_Click(self,*args):
        '''点击批量管理页面确认按钮'''
        self.clickElemByXpath_visibility(self.confirm_btn_loc)


    def ChildFormAssociation_ManagementDialog_CancelButton_Click(self,*args):
        '''点击批量管理页面取消按钮'''
        self.clickElemByXpath_visibility(self.cancel_btn_loc)
