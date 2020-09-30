#子表
import time

from public.selenium_page import SeleniumPage


class ChildForm_component(SeleniumPage):

    ChildForm_AddButton_loc ='[data-mark=%title] [data-mark=button_添加]'  #子表添加按钮

    ChildForm_AddOneRowButton_loc = "//div[@data-mark='%title']//button//span[text()='添加一行']" #子表添加一行按钮

    ChildForm_Input_loc = "[data-mark='%title'] .row_%title_%row [data-mark='%text'] input"  #子表输入框

    ChildForm_textarea_loc = "[data-mark='%title'] .row_%title_%row [data-mark='%text'] textarea"

    ChildForm_div_loc = "[data-mark='%title'] .row_%title_%row [data-mark='%text']"  # 子表输入框div


    ChildForm_SelectOption_loc = "//div[@id='app']/following-sibling::div[@class='el-select-dropdown el-popper %title']//li[@data-mark='%s']"   #下拉选项

    ChildForm_ForeignSelectOption_loc = "//div[@id='app']/following-sibling::div[1]//li[@data-mark='option_%s']"  #外键选项

    ChildForm_label_loc = "[data-mark='%title']>label"  #字段标题

    ChildForm_userSelect_loc = "[data-mark=%title] .row_%title_%row [data-mark=%user] [data-mark='选择人员按钮']"  #子表人员选择

    ChildForm_button_loc = "//button[contains(@class,'el-button')]/span[text()='%s']"

    ChildForm_CloseIcon_loc = "//div[contains(@data-mark,'子表弹层')]//i[@class='el-icon-close close']"

    ChildForm_Td_loc = "//div[@data-mark='%s']//tr[contains(@class,'el-table__row')][%row]//td[%col]"

    ChildForm_Td_shanchu_loc = "//div[@data-mark='%s']//div[@class='el-table__fixed']//tr[%row]//span[contains(@class,'shanchu')]"

    order_number_div = "//div[@data-mark='%s']//div[@class='el-table__body-wrapper is-scrolling-left']//div[@class='order_number']"

    def scroll_To_ChildForm_Div(self):
        self.scrollIntoView(self.ChildForm_div_loc)

    def ChildForm_Close(self):
        self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.ChildForm_CloseIcon_loc)

    def ChildForm_AddButton_Click(self,fieldName,*args):
        '''点击添加按钮
        fieldName：字段标题
        '''
        self.clickElemByCSS_visibility (self.ChildForm_AddButton_loc.replace ('%title', fieldName))

    def ChildForm_AddOneRowButton_Click(self,fieldName,*args):
        '''点击添加一行按钮
        fieldName：字段标题
        '''
        self.clickElemByXpath_visibility (self.ChildForm_AddOneRowButton_loc.replace ('%title', fieldName))

    def click_ChildForm_Button( self,buttonName ):
        '''点击子表按钮'''
        self.clickElemByXpath_visibility(self.ChildForm_button_loc.replace('%s',buttonName))



    def ChildForm_Record_Delete(self,fileName,row,index1=0):
        '''删除子表记录'''
        #悬浮到单元格
        td = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(
            self.ChildForm_Td_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(1)),index=index1)
        self.move_to_element(td)
        time.sleep(1)
        # 点击删除按钮
        tdshanchu = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.ChildForm_Td_shanchu_loc.replace('%s',fileName).replace('%row',str(row)))
        tdshanchu.click()
        # self.clickElemByXpath_visibility(self.ChildForm_Td_shanchu_loc)



    def ChildForm_GetTdValue( self,fileName,row,col,*args):
        '''获取子表组件表单元格值'''
        text = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.ChildForm_Td_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(col))).text
        if(text==""):
            text = self.getElemAttrValue(self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.ChildForm_Td_loc.replace('%s',fileName).replace('%row',str(row)).replace('%col',str(col))+"//input"),"value")
        return text



    def ChildForm_get_TotalRecordNumber(self,fileName):
        '''获取子表记录数'''
        elems = self.find_elemsByXPATH_presence(self.order_number_div.replace('%s',fileName))
        if(elems!=None):
            return len(elems)
        else:
            return 0

########给子表行字段添加数据方法

    def ChildForm_List_Text_sendkeys(self,childformTitle,row,TextTitle,key):
        '''给子表的单行文本组件输入值'''
        # childformTitle :子表字段名
        # row：行数
        # TextTitle：文本字段标题
        # key：文本值
        reallyRow = str(row - 1)
        self.sendkeysElemByCSS_Presence(self.ChildForm_Input_loc.replace('%title',childformTitle).replace('%row',reallyRow).replace('%text',TextTitle),key,isclear=True)


    def ChildForm_List_Textarea_sendkeys(self,childformTitle,row,TextTitle,key):
        '''给子表的多行文本组件输入值'''
        # childformTitle :子表字段名
        # row：行数
        # TextTitle：文本字段标题
        # key：文本值
        reallyRow = str(row - 1)
        self.sendkeysElemByCSS_Presence(self.ChildForm_textarea_loc.replace('%title',childformTitle).replace('%row',reallyRow).replace('%text',TextTitle),key,isclear=True)


    def ChildForm_List_Number_sendkeys(self,childformTitle,NumberTitle,row,key):
        '''给子表的数字组件输入值'''
        # childformTitle :子表字段名
        # row：行数
        # TextTitle：文本字段标题
        # key：文本值
        reallyRow = str(row - 1)
        self.sendkeysElemByCSS_Presence(self.ChildForm_Input_loc.replace('%title',childformTitle).replace('%row',reallyRow).replace('%text',NumberTitle),key,isclear=True)

    def ChildForm_List_ForeignSelection_sendkeys(self,childformTitle,row,TextTitle,option):
        '''给子表的外键组件输入值'''
        # childformTitle :子表字段名
        # row：行数
        # TextTitle：文本字段标题
        # option：选项值
        reallyRow = str(row - 1)
        self.clickElemByCSS_visibility(self.ChildForm_Input_loc.replace('%title',childformTitle).replace('%row',reallyRow).replace('%text',TextTitle))
        #选择选项
        self.clickElemByXpath_visibility(self.ChildForm_ForeignSelectOption_loc.replace('%s',option))


    def ChildForm_List_Select_sendkeys(self,childformTitle,row,SelectTitle,list,*args):
        '''给子表的选择框组件字段添加数据'''
        # childformTitle :子表字段名
        # row：行数
        # TextTitle：文本字段标题
        # key：文本值
        # '''
        reallyRow = str (row - 1)
        self.clickElemByCSS_visibility (self.ChildForm_Input_loc.replace ('%title', childformTitle).replace ('%row', reallyRow).replace ('%text',SelectTitle))
        for i in list:
            self.clickElemByXpath_visibility(self.ChildForm_SelectOption_loc.replace('%title',SelectTitle).replace('%s',i))


    def ChildForm_List_Date_sendkeys(self,childformTitle,DateTitle,row,key):
        '''给子表的日期组件字段添加数据   '''
        # childformTitle :子表字段名
        #         # DateTitle：日期字段标题
        #         # key：文本值
        reallyRow = str(row-1)
        self.sendkeysElemByCSS_Presence(self.ChildForm_Input_loc.replace('%title',childformTitle).replace('%row',reallyRow).replace('%text',DateTitle),key,isclear=True)
        self.clickElemByCSS_visibility(self.ChildForm_label_loc.replace('%title',childformTitle))


    def ChildForm_List_DateTime_sendkeys(self, childformTitle,DateTimeTitle, row, dateKey,timeKey):
        '''给子表的日期时间组件字段添加数据
        childformTitle :子表字段名
        DateTimeTitle：日期时间字段标题
        key：文本值
        '''
        reallyRow = str(row-1)
        self.sendkeysElemByCSS_Presence(self.ChildForm_Input_loc.replace('%title',childformTitle).replace('%row',reallyRow).replace('%text',DateTimeTitle),dateKey, index=0)
        self.clickElemByCSS_visibility (self.ChildForm_label_loc.replace ('%title', childformTitle))
        self.sendkeysElemByCSS_Presence (
            self.ChildForm_Input_loc.replace ('%title', childformTitle).replace ('%row', reallyRow).replace ('%text',
                                                                                                             DateTimeTitle),
            dateKey, index=1)
        self.clickElemByCSS_visibility (self.ChildForm_label_loc.replace ('%title', childformTitle))




    def ChildForm_List_Time_sendkeys(self,childformTitle,TimeTitle,row,key):
        '''给子表的时间组件字段添加数据
        childformTitle :子表字段名
        TimeTitle：时间字段标题
        key：文本值
        '''
        reallyRow = str(row-1)
        self.sendkeysElemByCSS_Presence(self.ChildForm_Input_loc.replace('%title',childformTitle).replace('%row',reallyRow).replace('%text',TimeTitle),key)
        self.clickElemByCSS_visibility (self.ChildForm_label_loc.replace ('%title', childformTitle))

    # 给子表的富文本组件字段添加数据

    #
    def ChildForm_List_PicUpload_sendkeys(self,childformTitle,PicUploadTitle,row,picPath):
        '''给子表的图片上传组件输入值
        childformTitle :子表字段名
        row：行数
        PicUploadTitle：图片字段标题
        picPath：图片路径
        '''
        reallyRow = str(row-1)
        self.sendkeysElemByCSS_Presence(self.ChildForm_Input_loc.replace('%title',childformTitle).replace('%row',reallyRow).replace('%text',PicUploadTitle),picPath)


    #
    def ChildForm_List_User_sendkeys(self,childformTitle,UserTitle,row,userNameList):
        '''给子表的人员选择组件字段添加数据'''
        # childformTitle :子表字段名
        # row：行数
        # UserTitle：人员字段标题

        reallyRow = str(row-1)
        #点击人员选择
        self.clickElemByCSS_visibility(self.ChildForm_userSelect_loc.replace('%title',childformTitle).replace('%row',reallyRow).replace('%user',UserTitle))

        for name in userNameList:
            self.clickElemByXpath_visibility (self.User_search_loc)
            self.sendkeysElemByXpath_visibility (self.User_search_loc, name)
            self.clickElemByXpath_visibility (self.User_searchOption_loc.replace ('%s', name))
        self.clickElemByXpath_visibility (self.User_querenButton_loc)


    # 给子表的部门选择组件字段添加数据

    # 给子表的地址选择组件字段添加数据

    # 给子表的级联选择组件字段添加数据



    # 给子表的单项选择组件输入值



