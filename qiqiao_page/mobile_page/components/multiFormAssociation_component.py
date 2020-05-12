#多表关联组件
from public.selenium_page import SeleniumPage


class MultiFormAssociation(SeleniumPage):

    #选项
    checkbox_loc = "div[title='%s'] input[type='checkbox']"


    def CheckboxIsSelect(self,fieldName,IndexList):
        for index in IndexList:
            elem = self.find_elemByCSS(self.checkbox_loc.replace('%s',fieldName))[index]
            while elem.is_selected() == False:
                return False
        return True