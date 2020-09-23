#外键
import time

from public.selenium_page import SeleniumPage


class MbForeignSelection_component(SeleniumPage):


    placeholder_loc = "//div[@title='%s']//span[@class='placeholder']"
    search_label_loc = "//label[@class='search-bar__label']"
    search_input_loc = "//input[@class='search-bar__input']"
    search_item_loc = "//div[@class='relation_field']/span[contains(text(),'%s')]"

    ChildFormPopup_ForeignSelectionBox_SpanValue_loc = "//div[@title='%title']//span[@class='value']"

    def MbForeignSelection_Sendkeys(self,fieldName,option,*args):
        '''外键选择组件输入值
        fieldName：字段标题
        list：下拉选项 list类型
        '''
        #点击选择框
        self.clickElemByXpath_visibility(self.placeholder_loc.replace('%s',fieldName))
        #搜索框输入查询项
        self.clickElemByXpath_visibility(self.search_label_loc)
        time.sleep(1)
        self.sendkeysElemByXpath_visibility(self.search_input_loc,option)
        #点击结果
        self.clickElemByXpath_visibility(self.search_item_loc.replace('%s',option))


    def MbForeignSelection_GetValue_writable_InPopup( self,fieldName):
        '''表单弹层获取可写状态的外键字段值'''
        loc = self.ChildFormPopup_ForeignSelectionBox_SpanValue_loc.replace('%title',fieldName)
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(loc)
        return elem.text