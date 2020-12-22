# coding=utf-8
#评分组件
from public.selenium_page import SeleniumPage


class Grade(SeleniumPage):

    item_loc = "//div[@data-mark='%s']//span[@class='el-rate__item'][%n]"

    def Grade_Sendkeys( self,fieldName,key,*args ):
        """给评分组件输入值
        fieldName：字段标题
        key：分值
        """
        self.clickElemByXpath_visibility(self.item_loc.replace('%s',fieldName).replace('%n',str(key)))