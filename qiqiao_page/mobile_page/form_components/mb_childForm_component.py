#子表
import time

from public.selenium_page import SeleniumPage


class MbChildForm_component(SeleniumPage):

    ChildForm_AddButton_loc ="//div[@title='%s']//span[@class='dyFormSubform_addBtn']"  #子表添加按钮

    ChildForm_Button_loc = "//button[text()=' %s']"

    ChildForm_Td_loc = "//div[@title='%s']//div[@class='subformTable']//tbody/tr[%row]/td[%col]"

    def MbChildForm_AddButton_Click(self,fieldName,*args):
        '''点击添加按钮
        fieldName：字段标题
        '''
        self.clickElemByXpath_visibility (self.ChildForm_AddButton_loc.replace ('%s', fieldName))

    def MbChildForm_Button_Click(self,buttonName,*args):
        '''点击添加按钮
        fieldName：字段标题
        '''
        self.clickElemByXpath_visibility (self.ChildForm_Button_loc.replace ('%s', buttonName))

    def MbChildForm_GetTdValue( self,fileName,row,col):
        '''获取移动端子表单元格值'''
        text = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(
            self.ChildForm_Td_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(col))).text
        if (text == ""):
            text = self.getElemAttrValue(self.find_elenmInElemsByXpath_visibility_of_any_elements_located(
                self.ChildForm_Td_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(col)) + "//input"),
                                         "value")
        return text

    def ChildForm_Record_Delete(self):
        '''删除子表记录'''
        pass




