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

    MultiForm_Td_loc = "//div[@data-mark='%s']//tr[contains(@class,'el-table__row')][%row]//td[%col]"

    MultiForm_Td_span_loc = "//div[@data-mark='%s']//tr[contains(@class,'el-table__row')][%row]//td[%col]//span[@class='overflow-text-span']"

    MultiForm_Td_input_loc = "//div[@data-mark='%s']//tr[contains(@class,'el-table__row')][%row]//td[%col]//input"

    MultiForm_Td_cell_loc = "//div[@data-mark='%s']//tr[contains(@class,'el-table__row')][%row]//td[%col]//div[@class='cell']"

    MultiForm_RelationForm_Td_loc = "//div[@data-mark='%s_table']//div[@class='el-table__body-wrapper is-scrolling-left']//tr[@class='el-table__row'][%row]//td[%col]//span"

    order_div = "//div[@data-mark='%s']//div[@class='el-table__fixed']//div[@class='order_number' and contains(text(),'%row')]"

    order_number_div = "//div[@data-mark='%s']//div[@class='el-table__fixed']//div[@class='order_number']"

    order_number_shanchu_span = "//div[@data-mark='%s']//div[@class='el-table__fixed']//div[@class='order_number' and contains(text(),'%row')]/parent::div//span[contains(@class,'shanchu')]"

    order_number_bianji_span = "//div[@data-mark='%s']//div[@class='el-table__fixed']//div[@class='order_number' and contains(text(),'%row')]/parent::div//span[contains(@class,'iconfont iconbianji primary_color')]"

    Selection_monomialSelectOption_loc = "//div[@id='app']//li[@data-mark='%value']"  #下拉单选选项

     #"//div[@id='app']//li[@data-mark='option_%value']"
    ForeignSelection_loc ="//div[@id='app']/following-sibling::div[@class='el-select-dropdown el-popper load_more']//span[text()='%value']/parent ::li"  # 外键选项""
    foreignSelectOptions_loc="//div[@id='app']/following-sibling::div[@class='el-select-dropdown el-popper %s ']//li[contains(@data-mark,'option_')]"
#多表关联组件外部操作

    def MultiForm_get_OptionValue(self,fileName,*args):
        '''获取下拉选项值'''
        list = []
        elems = self.find_elemsByXPATH_presence(self.foreignSelectOptions_loc.replace('%s',fileName))
        if elems == None:
            return list
        for elem in elems:
            list.append(elem.text)
        return list

    def MultiForm_Option_scrollDown( self,fieldName,scrollNumber=10):
        '''多表关联外键选项滚动至底部'''
        js = "document.getElementsByClassName('%s')[0].children[0].children[0].scrollTop=100000" %fieldName
        for n in range(1,scrollNumber):
            self.driver.execute_script(js)  # 从上往下滑
            time.sleep(0.5)

    def MultiForm_BatchManagementButton_Click(self,fileName,*args):
        '''点击批量管理按钮'''
        self.clickElemByCSS_visibility(self.MultiFormAssociation_HandleManagerButton_loc.replace('%title',fileName))


    def MultiForm_AddButton_Click(self,fileName,*args):
        '''点击添加按钮'''
        self.clickElemByCSS_visibility (self.MultiFormAssociation_AddButton_loc.replace ('%title', fileName))


    def MultiForm_GetTdValue( self,fileName,row,col,*args):
        '''获取多表关联组件中间表数据列表中单元格值'''
        text = self.find_elemByXPATH_presence(self.MultiForm_Td_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(col))).text
        if(text==""):
            text = self.getElemAttrValue(self.find_elemByXPATH_presence(self.MultiForm_Td_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(col))+"//input"),"value")
        return text

    def MultiForm_delete_Record(self,fileName,row):
        '''删除多表记录'''
        #鼠标移至删除的数据的序列号
        elem = self.find_elemByXPATH_visibility(self.order_div.replace('%s',fileName).replace('%row',str(row)))
        self.move_to_element(elem)
        time.sleep(1.5)
        #点击删除按钮
        self.clickElemByXpath_visibility(self.order_number_shanchu_span.replace('%s',fileName).replace('%row',str(row)))

    def MultiForm_edit_Record(self,fileName,row):
        '''编辑多表记录'''
        #鼠标移至数据的序列号
        elem = self.find_elemByXPATH_visibility(self.order_div.replace('%s',fileName).replace('%row',str(row)))
        self.move_to_element(elem)
        time.sleep(1.5)
        #点击编辑按钮
        self.clickElemByXpath_visibility(self.order_number_bianji_span.replace('%s',fileName).replace('%row',str(row)))

    def MultiForm_Click_Row(self,fileName,row):
        '''多表关联组件点击行'''
        elem = self.find_elemByXPATH_visibility(self.order_div.replace('%s',fileName).replace('%row',str(row)))
        self.clickElem(elem)


    def MultiForm_List_sendkeysTo_Number(self,fileName,row,col,key):
        '''给多表数据列表的中间表的数字组件字段添加数据'''
        # multiformTitle :多表字段名
        # row：行数
        # TextTitle：文本字段标题
        # key：文本值
        self.sendkeysElemByXpath_visibility(self.MultiForm_Td_input_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(col)),key)

    def MultiForm_List_click_Td( self,fileName,row,col ):
       '''点击输入框使其变成可编辑状态'''
       self.clickElemByXpath_visibility(self.MultiForm_Td_cell_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(col)))
       time.sleep(1)



    def MultiForm_List_sendkeysTo_SingleXiala(self,fileName,row,col,value):
        '''给多表数据列表的中间表的单项选择组件字段添加数据'''
        # multiformTitle :多表字段名
        # row：行数
        # TextTitle：文本字段标题
        # value：文本值
        self.clickElemByXpath_visibility(self.MultiForm_Td_input_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(col)))
        time.sleep(1)
        self.wait_elem_visible_XPATH(self.Selection_monomialSelectOption_loc.replace('%value',value))
        # 点击选项
        self.clickElemByXpath_visibility(self.Selection_monomialSelectOption_loc.replace('%value',value))


    def MultiForm_List_ForeignSelection_sendkeys(self,fileName,row,col,value):
        '''给多表的外键组件输入值'''
        # childformTitle :子表字段名
        # row：行数
        # TextTitle：文本字段标题
        # option：选项值
        self.clickElemByXpath_visibility(self.MultiForm_Td_input_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(col)))
        # 点击选项
        self.clickElemByXpath_visibility(self.ForeignSelection_loc.replace('%value',value))


    # def MultiForm_get_TotalRecordNumber(self,fileName):
    #     '''获取多表记录数'''
    #     elems = self.find_elemsByXPATH_visibility(self.order_number_div.replace('%s',fileName))
    #     if(elems!=None):
    #         return len(elems)
    #     else:
    #         return 0
    # #




























# 多表关联组件批量管理页面内操作

    def MultiForm_click_MultiFormManagementDialog_paginationPrev(self,fileName,*args):
        '''批量管理页面翻页上一页按钮'''
        self.clickElemByCSS_visibility(self.MultiFormManagementDialog_paginationPrev_loc.replace('%title',fileName))

    def MultiForm_click_MultiFormManagementDialog_paginationNext(self,fileName,*args):
        '''批量管理页面翻页下一页按钮'''
        self.clickElemByCSS_visibility(self.MultiFormManagementDialog_paginationNext_loc.replace('%title',fileName))

    def MultiForm_click_MultiFormManagementDialog_paginationNumber(self,fileName,PageNumber,*args):
        '''批量管理页面点击具体页数'''
        self.clickElemByCSS_visibility(self.MultiFormManagementDialog_paginationNumber_loc.replace('%title',fileName).replace('%n',PageNumber))


    def MultiForm_BathManagePage_Record_Tick(self,fileName,rowIndexList,*args):
        '''勾选批量管理页面关联表记录'''
        for rowIndex in rowIndexList:
            str_rowIndex = str(rowIndex-1)
            self.clickElemByCSS_presence (self.MultiFormManagementDialog_selected_loc.replace ('%title', fileName).replace('%rowIndex',str_rowIndex),index=1)
            time.sleep(2)


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


    def MultiForm_click_MultiFormManagementDialog_CancelButton(self,fileName,*args):
        '''点击批量管理页面取消按钮'''
        self.clickElemByCSS_visibility (self.MultiFormManagementDialog_CancelButton_loc.replace ('%title', fileName))



    def MultiForm_BathManagePage_sendkeysTo_Text(self,multiformTitle,row,TextTitle,key):
        '''给多表批量管理页面内的中间表的单行文本组件字段添加数据
        multiformTitle :多表字段名
        row：行数
        TextTitle：文本字段标题
        key：文本值
        '''
        reallyRow = str(row-1)
        self.sendkeysElemByCSS_Presence(self.MultiFormManagementDialog__Input_loc.replace('%title',multiformTitle).replace('%rowIndex',reallyRow).replace('%filename',TextTitle),key)



    def MultiForm_BathManagePage_sendkeysTo_Number(self,multiformTitle,row,NumberTitle,key):
        '''给多表批量管理页面内的中间表的数字组件字段添加数据'''
        # multiformTitle :多表字段名
        # row：行数
        # TextTitle：文本字段标题
        # key：文本值

        reallyRow = str(row-1)
        self.sendkeysElemByCSS_Presence(self.MultiFormManagementDialog__Input_loc.replace('%title',multiformTitle).replace('%rowIndex',reallyRow).replace('%filename',NumberTitle),str(key))



    # 给多表批量管理页面的中间表的选择框组件字段添加数据
    def MultiForm_BathManagePage_sendkeys_To_Select(self,multiformTitle,row,SelectTitle,list,*args):
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
    def MultiForm_BathManagePage_sendkeys_To_Date(self,MultiFormTitle,DateTitle,row,key):
        '''给多表批量管理页面的中间表的日期组件字段添加数据
        MultiFormTitle :子表字段名
        DateTitle：日期字段标题
        key：文本值
        '''
        reallyRow = str(row-1)
        self.sendkeysElemByCSS_Presence(self.MultiFormManagementDialog__Input_loc.replace('%title',MultiFormTitle).replace('%rowIndex',reallyRow).replace('%filename',DateTitle),key)
        self.clickElemByCSS_visibility(self.MultiFormManagementDialog__dialogfooter_loc,index=2)

    #
    def MultiForm_BathManagePage_sendkeys_To_DateTime(self, MultiFormTitle,DateTimeTitle, row, dateKey,timeKey):
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
    def MultiForm_BathManagePage_sendkeys_To_Time(self,MultiFormTitle,TimeTitle,row,key):
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
    def MultiForm_BathManagePage_sendkeys_To_PicUpload(self,MultiFormTitle,PicUploadTitle,row,picPath):
        '''给多表批量管理页面的中间表的图片上传组件字段添加数据
        MultiFormTitle :子表字段名
        row：行数
        PicUploadTitle：图片字段标题
        picPath：图片路径
        '''
        reallyRow = str(row-1)
        self.sendkeysElemByCSS_Presence(self.MultiFormManagementDialog__Input_loc.replace('%title',MultiFormTitle).replace('%rowIndex',reallyRow).replace('%filename',PicUploadTitle),picPath)

