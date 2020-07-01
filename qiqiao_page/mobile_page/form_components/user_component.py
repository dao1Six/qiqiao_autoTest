#人员组件
import time

from public.selenium_page import SeleniumPage


class User(SeleniumPage):


    peopleListName_loc = "div[title='%s'] span.peopleList_name"


    #获取表单人员组件的值
    def GetUserValue( self,fieldName):
        elem = self.find_elenmInElemsByCSS_visibility_of_any_elements_located(self.peopleListName_loc.replace('%s',fieldName))
        value = elem.text
        return value

