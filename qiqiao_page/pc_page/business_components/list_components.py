
import time
from public.selenium_page import SeleniumPage

class List(SeleniumPage):

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
    address_base_loc = "//span[text()='{addressname}']"

    search_creator_loc = "//label[@for='author_name']/following-sibling::div/div/div/div/input"
    search_startdate_loc = "//label[@for='{feild}']/following-sibling::div/div/div/input[1]"
    search_enddate_loc = "//label[@for='{feild}']/following-sibling::div/div/div/input[2]"

    btn_base_loc = "//div[@class='view_toolbar_panel']/div"
    btn_name_loc = "//div[@class='view_toolbar_panel']/div[{indexnum}]/button/span"

    search_btn_loc = "//button[@class='el-button search_btn el-button--primary']"
    reset_btn_loc = "//button[@class='el-button reset_btn el-button--default']"

    input_base_loc = "//form[@class='el-form el-form--label-right']//label[@for='{feildname}']/following-sibling::div//input"
    input_textarea_loc = "//form[@class='el-form el-form--label-right']//label[@for='{feildname}']/following-sibling::div//textarea"
    input_datetime_loc = "//form[@class='el-form el-form--label-right']//label[@for='{feildname}']/following-sibling::div/div/div[1]/input"
    input_datetime_loc2 = "//form[@class='el-form el-form--label-right']//label[@for='{feildname}']/following-sibling::div/div/div[2]/div/input"





    def openAppTitle(self):
        '''
        打开应用主页面
        :return:
        '''
        try:
            self.clickElemByXpath_Presence(self.app_home_loc)
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
                    self.clickElemByXpath_Presence(loc)
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
        self.clickElemByXpath_Presence(loc)



    def filterDataBySingleText(self,feild_name,value):
        '''通过单行文本组件筛选页面数据'''

        loc=self.search_data_loc.format(feildname=feild_name)
        self.sendkeysElemByXpath_Presence(loc,value)
        self.clickSerachBtn()



    def filterDataByTextArea(self,feild_name,value):
        '''通过多行文本组件筛选页面数据'''
        loc=self.search_data_loc.format(feildname=feild_name)
        self.sendkeysElemByXpath_Presence(loc,value)
        self.clickSerachBtn()


    def filterDataByDigital(self,feild_name,value):
        '''通过数字组件筛选页面数据'''

        loc=self.search_digital_loc.format(feildname=feild_name)
        self.sendkeysElemByXpath_Presence(loc,value)
        self.clickSerachBtn()


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
                    self.clickElemByXpath_Presence(loc)
                    break
                except Exception:
                    time.sleep(spacing)
            elif time.time()>endtime:
                break
        li_list=self.findElemsByXpath(self.search_li_loc)
        for i in range(0,len(li_list)):
            if li_list[i].text == value:
                self.clickElemByXpath_Presence(self.li_selector_loc.format(indexnum=i+1))
                self.clickElemByXpath_Presence("xpath=>//label[@for='{feildname}']/span".format(feildname=feild_name))
                self.clickSerachBtn()
                break
            else:
                print("输入值：{0} 不是选项值，请输入正确的选项值！！！".format(value))
                break


    def filterDataByPersonSelection(self,feild_name,name):
        '''通过人员选择筛选页面数据'''
        loc=self.search_choice_loc.format(feildname=feild_name)
        try:
            self.sendkeysElemByXpath_Presence(loc,name)
            self.clickElemByXpath_Presence("//div[@title='{name}' and @class='text_ellipsis']".format(name=name))
            self.clickSerachBtn()
        except Exception:
            self.refreshCurrentPage()
            time.sleep(1)
            self.sendkeysElemByXpath_Presence(loc,name)
            self.clickElemByXpath_Presence("//div[@title='{name}' and @class='text_ellipsis']".format(name=name))
            self.clickSerachBtn()


    def filterDataByDepartment(self,feild_name,departmentname):
        '''通过部门选择筛选页面数据'''
        loc=self.search_choice_loc.format(feildname=feild_name)
        try:
            self.sendkeysElemByXpath_Presence(loc,departmentname)
            self.clickElemByXpath_Presence("//div[@title='{name}']".format(name=departmentname))
            self.clickSerachBtn()
        except Exception:
            self.refreshCurrentPage()
            self.sendkeysElemByXpath_Presence(loc,departmentname)
            self.clickElemByXpath_Presence("//div[@title='{name}']".format(name=departmentname))
            self.clickSerachBtn()

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
                            self.clickElemByXpath_Presence(loc)
                            break
                        except Exception:
                            time.sleep(waitspacing)
                    elif time.time() > starttime + timeout:
                        break
                try:
                    self.clickElemByXpath_Presence(self.address_base_loc.format(addressname=address))
                    self.clickSerachBtn()
                except Exception:
                    time.sleep(1)
                    self.clickElemByXpath_Presence(self.address_base_loc.format(addressname=address))
                    self.clickSerachBtn()
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
                                self.clickElemByXpath_Presence(loc)
                                break
                            except Exception:
                                time.sleep(waitspacing)
                        elif time.time()>starttime+timeout:
                            break
                    try:
                        self.clickElemByXpath_Presence(self.address_base_loc.format(addressname=sp[0]))
                        self.clickElemByXpath_Presence(self.address_base_loc.format(addressname=sp[1]))
                        self.clickElemByXpath_Presence(self.address_base_loc.format(addressname=sp[2]))
                        self.clickSerachBtn()
                    except Exception:
                        time.sleep(1)
                        self.clickElemByXpath_Presence(self.address_base_loc.format(addressname=sp[0]))
                        self.clickElemByXpath_Presence(self.address_base_loc.format(addressname=sp[1]))
                        self.clickElemByXpath_Presence(self.address_base_loc.format(addressname=sp[2]))
                        self.clickSerachBtn()
                elif len(sp)==2:
                    starttime=time.time()
                    waitspacing=0.1
                    timeout=5
                    while True:
                        if time.time()<starttime+timeout:
                            try:
                                loc = self.search_address_loc.format(feildname=feild_name)
                                self.clickElemByXpath_Presence(loc)
                                break
                            except Exception:
                                time.sleep(waitspacing)
                        elif time.time()>starttime+timeout:
                            break
                    try:
                        self.clickElemByXpath_Presence(self.address_base_loc.format(addressname=sp[0]))
                        self.clickElemByXpath_Presence(self.address_base_loc.format(addressname=sp[1]))
                        self.clickSerachBtn()
                    except Exception:
                        time.sleep(1)
                        self.clickElemByXpath_Presence(self.address_base_loc.format(addressname=sp[0]))
                        self.clickElemByXpath_Presence(self.address_base_loc.format(addressname=sp[1]))
                        self.clickSerachBtn()

            except Exception:
                print("输入的地址不存在，请检查！！！")


    def filterDataByCoding(self,feild_name,value):
        '''通过生成编码组件筛选页面数据'''

        loc=self.search_data_loc.format(feildname=feild_name)
        self.sendkeysElemByXpath_Presence(loc,value)
        self.clickSerachBtn()

    def filterDataByScore(self,feild_name,value):
        '''通过评分组件筛选页面数据'''
        loc=self.search_base_loc.format(feildname=feild_name)
        try:
            self.clickElemByXpath_Presence(loc)
        except Exception:
            time.sleep(1)
            self.clickElemByXpath_Presence(loc)
        self.clickElemByXpath_Presence("//div[@title='{score}']".format(score=value))
        self.clickElemByXpath_Presence("//label[@for='{name}']".format(name=feild_name))
        self.clickSerachBtn()


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
                    self.sendkeysElemByXpath_Presence(loc, value)
                    break
                except Exception:
                    time.sleep(waitspacing)
            elif time.time() > starttime + timeout:
                break
        try:
            self.clickElemByXpath_Presence("//div[@title='{name}']".format(name=value))
            self.clickSerachBtn()
        except Exception:

            print("请检查输入的人员姓名，‘{value}’可能不存在".format(value=value))


    def filterDataByCreateDate(self,startdate,enddate):
        '''通过创建时间筛选页面数据'''
        if "-" not in startdate or "-" not in enddate:
            print("请检查日期时间输入格式，如：“2020-05-15”格式！！！")
        else:
            try:
                self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild="createDate"))
                self.sendkeysElemByXpath_Presence(self.search_startdate_loc.format(feild="createDate"),startdate)
                self.sendkeysElemByXpath_Presence(self.search_enddate_loc.format(feild="createDate"),enddate)
                self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild="createDate"))
                self.clickElemByXpath_Presence("//label[@for='createDate']")
                self.clickSerachBtn()
            except Exception:
                time.sleep(1)
                self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild="createDate"))
                self.sendkeysElemByXpath_Presence(self.search_startdate_loc.format(feild="createDate"),startdate)
                self.sendkeysElemByXpath_Presence(self.search_enddate_loc.format(feild="createDate"),enddate)
                self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild="createDate"))
                self.clickElemByXpath_Presence("//label[@for='createDate']")
                self.clickSerachBtn()

    def filterDataByModifyDate(self,startdate,enddate):
        '''通过修改时间筛选页面数据'''
        if "-" not in startdate or "-" not in enddate:
            print("请检查日期时间输入格式，如：“2020-05-15”格式！！！")
        else:
            try:
                self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild="last_modify_date"))
                self.sendkeysElemByXpath_Presence(self.search_startdate_loc.format(feild="last_modify_date"),startdate)
                self.sendkeysElemByXpath_Presence(self.search_enddate_loc.format(feild="last_modify_date"),enddate)
                self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild="last_modify_date"))
                self.clickElemByXpath_Presence("//label[@for='last_modify_date']")
                self.clickSerachBtn()
            except Exception:
                time.sleep(1)
                self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild="last_modify_date"))
                self.sendkeysElemByXpath_Presence(self.search_startdate_loc.format(feild="last_modify_date"),startdate)
                self.sendkeysElemByXpath_Presence(self.search_enddate_loc.format(feild="last_modify_date"),enddate)
                self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild="last_modify_date"))
                self.clickElemByXpath_Presence("//label[@for='last_modify_date']")
                self.clickSerachBtn()


    def filterDataByDate(self,feild_name,startdate,enddate):
        '''通过日期组件筛选页面数据'''
        if "-" not in startdate or "-" not in enddate:
            print("请检查日期时间输入格式，如：“2020-05-15”格式！！！")
        else:

            try:
                self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name))
                self.sendkeysElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name),startdate)
                self.sendkeysElemByXpath_Presence(self.search_enddate_loc.format(feild=feild_name),enddate)
                self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name))
                self.clickElemByXpath_Presence("//label[@for='{0}']".format(feild_name))
                self.clickSerachBtn()
            except Exception:
                time.sleep(1)
                self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name))
                self.sendkeysElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name),startdate)
                self.sendkeysElemByXpath_Presence(self.search_enddate_loc.format(feild=feild_name),enddate)
                self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name))
                self.clickElemByXpath_Presence("//label[@for='{0}']".format(feild_name))
                self.clickSerachBtn()


    def filterDataByTime(self,feild_name,starttime,endtime):
        '''通过时间组件筛选页面数据'''

        try:
            self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name))
            self.sendkeysElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name),starttime)
            self.sendkeysElemByXpath_Presence(self.search_enddate_loc.format(feild=feild_name),endtime)
            self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name))
            self.clickElemByXpath_Presence("//label[@for='{0}']".format(feild_name))
            self.clickSerachBtn()
        except Exception:
            time.sleep(1)
            self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name))
            self.sendkeysElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name),starttime)
            self.sendkeysElemByXpath_Presence(self.search_enddate_loc.format(feild=feild_name),endtime)
            self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name))
            self.clickElemByXpath_Presence("//label[@for='{0}']".format(feild_name))
            self.clickSerachBtn()


    def filterDataByDateAndTime(self,feild_name,starttime,endtime):
        '''通过日期时间组件筛选页面数据'''

        try:
            self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name))
            self.sendkeysElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name),starttime)
            self.sendkeysElemByXpath_Presence(self.search_enddate_loc.format(feild=feild_name),endtime)
            self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name))
            self.clickElemByXpath_Presence("//label[@for='{0}']".format(feild_name))
            self.clickSerachBtn()
        except Exception:
            time.sleep(1)
            self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name))
            self.sendkeysElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name),starttime)
            self.sendkeysElemByXpath_Presence(self.search_enddate_loc.format(feild=feild_name),endtime)
            self.clickElemByXpath_Presence(self.search_startdate_loc.format(feild=feild_name))
            self.clickElemByXpath_Presence("//label[@for='{0}']".format(feild_name))
            self.clickSerachBtn()


    def clickHeaderBtn(self,btnname):
        '''点击页面头部按钮'''
        btn_list=self.findElemsByXpath(self.btn_base_loc)
        for i in range(0,len(btn_list)):
            btn_name=self.getText(self.btn_name_loc.format(indexnum=i+1))
            if btn_name==btnname:
                try:
                    self.clickElemByXpath_Presence(self.btn_name_loc.format(indexnum=i+1))
                    break
                except Exception:
                    time.sleep(1)
                    self.clickElemByXpath_Presence(self.btn_name_loc.format(indexnum=i+1))
                    break
            else:
                continue

    def clickSerachBtn(self):
        '''点击筛选数据的搜索按钮'''
        self.clickElemByXpath_Presence(self.search_btn_loc)


    def clickResetBtn(self):
        '''点击筛选数据的重置按钮'''
        self.clickElemByXpath_Presence(self.reset_btn_loc)


    def inputValueToSingleText(self,feild_name,value):
        '''向单行文本字段输入值'''
        loc=self.input_base_loc.format(feildname=feild_name)
        self.sendkeysElemByXpath_Presence(loc,value)

    def inputValueToTextArea(self,feild_name,value):
        '''向多行文本字段输入值'''
        loc=self.input_textarea_loc.format(feildname=feild_name)
        self.sendkeysElemByXpath_Presence(loc,value)


    def inputValueToDigital(self,feild_name,value):
        '''向数字组件输入值'''
        loc=self.input_base_loc.format(feildname=feild_name)
        self.sendkeysElemByXpath_Presence(loc,value)


    def inputValueToSeletion(self,feild_name,value):
        '''输入单项选择框值'''
        loc = self.input_base_loc.format(feildname=feild_name)
        self.clickElemByXpath_Presence(loc)
        self.clickElemByXpath_Presence("//span[text()='{0}']".format(value))

    def inputValueToSeletions(self,feild_name,value):
        '''输入多项选择框值'''
        loc = self.input_base_loc.format(feildname=feild_name)
        self.clickElemByXpath_Presence(loc)
        self.clickElemByXpath_Presence("//div[@title='{0}']".format(value))
        self.clickElemByXpath_Presence("//form[@class='el-form el-form--label-right']//label[@for='{0}']".format(feild_name))


    def inputValueToDate(self,feild_name,value):
        '''输入日期'''
        loc = self.input_base_loc.format(feildname=feild_name)
        self.clickElemByXpath_Presence(loc)
        self.sendkeysElemByXpath_Presence(loc,value)
        self.clickElemByXpath_Presence("//form[@class='el-form el-form--label-right']//label[@for='{0}']".format(feild_name))


    def inputValueToTime(self,feild_name,value):
        '''输入时间'''
        loc = self.input_base_loc.format(feildname=feild_name)
        self.sendkeysElemByXpath_Presence(loc,value)
        self.clickElemByXpath_Presence("//form[@class='el-form el-form--label-right']//label[@for='{0}']".format(feild_name))

    def inputValueToDateAndTime(self,feild_name,date,time):
        '''输入日期时间'''
        self.sendkeysElemByXpath_Presence(self.input_datetime_loc.format(feildname=feild_name),date)
        self.sendkeysElemByXpath_Presence(self.input_datetime_loc2.format(feildname=feild_name),time)
        self.clickElemByXpath_Presence("//form[@class='el-form el-form--label-right']//label[@for='{0}']".format(feild_name))


    def clickSubmitBtn(self):
        '''点击提交按钮'''
        self.clickElemByXpath_Presence("//span[contains(text(),'提交')]")


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






        # for i in range(1,len(element_lis)+1):
        #     #fc_loc = "//thead[@class='has-gutter']/tr/th[{num}]/div/span".format(num=i + 3)
        #     fc_loc="//thead[@class='has-gutter']/tr/th[not(contains(@class,'is-hidden'))][{num}]/div/span".format(num=i)
        #     text_value = self.waiteElemsByXpath(fc_loc).text
        #     loc2 = "//div[@id='scroll']"
        #     element = self.waiteElemsByXpath(loc2)
        #
        #     if text_value==field_name:
        #         index_num=i
        #         break
        #     else:
        #         self.js("arguments[0].scrollBy(80,0)", element)
        #         continue
        # lis=[]
        # total_data = self.waiteElemsByXpath("//span[@class='el-pagination__total']").text
        # total_data=str(total_data)
        # total_value=total_data.split(" ")
        # value = total_value[1]
        # tr_base_loc="//tr[@class='el-table__row row_click_disabled']/td[not(contains(@class,'is-hidden'))][{index_num}]/div/a/span"
        # for j in range(1,int(value)+1):
        #     value_loc = tr_base_loc.format(index_num=j)
        #     result = self.waiteElemsByXpath(value_loc).text
        #     lis.append(result)
        # return lis