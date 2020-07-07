
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
    search_btn_loc = "//button[@data-mark='筛选条件搜索按钮']"   #列表组件的搜索按钮
    reset_btn_loc = "//button[@data-mark='筛选条件重置按钮']"  #列表组件的重置按钮
    expand_btn_loc = "//div[@class='view_search_panel']//span[@class='expand']" #列表组件的展开收起按钮
    QueryItem_loc = "//div[@class='view_search_panel']//div[@data-mark='%s']//input"  #列表查询项文本框
    address_option_loc = "//span[text()='{addressname}']"  #地址选择器选项
    li_selectOption_loc ="//div[@class='el-scrollbar']//div[@title='%s']"  #下拉框选项
    selectOptionName_loc = "//div[@data-mark='%s']//span[@title='%s']"  #查询项标题
    listTable_td_loc = "//div[contains(@class,'el-table__body-wrapper')]//tr[%row]//td[%col]//span" #列表单元格

    ListRow_Button_loc = "//span[@data-mark='%s_%row']/button/span[text()='%s']" #列表行按钮

    ListRow_MoreButton_loc = "//div[contains(@class,'el-table__body-wrapper')]//tr[%row]//span[contains(text(),'更多')]/parent::div[1]"#列表行更多按钮

    ListRow_SelectAllInput_loc = "//div[contains(@class,'el-table__fixed-header-wrapper')]//th[1]//span[@class='el-checkbox__inner']" #列表首行全选元素

    TooltipButton_loc = "//div[@role='tooltip']//button//span[text()='确定']"

    pagination_total_loc = "//span[@class='el-pagination__total']"
    tabsOption_loc = "//div[@class='el-tabs__header is-top']//span[text()='%s']"

    def ListComponent_GetRecordTotal(self):
        '''获取列表总条数'''
        text = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.pagination_total_loc).text
        num = int(text[1:-1])
        return num

    def ListComponent_SelectAllRecord( self ):
        '''全选数据'''
        self.clickElemByXpath_visibility(self.ListRow_SelectAllInput_loc)

    def ListComponent_TooltipButton_Click( self,ButtonNmae ):
        '''点击列表按钮提示框按钮'''
        self.clickElemByXpath_visibility(self.TooltipButton_loc.replace('%s',ButtonNmae))


    def ListComponent_TabsOption_Click( self,option ):
        '''点击选项卡'''
        self.clickElemByXpath_visibility(self.tabsOption_loc.replace('%s',option))


    def ListComponent_Click_ListHeader_Button( self, btnname ):
        '''点击列表头部按钮'''
        self.clickElemByXpath_visibility(self.ListHeader_Button_loc.replace('%s', btnname))

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
        return elem.text
    
    def ListComponent_TableTd_Click( self ,row,col):
        '''点击表单元格值'''
        self.clickElemByXpath_visibility(self.listTable_td_loc.replace('%row',str(row)).replace('%col',str(col)))



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

















###############################栋一
    def openAppTitle(self):
        '''
        打开应用主页面
        :return:
        '''
        try:
            self.clickElemByXpath_visibility(self.app_home_loc)
        except Exception:
            element=self.waiteElemsByXpath(self.app_home_loc)
            self.js("arguments[0].click()",element)


    def openApp(self,app_name):
        '''
        通过应用名称打开应用
        :param app_name: 要打开的应用名称
        :return:
        '''
        starttime=time.time()
        spacing=0.1
        timeout=3
        endtime=starttime+timeout
        loc = self.app_name_loc.format(appname=app_name)
        while True:
            if time.time()<endtime:
                try:
                    self.clickElemByXpath_visibility(loc)
                    break
                except Exception:
                    time.sleep(spacing)
            elif time.time()>endtime:
                break

    def clickPage(self,name):
        '''
        通过菜单名称打开应用左侧菜单或者页面
        :param name:菜单名称或者页面名称
        :return:

        '''
        loc=self.left_meau_loc.format(pagename=name)
        self.clickElemByXpath_visibility(loc)



    def filterDataBySingleText(self,feild_name,value):
        '''通过单行文本组件筛选页面数据'''

        loc=self.search_data_loc.format(feildname=feild_name)
        self.sendkeysElemByXpath_visibility(loc,value)
        self.ListComponent_Click_SerachBtn()



    def filterDataByTextArea(self,feild_name,value):
        '''通过多行文本组件筛选页面数据'''
        loc=self.search_data_loc.format(feildname=feild_name)
        self.sendkeysElemByXpath_visibility(loc,value)
        self.ListComponent_Click_SerachBtn()


    def filterDataByDigital(self,feild_name,value):
        '''通过数字组件筛选页面数据'''

        loc=self.search_digital_loc.format(feildname=feild_name)
        self.sendkeysElemByXpath_visibility(loc,value)
        self.ListComponent_Click_SerachBtn()


    def filterDataBySelectionBox(self,feild_name,value):
        '''通过选择框组件筛选页面数据'''
        loc = self.search_choice_loc.format(feildname=feild_name)
        starttime=time.time()
        spacing=0.1
        timeout=3
        endtime=starttime+timeout
        while True:
            if time.time()<endtime:
                try:
                    self.clickElemByXpath_visibility(loc)
                    break
                except Exception:
                    time.sleep(spacing)
            elif time.time()>endtime:
                break
        li_list=self.findElemsByXpath(self.search_li_loc)
        for i in range(0,len(li_list)):
            if li_list[i].text == value:
                self.clickElemByXpath_visibility(self.li_selector_loc.format(indexnum=i+1))
                self.clickElemByXpath_visibility("xpath=>//label[@for='{feildname}']/span".format(feildname=feild_name))
                self.ListComponent_Click_SerachBtn()
                break
            else:
                print("输入值：{0} 不是选项值，请输入正确的选项值！！！".format(value))
                break


    def filterDataByPersonSelection(self,feild_name,name):
        '''通过人员选择筛选页面数据'''
        loc=self.search_choice_loc.format(feildname=feild_name)
        try:
            self.sendkeysElemByXpath_visibility(loc,name)
            self.clickElemByXpath_visibility("//div[@title='{name}' and @class='text_ellipsis']".format(name=name))
            self.ListComponent_Click_SerachBtn()
        except Exception:
            self.refreshCurrentPage()
            time.sleep(1)
            self.sendkeysElemByXpath_visibility(loc,name)
            self.clickElemByXpath_visibility("//div[@title='{name}' and @class='text_ellipsis']".format(name=name))
            self.ListComponent_Click_SerachBtn()


    def filterDataByDepartment(self,feild_name,departmentname):
        '''通过部门选择筛选页面数据'''
        loc=self.search_choice_loc.format(feildname=feild_name)
        try:
            self.sendkeysElemByXpath_visibility(loc,departmentname)
            self.clickElemByXpath_visibility("//div[@title='{name}']".format(name=departmentname))
            self.ListComponent_Click_SerachBtn()
        except Exception:
            self.refreshCurrentPage()
            self.sendkeysElemByXpath_visibility(loc,departmentname)
            self.clickElemByXpath_visibility("//div[@title='{name}']".format(name=departmentname))
            self.ListComponent_Click_SerachBtn()

    def filterDataByAddress(self, feild_name, address):
        '''通过地址选择筛选页面数据'''

        address=str(address)
        if "/" not in address:
            try:
                starttime = time.time()
                waitspacing = 0.1
                timeout = 5
                while True:
                    if time.time() < starttime + timeout:
                        try:
                            loc = self.search_address_loc.format(feildname=feild_name)
                            self.clickElemByXpath_visibility(loc)
                            break
                        except Exception:
                            time.sleep(waitspacing)
                    elif time.time() > starttime + timeout:
                        break
                try:
                    self.clickElemByXpath_visibility(self.address_option_loc.format(addressname=address))
                    self.ListComponent_Click_SerachBtn()
                except Exception:
                    time.sleep(1)
                    self.clickElemByXpath_visibility(self.address_option_loc.format(addressname=address))
                    self.ListComponent_Click_SerachBtn()
            except Exception:
                print("地址输入格式不正确或者地址不存在，请使用如下输入格式：河南省/郑州市/金水区")
        else:
            try:
                sp=address.split("/")
                if len(sp)==3:
                    starttime=time.time()
                    waitspacing=0.1
                    timeout=5
                    while True:
                        if time.time()<starttime+timeout:
                            try:
                                loc = self.search_address_loc.format(feildname=feild_name)
                                self.clickElemByXpath_visibility(loc)
                                break
                            except Exception:
                                time.sleep(waitspacing)
                        elif time.time()>starttime+timeout:
                            break
                    try:
                        self.clickElemByXpath_visibility(self.address_option_loc.format(addressname=sp[0]))
                        self.clickElemByXpath_visibility(self.address_option_loc.format(addressname=sp[1]))
                        self.clickElemByXpath_visibility(self.address_option_loc.format(addressname=sp[2]))
                        self.ListComponent_Click_SerachBtn()
                    except Exception:
                        time.sleep(1)
                        self.clickElemByXpath_visibility(self.address_option_loc.format(addressname=sp[0]))
                        self.clickElemByXpath_visibility(self.address_option_loc.format(addressname=sp[1]))
                        self.clickElemByXpath_visibility(self.address_option_loc.format(addressname=sp[2]))
                        self.ListComponent_Click_SerachBtn()
                elif len(sp)==2:
                    starttime=time.time()
                    waitspacing=0.1
                    timeout=5
                    while True:
                        if time.time()<starttime+timeout:
                            try:
                                loc = self.search_address_loc.format(feildname=feild_name)
                                self.clickElemByXpath_visibility(loc)
                                break
                            except Exception:
                                time.sleep(waitspacing)
                        elif time.time()>starttime+timeout:
                            break
                    try:
                        self.clickElemByXpath_visibility(self.address_option_loc.format(addressname=sp[0]))
                        self.clickElemByXpath_visibility(self.address_option_loc.format(addressname=sp[1]))
                        self.ListComponent_Click_SerachBtn()
                    except Exception:
                        time.sleep(1)
                        self.clickElemByXpath_visibility(self.address_option_loc.format(addressname=sp[0]))
                        self.clickElemByXpath_visibility(self.address_option_loc.format(addressname=sp[1]))
                        self.ListComponent_Click_SerachBtn()

            except Exception:
                print("输入的地址不存在，请检查！！！")


    def filterDataByCoding(self,feild_name,value):
        '''通过生成编码组件筛选页面数据'''

        loc=self.search_data_loc.format(feildname=feild_name)
        self.sendkeysElemByXpath_visibility(loc,value)
        self.ListComponent_Click_SerachBtn()

    def filterDataByScore(self,feild_name,value):
        '''通过评分组件筛选页面数据'''
        loc=self.search_base_loc.format(feildname=feild_name)
        try:
            self.clickElemByXpath_visibility(loc)
        except Exception:
            time.sleep(1)
            self.clickElemByXpath_visibility(loc)
        self.clickElemByXpath_visibility("//div[@title='{score}']".format(score=value))
        self.clickElemByXpath_visibility("//label[@for='{name}']".format(name=feild_name))
        self.ListComponent_Click_SerachBtn()


    def filterDataByCreater(self,value):
        '''通过创建人字段筛选页面数据'''
        loc=self.search_creator_loc
        starttime = time.time()
        waitspacing = 5
        timeout = 10
        while True:
            if time.time() < starttime + timeout:
                try:
                    self.clear(loc)
                    self.sendkeysElemByXpath_visibility(loc, value)
                    break
                except Exception:
                    time.sleep(waitspacing)
            elif time.time() > starttime + timeout:
                break
        try:
            self.clickElemByXpath_visibility("//div[@title='{name}']".format(name=value))
            self.ListComponent_Click_SerachBtn()
        except Exception:

            print("请检查输入的人员姓名，‘{value}’可能不存在".format(value=value))


    def filterDataByCreateDate(self,startdate,enddate):
        '''通过创建时间筛选页面数据'''
        if "-" not in startdate or "-" not in enddate:
            print("请检查日期时间输入格式，如：“2020-05-15”格式！！！")
        else:
            try:
                self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild="createDate"))
                self.sendkeysElemByXpath_visibility(self.search_startdate_loc.format(feild="createDate"),startdate)
                self.sendkeysElemByXpath_visibility(self.search_enddate_loc.format(feild="createDate"),enddate)
                self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild="createDate"))
                self.clickElemByXpath_visibility("//label[@for='createDate']")
                self.ListComponent_Click_SerachBtn()
            except Exception:
                time.sleep(1)
                self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild="createDate"))
                self.sendkeysElemByXpath_visibility(self.search_startdate_loc.format(feild="createDate"),startdate)
                self.sendkeysElemByXpath_visibility(self.search_enddate_loc.format(feild="createDate"),enddate)
                self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild="createDate"))
                self.clickElemByXpath_visibility("//label[@for='createDate']")
                self.ListComponent_Click_SerachBtn()

    def filterDataByModifyDate(self,startdate,enddate):
        '''通过修改时间筛选页面数据'''
        if "-" not in startdate or "-" not in enddate:
            print("请检查日期时间输入格式，如：“2020-05-15”格式！！！")
        else:
            try:
                self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild="last_modify_date"))
                self.sendkeysElemByXpath_visibility(self.search_startdate_loc.format(feild="last_modify_date"),startdate)
                self.sendkeysElemByXpath_visibility(self.search_enddate_loc.format(feild="last_modify_date"),enddate)
                self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild="last_modify_date"))
                self.clickElemByXpath_visibility("//label[@for='last_modify_date']")
                self.ListComponent_Click_SerachBtn()
            except Exception:
                time.sleep(1)
                self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild="last_modify_date"))
                self.sendkeysElemByXpath_visibility(self.search_startdate_loc.format(feild="last_modify_date"),startdate)
                self.sendkeysElemByXpath_visibility(self.search_enddate_loc.format(feild="last_modify_date"),enddate)
                self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild="last_modify_date"))
                self.clickElemByXpath_visibility("//label[@for='last_modify_date']")
                self.ListComponent_Click_SerachBtn()


    def filterDataByDate(self,feild_name,startdate,enddate):
        '''通过日期组件筛选页面数据'''
        if "-" not in startdate or "-" not in enddate:
            print("请检查日期时间输入格式，如：“2020-05-15”格式！！！")
        else:

            try:
                self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name))
                self.sendkeysElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name),startdate)
                self.sendkeysElemByXpath_visibility(self.search_enddate_loc.format(feild=feild_name),enddate)
                self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name))
                self.clickElemByXpath_visibility("//label[@for='{0}']".format(feild_name))
                self.ListComponent_Click_SerachBtn()
            except Exception:
                time.sleep(1)
                self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name))
                self.sendkeysElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name),startdate)
                self.sendkeysElemByXpath_visibility(self.search_enddate_loc.format(feild=feild_name),enddate)
                self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name))
                self.clickElemByXpath_visibility("//label[@for='{0}']".format(feild_name))
                self.ListComponent_Click_SerachBtn()


    def filterDataByTime(self,feild_name,starttime,endtime):
        '''通过时间组件筛选页面数据'''

        try:
            self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name))
            self.sendkeysElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name),starttime)
            self.sendkeysElemByXpath_visibility(self.search_enddate_loc.format(feild=feild_name),endtime)
            self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name))
            self.clickElemByXpath_visibility("//label[@for='{0}']".format(feild_name))
            self.ListComponent_Click_SerachBtn()
        except Exception:
            time.sleep(1)
            self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name))
            self.sendkeysElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name),starttime)
            self.sendkeysElemByXpath_visibility(self.search_enddate_loc.format(feild=feild_name),endtime)
            self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name))
            self.clickElemByXpath_visibility("//label[@for='{0}']".format(feild_name))
            self.ListComponent_Click_SerachBtn()


    def filterDataByDateAndTime(self,feild_name,starttime,endtime):
        '''通过日期时间组件筛选页面数据'''

        try:
            self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name))
            self.sendkeysElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name),starttime)
            self.sendkeysElemByXpath_visibility(self.search_enddate_loc.format(feild=feild_name),endtime)
            self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name))
            self.clickElemByXpath_visibility("//label[@for='{0}']".format(feild_name))
            self.ListComponent_Click_SerachBtn()
        except Exception:
            time.sleep(1)
            self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name))
            self.sendkeysElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name),starttime)
            self.sendkeysElemByXpath_visibility(self.search_enddate_loc.format(feild=feild_name),endtime)
            self.clickElemByXpath_visibility(self.search_startdate_loc.format(feild=feild_name))
            self.clickElemByXpath_visibility("//label[@for='{0}']".format(feild_name))
            self.ListComponent_Click_SerachBtn()





    def inputValueToSingleText(self,feild_name,value):
        '''向单行文本字段输入值'''
        loc=self.input_base_loc.format(feildname=feild_name)
        self.sendkeysElemByXpath_visibility(loc,value)

    def inputValueToTextArea(self,feild_name,value):
        '''向多行文本字段输入值'''
        loc=self.input_textarea_loc.format(feildname=feild_name)
        self.sendkeysElemByXpath_visibility(loc,value)


    def inputValueToDigital(self,feild_name,value):
        '''向数字组件输入值'''
        loc=self.input_base_loc.format(feildname=feild_name)
        self.sendkeysElemByXpath_visibility(loc,value)


    def inputValueToSeletion(self,feild_name,value):
        '''输入单项选择框值'''
        loc = self.input_base_loc.format(feildname=feild_name)
        self.clickElemByXpath_visibility(loc)
        self.clickElemByXpath_visibility("//span[text()='{0}']".format(value))

    def inputValueToSeletions(self,feild_name,value):
        '''输入多项选择框值'''
        loc = self.input_base_loc.format(feildname=feild_name)
        self.clickElemByXpath_visibility(loc)
        self.clickElemByXpath_visibility("//div[@title='{0}']".format(value))
        self.clickElemByXpath_visibility("//form[@class='el-form el-form--label-right']//label[@for='{0}']".format(feild_name))


    def inputValueToDate(self,feild_name,value):
        '''输入日期'''
        loc = self.input_base_loc.format(feildname=feild_name)
        self.clickElemByXpath_visibility(loc)
        self.sendkeysElemByXpath_visibility(loc,value)
        self.clickElemByXpath_visibility("//form[@class='el-form el-form--label-right']//label[@for='{0}']".format(feild_name))


    def inputValueToTime(self,feild_name,value):
        '''输入时间'''
        loc = self.input_base_loc.format(feildname=feild_name)
        self.sendkeysElemByXpath_visibility(loc,value)
        self.clickElemByXpath_visibility("//form[@class='el-form el-form--label-right']//label[@for='{0}']".format(feild_name))

    def inputValueToDateAndTime(self,feild_name,date,time):
        '''输入日期时间'''
        self.sendkeysElemByXpath_visibility(self.input_datetime_loc.format(feildname=feild_name),date)
        self.sendkeysElemByXpath_visibility(self.input_datetime_loc2.format(feildname=feild_name),time)
        self.clickElemByXpath_visibility("//form[@class='el-form el-form--label-right']//label[@for='{0}']".format(feild_name))


    def clickSubmitBtn(self):
        '''点击提交按钮'''
        self.clickElemByXpath_visibility("//span[contains(text(),'提交')]")


    def getFeildValues(self):
        '''
        通过人员选择字段名称，获取对应字段的所有字段值
        :param field_name:获取字段的名称
        :return:返回字段值的列表
        # '''
        loc = "//div[@class='el-table__body-wrapper is-scrolling-left']"
        self.addAttributeElemsByXpath_Presence(loc, "id", "scroll")
        feild_name=[]
        feild_value=[]
        element_lis=self.findElemsByXpath("//th[starts-with(@class,'el-table') and not(contains(@class,'is-hidden'))]")
        for i in range(0,len(element_lis)-3):
            value=self.waiteElemsByXpath("//th[starts-with(@class,'el-table') and not(contains(@class,'is-hidden'))][{num}]/div/span[not(contains(@class,'operation'))]".format(num=i+1)).text
            feild_name.append(value)
            element = self.waiteElemsByXpath("//div[@id='scroll']")
            self.js("arguments[0].scrollBy(80,0)", element)
        element2 = self.waiteElemsByXpath("//div[@id='scroll']")
        self.js("arguments[0].scrollBy(-1000,0)", element2)
        value_list=self.findElemsByXpath("//div[@id='scroll']//tr[@class='el-table__row row_click_disabled' or @class='el-table__row  row_click_disabled']")
        print(len(value_list))
        for j in range(0,len(value_list)):
            for k in range(0,6):
                loc="//div[@id='scroll']//tr[@class='el-table__row row_click_disabled' or @class='el-table__row  row_click_disabled'][{row_num}]/td[not(contains(@class,'is-hidden'))][{crow_num}]//span".format(row_num=j+1,crow_num=k+1)
                print(loc)
                value1=self.waiteElemsByXpath(loc).text
                feild_value.append(value1)
                print(feild_value)
                element = self.waiteElemsByXpath("//div[@id='scroll']")
                self.js("arguments[0].scrollBy(80,0)", element)
            element1 = self.waiteElemsByXpath("//div[@id='scroll']")
            self.js("arguments[0].scrollBy(-1000,0)", element1)



