# coding=utf-8
from public.selenium_page import SeleniumPage


class MbListComponent(SeleniumPage):



    # 列表记录元素
    CardList_loc = "div.dyCardList div.dyCardList_text_wrapper"

    # 列表按钮
    CardListButton_loc = "div.cube-action-sheet-content li"
    # 列表底部按钮
    CardListBottomButton_loc = "div.cube-action-sheet-panel div:last-child"

    CardList_tabItem = "div.dyCardList div.dyCardList_tabItem"

    add_btn = "//div[@class='add_btn']"
    dyCardList_item = "//div[@class='dyCardList_item']"
    dyCardList_status =  "//div[@class='dyCardList_item']//div[@class='dyCardList_status']"
    dyCardList_text_main = "//div[@class='dyCardList_item']//h2[@class='dyCardList_text_main']"
    dyCardList_text_content = "//div[@class='cube-swipe']/div[%r]//p"
    shaixuanIcoon = "//i[@class='icon iconfont icon-huaban16']"
    searchBar_i = "//div[@class='searchBar_search_input']//i"
    searchBar_input = "//div[@class='searchBar_search_input']//input"

    fieldSelect_i = "//div[@class='searchBar_search_fieldSelect']//i"

    fieldSelect_Item = "//div[contains(@class,'searchBar_leftDrawer_item') and contains(text(),'%s')]"

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
        self.clickElemByXpath_visibility(self.fieldSelect_Item,Item)


    def MbListComponent_AddButton_Click( self ):
        '''点击列表添加按钮'''
        self.clickElemByXpath_visibility(self.add_btn)

    # 长按列表某条记录
    def MbListComponent_Recore_ClickAndHole( self, index ,*args):
        elem = self.find_elemsByCSS(self.CardList_loc)[index]
        self.click_and_hold(elem)

    #点击列表某条记录
    def MbListComponent_Recore_Click( self, index ,*args):
        elem = self.find_elemsByCSS(self.CardList_loc)[index]
        self.clickElem(elem)


    # 判断列表记录是否有某按钮操作权限
    def MbListComponent_GetRecoreButton( self ):
        buttonList = []
        cardListButtons = self.find_elemsByCSS(self.CardListButton_loc)
        for cardListButton in cardListButtons:
            buttonList.append(cardListButton.get_attribute("title"))
        buttonList.append(self.find_elenmInElemsByCSS_visibility_of_any_elements_located(self.CardListBottomButton_loc).get_attribute("title"))
        return buttonList

    #获取列表选项卡所有选项
    def MbListComponent_GetListAllTab( self ):
        tabItems = []
        tabItemsElem = self.find_elemsByCSS(self.CardList_tabItem)
        for tabItemElem in tabItemsElem:
            tabItems.append(tabItemElem.text)
        return tabItems


    def MbListComponent_Get_RecoresNumber( self ):
        '''返回当前列表记录数'''
        return len(self.find_elemsByXPATH_presence(self.dyCardList_item))


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
        elems = self.find_elemsByXPATH_visibility(self.dyCardList_text_content.replace("%r",str(r)))
        if (elems!=None):
            for elem in elems:
                list.append(elem.text)
            return list
        else:
            return None