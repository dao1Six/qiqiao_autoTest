
import time
from public.selenium_page import SeleniumPage

class ListComponent(SeleniumPage):

    app_home_loc="//a[text()='应用']"
    app_name_loc="//p[@title='{appname}']/../.."
    left_meau_loc="//span[@title='{pagename}']"
    tab_base_loc = "//div[contains(text(),'{tablename}')]"

    search_data_loc = "//label[@for='{feildname}']/following-sibling::div/div/div/input"
    search_base_loc = "//label[@for='{feildname}']/following-sibling::div/div/div/div/input"
    search_digital_loc = "//label[@for='{feildname}']/following-sibling::div/div/div/div/input"
    search_choice_loc = "//label[@for='{feildname}']/following-sibling::div/div/div/div/input"
    search_li_loc = "//div[@id='app']/following-sibling::div/div/div/ul/li"
    li_selector_loc = "//div[@id='app']/following-sibling::div/div/div/ul/li[{indexnum}]"

    search_address_loc = "//label[@for='{feildname}']/following-sibling::div/div/span"
    

    search_creator_loc = "//label[@for='author_name']/following-sibling::div/div/div/div/input"
    search_startdate_loc = "//label[@for='{feild}']/following-sibling::div/div/div/input[1]"
    search_enddate_loc = "//label[@for='{feild}']/following-sibling::div/div/div/input[2]"

    btn_base_loc = "//div[@class='view_toolbar_panel']/div"
    btn_name_loc = "//div[@class='view_toolbar_panel']/div[{indexnum}]/button/span"
    input_base_loc = "//form[@class='el-form el-form--label-right']//label[@for='{feildname}']/following-sibling::div//input"
    input_textarea_loc = "//form[@class='el-form el-form--label-right']//label[@for='{feildname}']/following-sibling::div//textarea"
    input_datetime_loc = "//form[@class='el-form el-form--label-right']//label[@for='{feildname}']/following-sibling::div/div/div[1]/input"
    input_datetime_loc2 = "//form[@class='el-form el-form--label-right']//label[@for='{feildname}']/following-sibling::div/div/div[2]/div/input"

    #six
    ListHeader_Button_loc = "//div[@class='listView_headerButtonWrapper']//div[@data-mark='%s']"  #列表头部按钮
    ListHeader_Buttons_loc = "//div[@class='listView_headerButtonWrapper']//div[@class='view_toolbar_panel']/div"  # 列表头部按钮

    tablist_loc = "//div[@role='tablist']//div[@role='tab']"
    search_btn_loc = "//button[@data-mark='筛选条件搜索按钮']"   #列表组件的搜索按钮
    reset_btn_loc = "//button[@data-mark='筛选条件重置按钮']"  #列表组件的重置按钮
    expand_btn_loc = "//div[@class='view_search_panel']//span[@class='expand']" #列表组件的展开收起按钮
    QueryItem_loc = "//div[@class='view_search_panel']//div[@data-mark='%s']//input"  #列表查询项文本框
    address_option_loc = "//span[text()='{addressname}']"  #地址选择器选项
    li_selectOption_loc ="//div[@class='el-scrollbar']//div[@title='%s']"  #下拉框选项
    selectOptionName_loc = "//div[@data-mark='%s']//span[@title='%s']"  #查询项标题
    listTable_td_loc = "//div[contains(@class,'el-table__body-wrapper')]//tr[%row]//td[%col]//span" #列表单元格

    listTable_checkbox_loc = "//div[@class='el-table__fixed-body-wrapper']//tr[%row]//td[1]//label//span[@class='el-checkbox__inner']" #列表勾选框

    ListRow_Button_loc = "//span[@data-mark='%s_%row']/button/span[text()='%s']" #列表行按钮

    ListRow_MoreButton_loc = "//div[contains(@class,'el-table__body-wrapper')]//tr[%row]//span[contains(text(),'更多')]/parent::div[1]"#列表行更多按钮

    ListRow_SelectAllInput_loc = "//div[contains(@class,'el-table__fixed-header-wrapper')]//th[1]//span[@class='el-checkbox__inner']" #列表首行全选元素

    TooltipButton_loc = "//div[@role='tooltip']//button//span[text()='%s']"
    dialogfooterButton = "//div[@class='el-dialog__footer']//button/span[text()='%s']"
    pagination_total_loc = "//span[@class='el-pagination__total']"
    containerViewOption_loc = "//div[@class='el-tabs__header is-top']//span[text()='%s']"
    ColHeader_sort_down_loc = "//tr//span[@title='%s']/ancestor::div[@class='cell']//i[@class='sort-caret descending']"
    ColHeader_sort_up_loc = "//tr//span[@title='%s']/ancestor::div[@class='cell']//i[@class='sort-caret ascending']"
    ColHeader_iconxiala = "//tr//span[@title='%s']/ancestor::div[@class='cell']//i[contains(@class,'iconxiala')]"
    ColHeader_checkbox = "//div[@class='content']//label[contains(@class,'el-checkbox')]"
    ColHeader_confirm_btn = "//div[@class='content']/following-sibling::div//span[@class='confirm_btn']"




    def ListComponent_GetRecordTotal(self,index=0):
        '''获取列表总条数'''
        text = self.find_elemsByXPATH_visibility(self.pagination_total_loc)[index].text
        num = int(text[1:-1])
        return num

    def ListComponent_SelectAllRecord( self ):
        '''全选数据'''
        self.clickElemByXpath_visibility(self.ListRow_SelectAllInput_loc)

    def ListComponent_TooltipButton_Click( self,ButtonNmae ):
        '''点击列表按钮消息提示框按钮'''
        self.clickElemByXpath_visibility(self.TooltipButton_loc.replace('%s',ButtonNmae))

    def ListComponent_dialogfooterButton_Click( self,ButtonNmae ):
        '''点击列表按钮弹框按钮'''
        self.clickElemByXpath_visibility(self.dialogfooterButton.replace('%s',ButtonNmae))

    def ListComponent_get_tablistValule( self ):
        '''获取列表所有选项卡文本值'''
        tablist = []
        elems = self.find_elemsByXPATH_visibility(self.tablist_loc)
        for elem in elems:
            tablist.append(elem.text)
        return tablist


    def ListComponent_containerViewOption_Click( self,option ):
        '''点击容器视图选项'''
        self.clickElemByXpath_visibility(self.containerViewOption_loc.replace('%s',option))

    def ListComponent_ColHeader_sort( self,ColName,sortType):
        '''点击列头排序按钮,sortType等于0为升序，sortType等于1为降序'''
        if(sortType==0):
            self.clickElemByXpath_visibility(self.ColHeader_sort_up_loc.replace('%s',ColName))
        elif(sortType==1):
            self.clickElemByXpath_visibility(self.ColHeader_sort_down_loc.replace('%s',ColName))

    def ListComponent_ColHeader_search( self,ColName,searchList):
        '''列头筛选'''
        #点击列的筛选下拉按钮
        self.clickElemByXpath_visibility(self.ColHeader_iconxiala.replace('%s',ColName))
        #勾选筛选项
        for i in searchList:
            self.clickElemByXpath_visibility(self.ColHeader_checkbox,index=i-1)
        #点击确定按钮
        self.clickElemByXpath_visibility(self.ColHeader_confirm_btn)


    def ListComponent_Click_ListHeader_Button( self, btnname ):
        '''点击列表头部按钮'''
        self.clickElemByXpath_visibility(self.ListHeader_Button_loc.replace('%s', btnname))

    def ListComponent_Get_ListHeader_Buttons( self):
        '''获取列表头部按钮'''
        buttonList = []
        elems = self.find_elemsByXPATH_visibility(self.ListHeader_Buttons_loc)
        for elem in elems:
            buttonList.append(elem.text)
        return buttonList

    def ListComponent_Click_ListRow_Button( self, btnname,row):
        '''点击列表行按钮'''
        self.clickElemByXpath_visibility(self.ListRow_Button_loc.replace('%s', btnname).replace('%row',str(row-1)))

    def ListComponent_MoveTo_ListRow_MoreButton( self,row):
        '''悬浮列表行更多按钮'''
        elem = self.find_elenmInElemsByXpath_presence_of_all_elements_located(self.ListRow_MoreButton_loc.replace('%row',str(row)))
        self.move_to_element(elem)

    def ListComponent_Click_SerachBtn( self ):
        '''点击筛选数据的搜索按钮'''
        self.clickElemByXpath_visibility(self.search_btn_loc)

    def ListComponent_Click_ResetBtn( self ):
        '''点击筛选数据的重置按钮'''
        self.clickElemByXpath_visibility(self.reset_btn_loc)

    def ListComponent_Click_ExpandBtn( self ):
        '''点击展开收起按钮'''
        self.clickElemByXpath_visibility(self.expand_btn_loc)

    def ListComponent_GetTable_Td_Value( self ,row,col):
        '''获取列表单元格值'''
        elem = self.find_elenmInElemsByXpath_presence_of_all_elements_located(self.listTable_td_loc.replace('%row',str(row)).replace('%col',str(col)))
        if(elem==None):
            return None
        return elem.text
    
    def ListComponent_TableTd_Click( self ,row,col):
        '''点击表单元格值'''
        self.clickElemByXpath_visibility(self.listTable_td_loc.replace('%row',str(row)).replace('%col',str(col)))

    def ListComponent_checkbox_Click( self ,row):
        '''点击列表勾选框'''
        self.clickElemByXpath_visibility(self.listTable_checkbox_loc.replace('%row',str(row)))

    def ListComponent_QueryItem_Sendkeys( self, itemName, keys, *args,QueryItemType="text"):
        '''列表组件的查询项输入值
        :type QueryItemType: object
        '''
        try:
            # 文本类型
            if (QueryItemType == "text"):
                self.sendkeysElemByXpath_visibility(self.QueryItem_loc.replace('%s', itemName), keys)

            # 日期类型
            elif (QueryItemType == "date"):
                #开始
                self.clickElemByXpath_visibility(self.QueryItem_loc.replace('%s', itemName), index=0)
                self.sendkeysElemByXpath_visibility(self.QueryItem_loc.replace('%s', itemName), keys, index=0)
                #结束
                self.clickElemByXpath_visibility(self.QueryItem_loc.replace('%s', itemName), index=1)
                self.sendkeysElemByXpath_visibility(self.QueryItem_loc.replace('%s', itemName), args[0], index=1)
            #时间
            elif (QueryItemType == "time"):
                # 开始
                self.clickElemByXpath_visibility(self.QueryItem_loc.replace('%s', itemName), index=0)
                self.sendkeysElemByXpath_visibility(self.QueryItem_loc.replace('%s', itemName), keys, index=0)
                # 结束
                self.clickElemByXpath_visibility(self.QueryItem_loc.replace('%s', itemName), index=1)
                self.sendkeysElemByXpath_visibility(self.QueryItem_loc.replace('%s', itemName), args[0], index=1)
            #日期时间
            elif (QueryItemType == "datetime"):
                self.sendkeysElemByXpath_visibility(self.QueryItem_loc.replace('%s', itemName), keys)

            # 地址选择器类型
            elif (QueryItemType == "address"):
                # 点击地址输入框
                self.clickElemByXpath_visibility("//span[@data-mark='地址选择下拉框']")
                address = str(keys)
                if "/" not in address:
                    raise Exception("地址输入格式不正确或者地址不存在，请使用如下输入格式：河南省/郑州市/金水区")
                else:
                    # 将地址划分
                    sp = address.split("/")
                    for i in sp:
                        # 点击选项
                        self.clickElemByXpath_visibility(self.address_option_loc.format(addressname=i))
            # 下拉框类型
            elif (QueryItemType == "option"):
                # 点击文本框
                self.clickElemByXpath_visibility(self.QueryItem_loc.replace('%s', itemName))
                # 点击选项
                if(type(keys)==type("sasdr")):
                    #下拉单选
                    self.clickElemByXpath_visibility(self.li_selectOption_loc.replace('%s', keys))
                elif(type(keys)==type([1,2])):
                    #下拉多选
                    for key in keys:
                        self.clickElemByXpath_visibility(self.li_selectOption_loc.replace('%s', key))

            # 人员部门类型
            elif (QueryItemType == "user"):
                # 向文本框输入值
                self.sendkeysElemByXpath_visibility(self.QueryItem_loc.replace('%s', itemName), keys)
                # 点击选项
                self.clickElemByXpath_visibility(self.li_selectOption_loc.replace('%s', keys))
            else:
                print("类型值为：" + type)
                raise Exception("查询项无此类型，请检查type参数的值")
        finally:
            # 点击一下选项标题，使光标离开
            self.clickElemByXpath_visibility(self.selectOptionName_loc.replace('%s', itemName))














