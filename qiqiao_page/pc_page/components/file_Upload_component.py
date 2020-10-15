#文件组件
from public.selenium_page import SeleniumPage


class FileUpload(SeleniumPage):

    FileUpload_input_loc = "//div[@data-mark='%s']//input"  # 文件上传组件输入框
    FileUpload_success_loc ="div[title='%s'] ul.file_content"  #文件上传成功标识



    def FileUpload_Sendkeys(self,fieldName,key,*args):
        '''给文件组件输入值
        fieldName：字段标题
        key：文件路径
        '''
        locator = self.FileUpload_input_loc.replace('%s',fieldName)
        self.sendkeysElemByXpath_presence(locator,key)
        #等待上传成功
        # self.wait_elem_visible_CSS(self.FileUpload_success_loc.replace('%s',fieldName))



    #获取文件组件的值