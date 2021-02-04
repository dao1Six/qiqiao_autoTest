#地址组件
from public.selenium_page import SeleniumPage


class Address(SeleniumPage):

    Address_selectionBox_loc = "//div[@data-mark='%s']//span[@class='el-cascader__label']"  #地址组件字段选择下拉框
    Address_selecOption_loc = "//div[@class='el-cascader-menus el-popper 地址选择器']//span[text()='%s']"  #地址组件字段选项
    Address_detilInput_loc = "//div[@data-mark='%s']//textarea[@placeholder='详细地址']"  #地址组件字段地址详情输入框

    #给地址组件输入值
    def Address_Sendkeys(self,fieldName,addkeys,detilkey,*args):
        '''给地址组件字段输入值
        fieldName：字段标题
        addkeys：省市区地址  list类型
        detilkey：详情地址信息
        '''
        self.clickElemByXpath_visibility(self.Address_selectionBox_loc.replace('%s', fieldName))
        for i in addkeys:
            self.clickElemByXpath_visibility(self.Address_selecOption_loc.replace('%s', i))
        self.sendkeysElemByXpath_visibility(self.Address_detilInput_loc.replace('%s', fieldName),detilkey)


    def Address_Sendkeys_External(self,fieldName,addkeys,detilkey,*args):
        '''给外部表单里地址组件字段输入值
        fieldName：字段标题
        addkeys：省市区地址  list类型
        detilkey：详情地址信息
        '''
        self.clickElemByXpath_visibility(self.Address_selectionBox_loc.replace('%s', fieldName))
        for i in addkeys:
            self.clickElemByXpath_visibility(self.Address_selecOption_loc.replace('%s', i))
        self.sendkeysElemByXpath_visibility(self.Address_detilInput_loc.replace('%s', fieldName),detilkey)

