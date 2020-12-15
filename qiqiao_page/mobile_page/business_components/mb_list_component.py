# coding=utf-8
import time

from public.selenium_page import SeleniumPage
from qiqiao_page.mobile_page.form_components.mb_user_component import MbUser
from qiqiao_page.mobile_page.mb_public_page import MbPublicPage


class MbListComponent(MbPublicPage):



    # 列表记录元素
    CardList_loc = "div.dyCardList div.dyCardList_text_wrapper"

    # 列表按钮
    CardListButton_loc = "div.cube-action-sheet-content li"

    # 列表底部按钮
    CardListBottomButton_loc = "div.cube-action-sheet-panel div:last-child"

    CardList_tabItem = "div.dyCardList div.dyCardList_tabItem"

    CardList_tabItem_div_loc = "//div[@class='dyCardList_tabItem' and contains(text(),'%s')]"

    add_btn = "//div[@class='add_btn']"
    dyCardList_item = "//div[starts-with(@class,'dyCardList_item')]"
    lastPage_div = "//div[@class='myScroll_loadText' and contains(text(),'已经是最后一页了')]"
    dyCardList_status =  "//div[starts-with(@class,'dyCardList_item')]//div[@class='dyCardList_status']"
    dyCardList_text_main = "//div[@class='dyCardList_item']//h2[@class='dyCardList_text_main']"
    dyCardList_text_content = "//div[@class='myScroll_container']/div[@index='%r']//p"
    shaixuanIcoon = "//i[@class='icon iconfont icon-huaban16']"
    searchBar_i = "//div[@class='searchBar_search_input']//i"
    searchBar_input = "//div[@class='searchBar_search_input']//input"

    fieldSelect_i = "//div[@class='searchBar_search_fieldSelect']//i"

    fieldSelect_Item = "//div[contains(@class,'searchBar_leftDrawer_item') and contains(text(),'%s')]"

    item_p_loc = "//div[starts-with(@class,'dyCardList_item')][%s]//p[%n]"

    userSelect_Filter_addIcon_loc = "//h3[text()='%s']/following-sibling::ul/li[@class='icon_add_new']"

    filter_button_loc = "//div[@class='filter_render_operation']//button[text()=' %s']"

    CubeActionBottomButton = "//li[@title='%s']"

    CubeActionBottomCancelButton = "//div[@class='cube-action-sheet-cancel']"
    Cube_dialog_Button = "//a[text()='%s']"
    dyCardList_right_dot_loc = "//div[@index='%s']//div[@class='dyCardList_right_dot']/i"
    MbListComponent_dialog_button = "//a[text()='%s']"

    def MbListComponent_Click_dialogButton( self,buttonName ):
        '''点击列表弹框按钮'''
        self.clickElemByXpath_visibility(self.MbListComponent_dialog_button.replace('%s',buttonName))

    def MbListComponent_Click_CardListBottomButton( self,buttonName ):
        '''点击底部按钮'''
        if(buttonName=="取消"):
            self.clickElemByXpath_visibility(self.CubeActionBottomCancelButton)
        else:
            self.clickElemByXpath_visibility(self.CubeActionBottomButton.replace('%s',buttonName))

    def MbListComponent_Click_Cube_dialog_Button(  self,buttonName  ):
        '''列表弹框按钮'''
        self.clickElemByXpath_visibility(self.Cube_dialog_Button.replace('%s',buttonName))


    def MbListComponent_FilterButton_Click( self,buttonName ):
        '''点击列表筛选确定重置按钮'''
        self.clickElemByXpath_visibility(self.filter_button_loc.replace('%s',buttonName))

    def MbListComponent_ItemP_Get( self,row,now ):
        '''获取列表记录行显示值'''
        return self.find_elemByXPATH_visibility(self.item_p_loc.replace('%s',str(row)).replace('%n',str(now))).text

    def MbListComponent_shaixuanIcoon_Click( self ):
        '''点击列表筛选图标'''
        self.clickElemByXpath_visibility(self.shaixuanIcoon)

    def MbListComponent_searchInput_Sendkeys( self,key ):
        '''点击列表搜索框输入值'''
        self.clickElemByXpath_visibility(self.searchBar_i)
        self.sendkeysElemByXpath_visibility(self.searchBar_input,key)

    def MbListComponent_searchItem_Switch( self,Item ):
        '''点击列表切换搜索项'''
        self.clickElemByXpath_visibility(self.fieldSelect_i)
        time.sleep(1)
        self.clickElemByXpath_visibility(self.fieldSelect_Item.replace("%s",Item))


    def MbListComponent_AddButton_Click( self ):
        '''点击列表添加按钮'''
        self.clickElemByXpath_visibility(self.add_btn)

    # 长按列表某条记录
    def MbListComponent_Recore_ClickAndHole( self, index ,*args):
        '''长按列表某条记录'''
        elem = self.find_elemsByCSS_presence(self.CardList_loc)[index-1]
        self.click_and_hold(elem)

    def MbListComponent_click_moreButton(self, index, *args):
        '''点击列表更多按钮图标'''
        self.clickElemByXpath_visibility(self.dyCardList_right_dot_loc.replace('%s',str(index - 1)))



    #点击列表某条记录
    def MbListComponent_Recore_Click( self, index ,*args):
        '''点击列表某条记录'''
        elem = self.find_elemsByCSS_presence(self.CardList_loc)[index-1]
        self.clickElem(elem)



    def MbListComponent_GetRecoreButton( self ):
        '''获取列表底部按钮'''
        buttonList = []
        cardListButtons = self.find_elemsByCSS_presence(self.CardListButton_loc)
        for cardListButton in cardListButtons:
            buttonList.append(cardListButton.get_attribute("title"))
        buttonList.append(self.find_elenmInElemsByCSS_visibility_of_any_elements_located(self.CardListBottomButton_loc).get_attribute("title"))
        return buttonList



    def MbListComponent_GetListAllTab( self ):
        '''获取列表选项卡所有选项'''
        tabItems = []
        tabItemsElem = self.find_elemsByCSS_presence(self.CardList_tabItem)
        for tabItemElem in tabItemsElem:
            tabItems.append(tabItemElem.text)
        return tabItems

    def MbListComponent_SwitchTab( self,itemName):
        '''切换到具体选项卡'''
        self.clickElemByXpath_visibility(self.CardList_tabItem_div_loc.replace('%s',itemName))


    def MbListComponent_Get_RecoresNumber( self ):
        '''返回当前列表记录数'''
        elems =self.find_elemsByXPATH_presence(self.dyCardList_item,timeout=3)
        if(elems!=None):
            return len(elems)
        else:
            return 0

    def MbListComponent_Scroll_To_Bottom( self ):
        '''滚动到列表底部'''
        while(self.find_elemByXPATH_visibility(self.lastPage_div,timeout=2)==None):
            elem = self.find_elemsByCSS_visibility(self.CardList_loc)[-1]
            self.h5_scroll(elem,0,1000)



    def MbListComponent_Get_RecoreStatusValule( self,index):
        '''返回当前列表记录状态值'''
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.dyCardList_status,index=index-1)
        if (elem!=None):
            return elem.text
        else:
            return None





    def MbListComponent_Get_RecoreTitleValule( self,index ):
        '''返回当前列表记录标题值'''
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.dyCardList_text_main,index=index-1)
        if (elem!=None):
            return elem.text
        else:
            return None


    def MbListComponent_Get_RecoreTextContents( self,r ):
        '''返回当前列表记录标题值'''
        list = []
        elems = self.find_elemsByXPATH_visibility(self.dyCardList_text_content.replace("%r",str(r-1)))
        if (elems!=None):
            for elem in elems:
                list.append(elem.text)
            return list
        else:
            return None


    def MbListComponent_QueryItem_Sendkeys( self, itemName, keys, *args,QueryItemType="text"):
        '''列表组件的查询项输入值
        :type QueryItemType: object
        itemName ：查询项字段
        keys: 查询项值
        QueryItemType ： 查询项类型
        '''
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
            #点击添加按钮
            self.clickElemByXpath_visibility(self.userSelect_Filter_addIcon_loc.replace('%s',itemName))
            #选择人员
            MbUser(self.driver).MbUser_SelectUser(keys)
        else:
            print("类型值为：" + type)
            raise Exception("查询项无此类型，请检查type参数的值")