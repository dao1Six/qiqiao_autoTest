#外键
import time

from public.selenium_page import SeleniumPage


class MbForeignSelection_component(SeleniumPage):


    placeholder_loc = "//div[@title='%s']//span[@class='placeholder']"
    search_label_loc = "//label[@class='search-bar__label']"
    search_input_loc = "//input[@class='search-bar__input']"
    search_item_loc = "//div[@class='myScroll_container']//span[text()='%s ']/ancestor::li"

    SelectOptions = "//div[@class='myScroll_container']//div[@class='relation_field']/parent::li"

    ForeignSelectOption_loc = "//div[@class='myScroll_container']//span[text()='%s ']/ancestor::li"

    lastPage_div = "//div[@class='myScroll_loadText' and contains(text(),'没有更多数据')]"

    ChildFormPopup_ForeignSelectionBox_SpanValue_loc = "//div[@title='%title']//span[@class='value']"

    ChildFormPopup_ForeignSelectionBox_Span_readonlyValue_loc = "//div[@title='%title']//span[@class='value readonly']"


    def MbForeignSelection_Sendkeys(self,fieldName,option,*args):
        """外键选择组件输入值
        fieldName：字段标题
        list：下拉选项 list类型
        """
        #点击选择框
        self.clickElemByXpath_visibility(self.placeholder_loc.replace('%s',fieldName))
        if(option=="无"):
            self.clickElemByXpath_visibility(self.search_item_loc.replace('%s','无'))
        else:
            #搜索框输入查询项
            self.clickElemByXpath_visibility(self.search_label_loc)
            self.sendkeysElemByXpath_visibility(self.search_input_loc,option)
            time.sleep(1)
            self.MbForeignSelection_Option_scrollDown()
            #点击结果
            self.clickElemByXpath_visibility(self.search_item_loc.replace('%s',option))

    def MbForeignSelection_SelectionBox_Click( self,fieldName ):
        """点击外键选择组件输入框"""
        #点击选择框
        self.clickElemByXpath_visibility(self.placeholder_loc.replace('%s',fieldName))


    def MbForeignSelection_GetValue_writable_InPopup( self,fieldName):
        """表单弹层获取可写状态的外键字段值"""
        loc = self.ChildFormPopup_ForeignSelectionBox_SpanValue_loc.replace('%title',fieldName)
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(loc)
        return elem.text


    def MbForeignSelection_GetValue_readOnly_InPopup( self,fieldName):
        """表单弹层获取只读状态的外键字段值"""
        elem = self.find_elenmInElemsByXpath_visibility_of_any_elements_located(self.ChildFormPopup_ForeignSelectionBox_Span_readonlyValue_loc.replace('%title',fieldName))
        return elem.text


    def MbForeignSelection_Option_scrollDown( self):
        """外键选项滚动至底部"""
        while(self.find_elemByXPATH_visibility(self.lastPage_div,timeout=2)==None):
            elem = self.find_elemsByXPATH_visibility(self.SelectOptions)[-1]
            self.h5_scroll(elem,0,5000)

    def MbForeignSelection_get_OptionValue(self,fieldName,*args):
        """获取外键选择组件选项值"""
        list = []
        elems = self.find_elemsByXPATH_presence(self.SelectOptions)#.replace('%s',fieldName)
        if elems == None:
            return list
        for elem in elems:
            list.append(elem.text)
        return list


    def MbForeignSelection_SelectOption_isExist(self,value,*args):
        """外键选项是否存在"""
        elem = self.find_elemByXPATH_visibility(self.ForeignSelectOption_loc.replace('%s',value))
        if(elem!=None):
            return True
        return False
