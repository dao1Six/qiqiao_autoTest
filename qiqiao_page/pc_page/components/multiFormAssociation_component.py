#多表关联组件
import time

from public.selenium_page import SeleniumPage


class MultiFormAssociation(SeleniumPage):
    MultiFormAssociation_HandleManagerButton_loc = "[data-mark=%title] [data-mark=button_批量管理]" #批量管理按钮

    MultiFormAssociation_AddButton_loc = "[data-mark=%title] [data-mark=button_添加]"  #添加按钮

    MultiFormManagementDialog_ConfirmButton_loc = ".%title [data-mark=确定按钮]"  #批量管理页面确定按钮

    MultiFormManagementDialog_CancelButton_loc = ".%title [data-mark=取消按钮]"  #批量管理页面取消按钮

    MultiFormManagementDialog_selected_loc =  ".%title [data-mark=%title_table] [data-mark=row_checkbox_%rowIndex] span.el-checkbox__input"  #批量管理页面记录勾选框

    MultiFormManagementDialog_paginationPrev_loc = ".%title [data-mark=%title_pagination] .btn-prev"  #批量管理页面翻页上一页按钮

    MultiFormManagementDialog_paginationNext_loc = ".%title [data-mark=%title_pagination] .btn-next"   #批量管理页面翻页下一页按钮

    MultiFormManagementDialog_paginationNumber_loc = ".%title [data-mark=%title_pagination] .number:nth-child(%n)"  #批量管理页面翻页第几页

    MultiFormManagementDialog__Input_loc = ".%title [data-mark=%title_selected] .row_%title_%rowIndex [data-mark=%filename] input"  #批量管理页面，中间表字段输入框

    MultiForm_SelectOption_loc = "[data-mark='%option']"  # 下拉选项

    MultiFormManagementDialog__dialogfooter_loc = "div.dialog-footer"

    MultiForm_Td_loc = "//div[@data-mark='%s']//tr[@class='el-table__row'][%row]//td[%col]"

    MultiForm_RelationForm_Td_loc = "//div[@data-mark='%s_table']//tr[@class='el-table__row'][%row]//td[%col]//span"

    def MultiForm_BatchManagementButton_Click(self,fileName,*args):
        '''点击批量管理按钮'''
        self.clickElemByCSS_visibility(self.MultiFormAssociation_HandleManagerButton_loc.replace('%title',fileName))


    def MultiForm_AddButton_Click(self,fileName,*args):
        '''点击添加按钮'''
        self.clickElemByCSS_visibility (self.MultiFormAssociation_AddButton_loc.replace ('%title', fileName))



    def click_MultiFormManagementDialog_paginationPrev(self,fileName,*args):
        '''批量管理页面翻页上一页按钮'''
        self.clickElemByCSS_visibility(self.MultiFormManagementDialog_paginationPrev_loc.replace('%title',fileName))

    def click_MultiFormManagementDialog_paginationNext(self,fileName,*args):
        '''批量管理页面翻页下一页按钮'''
        self.clickElemByCSS_visibility(self.MultiFormManagementDialog_paginationNext_loc.replace('%title',fileName))

    def click_MultiFormManagementDialog_paginationNumber(self,fileName,PageNumber,*args):
        '''批量管理页面点击具体页数'''
        self.clickElemByCSS_visibility(self.MultiFormManagementDialog_paginationNumber_loc.replace('%title',fileName).replace('%n',PageNumber))




    def MultiForm_BathManagePage_Record_Tick(self,fileName,rowIndexList,*args):
        '''勾选批量管理页面关联表记录'''
        for rowIndex in rowIndexList:
            str_rowIndex = str(rowIndex-1)
            self.clickElemByCSS_visibility (self.MultiFormManagementDialog_selected_loc.replace ('%title', fileName).replace('%rowIndex',str_rowIndex))
            time.sleep(1)

    def MultiForm_GetTdValue( self,fileName,row,col,*args):
        '''获取多表关联组件中间表单元格值'''
        text = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.MultiForm_Td_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(col))).text
        if(text==""):
            text = self.getElemAttrValue(self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.MultiForm_Td_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(col))+"//input"),"value")
        return text


    def MultiForm_RelationForm_GetTdValue( self,fileName,row,col,*args):
        '''获取多表关联组件关联表单元格值'''
        tdElem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.MultiForm_RelationForm_Td_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(col)))
        if tdElem!=None:
            text = tdElem.text
            if(text==""):
                text = self.getElemAttrValue(self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.MultiForm_RelationForm_Td_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(col))+"//input"),"value")
            return text
        else:
            #关联表数据为空
            return None





    def MultiForm_BathManagePage_ConfirmButton_Tick(self,fileName,*args):
        '''点击批量管理页面确认按钮'''
        self.clickElemByCSS_visibility (self.MultiFormManagementDialog_ConfirmButton_loc.replace ('%title', fileName))


    def click_MultiFormManagementDialog_CancelButton(self,fileName,*args):
        '''点击批量管理页面取消按钮'''
        self.clickElemByCSS_visibility (self.MultiFormManagementDialog_CancelButton_loc.replace ('%title', fileName))

    def delete_MultiForm_Record(self):
        '''删除多表记录'''
        pass



    #
    def sendkeys_To_MultiFormText(self,multiformTitle,row,TextTitle,key):
        '''给多表批量管理页面的中间表的单行文本组件字段添加数据
        multiformTitle :多表字段名
        row：行数
        TextTitle：文本字段标题
        key：文本值
        '''
        reallyRow = str(row-1)
        self.sendkeysElemByCSS_Presence(self.MultiFormManagementDialog__Input_loc.replace('%title',multiformTitle).replace('%rowIndex',reallyRow).replace('%filename',TextTitle),key)


    # 给多表批量管理页面的中间表的数字组件字段添加数据

    # 给多表批量管理页面的中间表的多行文本组件字段添加数据

    # 给多表批量管理页面的中间表的选择框组件字段添加数据
    def sendkeys_To_MultiFormSelect(self,multiformTitle,row,SelectTitle,list,*args):
        '''
        multiformTitle :子表字段名
        row：行数
        TextTitle：文本字段标题
        key：文本值
        '''
        reallyRow = str (row - 1)
        self.clickElemByCSS_visibility (self.MultiFormManagementDialog__Input_loc.replace ('%title', multiformTitle).replace ('%rowIndex', reallyRow).replace ('%filename',SelectTitle))
        for i in list:
            self.clickElemByCSS_visibility(self.MultiForm_SelectOption_loc.replace('%option',i),index=1)

    #
    def sendkeys_To_MultiFormDate(self,MultiFormTitle,DateTitle,row,key):
        '''给多表批量管理页面的中间表的日期组件字段添加数据
        MultiFormTitle :子表字段名
        DateTitle：日期字段标题
        key：文本值
        '''
        reallyRow = str(row-1)
        self.sendkeysElemByCSS_Presence(self.MultiFormManagementDialog__Input_loc.replace('%title',MultiFormTitle).replace('%rowIndex',reallyRow).replace('%filename',DateTitle),key)
        self.clickElemByCSS_visibility(self.MultiFormManagementDialog__dialogfooter_loc,index=2)

    #
    def sendkeys_To_MultiFormDateTime(self, MultiFormTitle,DateTimeTitle, row, dateKey,timeKey):
        '''给多表批量管理页面的中间表的日期时间组件字段添加数据
        MultiFormTitle :子表字段名
        DateTimeTitle：日期时间字段标题
        key：文本值
        '''
        reallyRow = str(row-1)
        #日期输入框
        self.sendkeysElemByCSS_Presence(self.MultiFormManagementDialog__Input_loc.replace('%title',MultiFormTitle).replace('%rowIndex',reallyRow).replace('%filename',DateTimeTitle),dateKey, index=0)
        self.clickElemByCSS_visibility (self.MultiFormManagementDialog__dialogfooter_loc, index=2)
        #时间输入框
        self.sendkeysElemByCSS_Presence(self.MultiFormManagementDialog__Input_loc.replace('%title',MultiFormTitle).replace('%rowIndex',reallyRow).replace('%filename',DateTimeTitle),dateKey, index=1)
        self.clickElemByCSS_visibility (self.MultiFormManagementDialog__dialogfooter_loc, index=2)

    #
    def sendkeys_To_MultiFormTime(self,MultiFormTitle,TimeTitle,row,key):
        '''给多表批量管理页面的中间表的时间组件字段添加数据
        MultiFormTitle :子表字段名
        TimeTitle：时间字段标题
        key：文本值
        '''
        reallyRow = str(row-1)
        self.sendkeysElemByCSS_Presence(self.MultiFormManagementDialog__Input_loc.replace('%title',MultiFormTitle).replace('%rowIndex',reallyRow).replace('%filename',TimeTitle),key)
        #点击底部
        self.clickElemByCSS_visibility (self.MultiFormManagementDialog__dialogfooter_loc, index=2)

    # 给多表批量管理页面的中间表的富文本组件字段添加数据

    #
    def sendkeys_To_ChildPicUpload(self,MultiFormTitle,PicUploadTitle,row,picPath):
        '''给多表批量管理页面的中间表的图片上传组件字段添加数据
        MultiFormTitle :子表字段名
        row：行数
        PicUploadTitle：图片字段标题
        picPath：图片路径
        '''
        reallyRow = str(row-1)
        self.sendkeysElemByCSS_Presence(self.MultiFormManagementDialog__Input_loc.replace('%title',MultiFormTitle).replace('%rowIndex',reallyRow).replace('%filename',PicUploadTitle),picPath)

    # 给多表批量管理页面的中间表的文件上传组件字段添加数据

    # 给多表批量管理页面的中间表的人员选择组件字段添加数据

    # 给多表批量管理页面的中间表的部门选择组件字段添加数据

    # 给多表批量管理页面的中间表的地址选择组件字段添加数据

    # 给多表批量管理页面的中间表的级联选择组件字段添加数据
