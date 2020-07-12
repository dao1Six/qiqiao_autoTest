#外键
import time

from public.selenium_page import SeleniumPage


class MbForeignSelection_component(SeleniumPage):


    placeholder_loc = "//div[@title='%s']//span[@class='placeholder']"
    search_label_loc = "//label[@class='search-bar__label']"
    search_input_loc = "//input[@class='search-bar__input']"
    search_item_loc = "//div[@class='relation_field']/span[contains(text(),'%s')]"


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
