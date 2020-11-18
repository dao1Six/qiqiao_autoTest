#图片组件
from public.selenium_page import SeleniumPage


class MbPicUpload(SeleniumPage):


    PicUpload_input_loc = "//div[@title='%s']//input[@type='file']"  # 图片上传字段输入框
    PicUpload_success_loc = "//div[@title='%s']//div[@class='showImage']//img" #图片上传成功标识

    #给图片组件输入值
    def MbPicUpload_Sendkeys(self,fieldName,picPath,uplodaTime=5,*args):
        """给文件组件输入值
        fieldName：字段标题
        picPath：图片路径
        """
        self.sendkeysElemByXpath_presence(self.PicUpload_input_loc.replace('%s',fieldName),picPath)
        #判斷是否上傳圖片成功
        return self.wait_elem_visible_XPATH(self.PicUpload_success_loc.replace('%s', fieldName),timeout=uplodaTime)



    #获取图片组件的值