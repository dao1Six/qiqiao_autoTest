#部门组件
import time

from public.selenium_page import SeleniumPage


class Dept(SeleniumPage):


    departmentListName_loc = "div[title='%s'] div.departmentList_name>span"




    #获取部门值
    def GetDeptVale( self,fieldName):
        elem = self.find_elemByCSS(self.departmentListName_loc.replace('%s',fieldName))
        value = elem.text
        return value

