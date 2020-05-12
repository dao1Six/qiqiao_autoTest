#选择组件


from public.selenium_page import SeleniumPage


class Selection(SeleniumPage):

    #选项
    radio_loc = "div[title='%s'] input[type='radio']"

    def RadioIsSelect(self,fieldName,index):
        elem = self.find_elemByCSS(self.radio_loc.replace('%s',fieldName))[index]
        return elem.is_selected()

