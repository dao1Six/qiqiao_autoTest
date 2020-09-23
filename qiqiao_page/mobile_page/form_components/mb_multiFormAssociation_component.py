#多表关联组件
import time

from public.selenium_page import SeleniumPage


class MbMultiFormAssociation(SeleniumPage):


    MultiFormAssociation_AddButton_loc = "//div[@title='%title']//div[@class='dyFormMultiFormAssociation_add']"  #添加按钮元素

    MultiFormAssociation_rightAddButton_loc = "//div[@title='%title']//span[@class='title_add']" # 添加按钮元素

    MultiFormManagementDialog_selected_loc = "//div[@class='el-table__fixed-body-wrapper']//table[@class='el-table__body']//tr[%rowIndex]//td[last()]//span[@class='el-checkbox__inner']"

    MultiFormManagementDialog_Button_loc = "//div[contains(@class,'multiFormAssociation_choose_bottom')]//button[contains(text(),'%s')]"

    MultiForm_Td_loc = "//div[@title='%s']//table[@class='el-table__body']//tr[%row]/td[%col]//div[@class='text_overflow']"

    MultiForm_Td_order_operation_loc = "//div[@title='%s']//table[@class='el-table__body']//tr[%row]/td[%col]//div[@class='subformTable_order subformTable_order_operation']"

    MultiForm_Td_iconDelete_loc = "//div[@title='%s']//i[@class='iconfont icon-del iconDelete']"

#多表关联外部操作

    def MbMultiForm_edit_Record(self,fileName,row):
        '''点击多表关联组件编辑按钮'''
        self.clickElemByXpath_visibility(self.MultiForm_Td_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(2)))

    def MbMultiForm_AddButton_Click(self,fileName,*args):
        '''点击添加按钮'''
        self.clickElemByXpath_visibility (self.MultiFormAssociation_AddButton_loc.replace ('%title', fileName))

    def MbMultiForm_rightAddButton_Click(self,fileName,*args):
        '''点击右上角添加按钮'''
        self.clickElemByXpath_visibility (self.MultiFormAssociation_rightAddButton_loc.replace ('%title', fileName))

    def MbMultiForm_GetTdValue( self,fileName,row,col,*args ):
        '''获取多表关联组件中间表单元格值'''
        text = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(
            self.MultiForm_Td_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(col))).text
        if (text == ""):
            text = self.getElemAttrValue(self.find_elenmInElemsByXpath_visibility_of_any_elements_located(
                self.MultiForm_Td_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',
                                                                                              str(col)) + "//input"),
                                         "value")
        return text

    def MbMultiForm_DeletTdValue( self,fileName,row,*args ):
        '''删除多表关联组件中间表数据'''
        # 点击删除数据的序号
        self.clickElemByXpath_visibility(
            self.MultiForm_Td_order_operation_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',
                                                                                                          str(1)))
        # 点击删除按钮
        self.clickElemByXpath_visibility(self.MultiForm_Td_iconDelete_loc.replace('%s',fileName))

#多表关联批量管理页面内部操作

    def MbMultiForm_BathManagePage_Record_Tick(self,fileName,rowIndexList,*args):
        '''勾选批量管理页面关联表记录'''
        for rowIndex in rowIndexList:
            str_rowIndex = str(rowIndex)
            # self.clickElemByCSS_visibility (self.MultiFormManagementDialog_selected_loc.replace ('%title', fileName).replace('%rowIndex',str_rowIndex))
            self.clickElemByXpath_visibility(self.MultiFormManagementDialog_selected_loc.replace('%rowIndex',str_rowIndex))
            time.sleep(2)


    def MbMultiForm_BathManagePage_Button_Cick(self,fileName,buttonName,*args):
        '''点击批量管理页面按钮'''
        self.clickElemByXpath_visibility (self.MultiFormManagementDialog_Button_loc.replace ('%s', buttonName))


