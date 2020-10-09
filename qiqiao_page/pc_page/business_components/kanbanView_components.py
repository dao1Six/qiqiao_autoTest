import time
from public.selenium_page import SeleniumPage

class KanBanComponent(SeleniumPage):
    '''看板视图组件'''

    view_card_item_button = "//div[@class='view_card_container']//div[@class='view_card_item'][%n]//div[@class='view_card_item_button']"

    item_MoreButton_loc = "//div[@class='view_card_container']//div[@class='view_card_item'][%n]//div[@class='view_card_item_content'][%i]//i"

    item_Button_loc = "//li[text()='%s']"

    view_card_item_content = "//div[@class='view_card_container']//div[@class='view_card_item'][%n]//div[@class='view_card_item_content'][%i]"

    view_card_item_content_title = "//div[@class='view_card_container']//div[@class='view_card_item'][%n]//div[@class='view_card_item_content'][%i]//div[@class='view_card_item_content_title']/span"

    view_card_item_content_label = "//div[@class='view_card_container']//div[@class='view_card_item'][1]//div[@class='view_card_item_content'][1]//div[contains(@class,'view_card_item_content_sub')]/span[@class='view_card_item_content_label']"

    view_card_item_content_text = "//div[@class='view_card_container']//div[@class='view_card_item'][1]//div[@class='view_card_item_content'][1]//div[contains(@class,'view_card_item_content_sub')]/span[@class='view_card_item_content_text']"

    def KanBanComponent_addButton_click( self,number):
        '''点击看板添加按钮'''
        self.clickElemByXpath_visibility(self.view_card_item_button.replace('%n',str(number)))

    def KanBanComponent_MoveTo_Item_MoreButton( self,number,i):
        '''悬浮看板选项更多按钮'''
        elem = self.find_elenmInElemsByXpath_presence_of_all_elements_located(self.view_card_item_content_title.replace('%n',str(number)).replace('%i',str(i)))
        self.move_to_element(elem)
        time.sleep(1)
        self.clickElemByXpath_visibility(self.item_MoreButton_loc.replace('%n',str(number)).replace('%i',str(i)))



    def KanBanComponent_Button_click( self,name):
        '''点击看板按钮'''

        self.clickElemByXpath_visibility(self.item_Button_loc.replace('%s',name))

    def KanBanComponent_ItemContent_click( self,number,i):
        '''点击看板记录'''
        self.clickElemByXpath_visibility(self.view_card_item_content.replace('%n',str(number)).replace('%i',str(i)))

    def KanBanComponent_Get_RecoreTitleValule( self,number,i ):
        '''返回当前记录标题值'''
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.view_card_item_content_title.replace('%n',str(number)).replace('%i',str(i)))
        if (elem!=None):
            return elem.text
        else:
            return None


    def KanBanComponent_Get_RecoreTextContents( self,number,i ):
        """返回当前记录显示字段值"""
        value = {}
        labelList = []
        textList = []
        labelelems = self.find_elemsByXPATH_visibility(self.view_card_item_content_label.replace('%n',str(number)).replace('%i',str(i)))
        if (labelelems!=None):
            for elem in labelelems:
                labelList.append(elem.text)
        textelems = self.find_elemsByXPATH_visibility(self.view_card_item_content_text.replace('%n',str(number)).replace('%i',str(i)))
        if (textelems!=None):
            for elem in textelems:
                textList.append(elem.text)
        return dict(zip(labelList,textList))

