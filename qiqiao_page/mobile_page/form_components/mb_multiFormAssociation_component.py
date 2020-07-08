#多表关联组件
from public.selenium_page import SeleniumPage


class MbMultiFormAssociation(SeleniumPage):


    MultiFormAssociation_AddButton_loc = "//div[@title='%title']//div[@class='dyFormMultiFormAssociation_add']"  #添加按钮元素

    MultiFormManagementDialog_selected_loc = "//div[@class='el-table__fixed-body-wrapper']//table[@class='el-table__body']//tr[%rowIndex]//td[last()]//span[@class='el-checkbox__inner']"

    MultiFormManagementDialog_Button_loc = "//div[contains(@class,'multiFormAssociation_choose_bottom')]//button[contains(text(),'%s')]"

    MultiForm_Td_loc = "//div[@title='%s']//table[@class='el-table__body']//tr[%row]/td[%col]//div[@class='text_overflow']"

    def MultiForm_AddButton_Click(self,fileName,*args):
        '''点击添加按钮'''
        self.clickElemByXpath_visibility (self.MultiFormAssociation_AddButton_loc.replace ('%title', fileName))


    def MultiForm_BathManagePage_Record_Tick(self,fileName,rowIndexList,*args):
        '''勾选批量管理页面关联表记录'''
        for rowIndex in rowIndexList:
            str_rowIndex = str(rowIndex)
            # self.clickElemByCSS_visibility (self.MultiFormManagementDialog_selected_loc.replace ('%title', fileName).replace('%rowIndex',str_rowIndex))
            self.clickElemByXpath_visibility(self.MultiFormManagementDialog_selected_loc.replace('%rowIndex',str_rowIndex))


    def MultiForm_BathManagePage_Button_Cick(self,fileName,buttonName,*args):
        '''点击批量管理页面按钮'''
        self.clickElemByXpath_visibility (self.MultiFormManagementDialog_Button_loc.replace ('%s', buttonName))


    def MultiForm_GetTdValue( self,fileName,row,col,*args):
        '''获取多表关联组件中间表单元格值'''
        text = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.MultiForm_Td_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(col))).text
        if(text==""):
            text = self.getElemAttrValue(self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.MultiForm_Td_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(col))+"//input"),"value")
        return text