# coding=utf-8
from public.selenium_page import SeleniumPage


class ListComponent(SeleniumPage):
    # 列表记录元素
    CardList_loc = "div.dyCardList div.dyCardList_text_wrapper"

    # 列表按钮
    CardListButton_loc = "div.cube-action-sheet-content li"
    # 列表底部按钮
    CardListBottomButton_loc = "div.cube-action-sheet-panel div:last-child"

    CardList_tabItem = "div.dyCardList div.dyCardList_tabItem"


    # 长按列表某条记录
    def ClickAndHoleRecore( self, index ,*args):
        elem = self.find_elemsByCSS(self.CardList_loc)[index]
        self.click_and_hold(elem)

    # 判断列表记录是否有某按钮操作权限
    def GetRecoreButton( self ):
        buttonList = []
        cardListButtons = self.find_elemsByCSS(self.CardListButton_loc)
        for cardListButton in cardListButtons:
            buttonList.append(cardListButton.get_attribute("title"))
        buttonList.append(self.find_elemByCSS(self.CardListBottomButton_loc).get_attribute("title"))
        return buttonList

    #获取列表选项卡所有选项
    def GetListAllTab( self ):
        tabItems = []
        tabItemsElem = self.find_elemsByCSS(self.CardList_tabItem)
        for tabItemElem in tabItemsElem:
            tabItems.append(tabItemElem.text)
        return tabItems

