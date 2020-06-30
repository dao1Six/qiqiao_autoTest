# coding=utf-8
import os
import time
import unittest
from functools import wraps

from public.HTMLTestRunner_cn import _TestResult
from public.driver import Driver
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.form_page import FormPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.portal_page import PortalPage
from qiqiao_page.pc_page.process_page import ProcessPage
from util.parseExcel import ParseExcel


class PomAppTest_001(unittest.TestCase):


    # ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"
    # excelPath = ProjectRootPath+"\\testcase\\testcase_data\\user_token.xlsx"
    # sheetName = "user_token"
    # excel = ParseExcel(excelPath, sheetName)
    # accountList = excel.getColValues(1)
    # tokenList = excel.getColValues(2)
    # userDict = dict(zip(accountList, tokenList))



    def setUp(self):
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        # loginpage.user_login('http://runtime.qwqa.do1.work', "wanghao@uat", "qiqiao123")
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@hui", "do1qiqiao")
        time.sleep(5)


    def screenshot_error(func):
        def _screenshot_error(self,*args,**kwargs):
            try:
                func(self,*args,**kwargs)
            except AssertionError as err:
                self.imgs.append(self.driver.get_screenshot_as_base64())
                _TestResult.addFailure(_TestResult(self),self,err)
            except Exception as e:
                self.imgs.append(self.driver.get_screenshot_as_base64())
                _TestResult.addError(_TestResult(self),self,e)
        return _screenshot_error



    def tearDown(self) -> None:
        self.driver.quit()



    #@screenshot_error
    def test_01( self ):
        '''道一云生产运营应用，立项申请流程(事业二部)流程'''

        portalPage = PortalPage(self.driver)
        self.assertEquals(portalPage.get_loginUser_name(),'王浩')
        #打开“发起流程列表”
        portalPage.click_header_menu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.click_process_icon("立项申请流程(事业二部)")

        formPage = FormPage(self.driver)
        formPage.Text_Sendkeys("项目名称","中科信息立项申请")
        formPage.Textarea_Sendkeys("项目简介","中科信息立项申请哈哈哈哈哈哈哈")
        #
        formPage.Dept_MonomialDept_Sendkeys("所属一级部门","企微")
        formPage.Dept_MonomialDept_Sendkeys("所属二级部门", "企微")
        self.assertEquals(formPage.User_GetMonomialUserValue_readOnly("项目经理"),"王浩")

        #点击管理订单添加按钮字段
        formPage.ChildForm_AddButton_Click("关联订单")
        formPage.ForeignSelection_InChildForm_Sendkeys("关联订单","关联订单","电信")
        time.sleep(2)
        formPage.Selection_MonomialSelect_InChildForm_Sendkeys("关联订单","战略意义","标杆作用")
        formPage.Number_Sendkeys("预估成本（人天）",10)
        #点击子表保存按钮
        formPage.click_ChildForm_Button('保存')

        print(formPage.getNumberValue_readOnly("项目总金额"))
        print(formPage.getNumberValue_readOnly("项目预估总成本（人天）"))
        print(formPage.Date_GetValue_writable("项目启动时间"))
        print(formPage.Selection_GetSelectionBoxValue_writable("项目类型"))
        time.sleep(1)
        formPage.Selection_MonomialSelect_Sendkeys('项目等级','普通（普）')
        formPage.Date_Sendkeys("预计验收时间","2020-06-22")
        formPage.Text_Sendkeys("客户名称", "李嘉诚")
        formPage.Text_Sendkeys("甲方对接人", "李嘉诚")
        formPage.Text_Sendkeys("联系方式", "13025805485")
        formPage.Textarea_Sendkeys("备注信息", "中科信息立项申请哈哈哈哈哈哈哈")

        # 点击项目里程碑添加按钮字段
        formPage.ChildForm_AddButton_Click("项目里程碑")
        formPage.Text_InChildForm_Sendkeys("项目里程碑","阶段名称", "测试")
        formPage.Date_InChildForm_Sendkeys("项目里程碑","计划完成时间", "2020-06-22")
        time.sleep(2)
        # 点击子表保存按钮
        formPage.click_ChildForm_Button('保存')
        formPage.Form_Button_Click("提交")
        formPage.selectProcessManager(["王浩"])
        time.sleep(5)
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        formPage.Form_Button_Click("审核通过")


    def test_001( self ):
        '''处理待办'''
        portalPage = PortalPage(self.driver)
        # self.assertEquals(portalPage.get_loginUser_name(),'王浩')
        #打开“发起流程列表”
        portalPage.click_header_menu('流程')
        processPage = ProcessPage(self.driver)
        processPage.click_process_menu("我的待办")
        processPage.click_process_record(1)
        formPage = FormPage(self.driver)
        formPage.MultiForm_BatchManagementButton_Click("领用明细")
        formPage.MultiForm_BathManagePage_Record_Tick("领用明细",[1,2])
        formPage.MultiForm_BathManagePage_ConfirmButton_Tick("领用明细")
        formPage.MultiForm_GetTdValue("领用明细",1,5)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        time.sleep(10)


    def test_02( self ):
        '''添加工时'''
        self.driver.get("http://runtime.qwqa.do1.work/?corp_id=wwd5af6a678822e11b#/application/business?applicationId=b289921621e245e2a114c481ddfc4304&mainColor=orange&businessModelId=e532fc5dc28d414ba10b4311bb2c31da")
        businessPage = BusinessPage(self.driver)
        businessPage.ListComponent_Click_ListHeader_Button("添加工时")
        formPage = FormPage(self.driver)
        formPage.ChildForm_AddButton_Click('工时明细')
        formPage.Selection_RadioSelect_InChildForm_Sendkeys("工时明细","工时类型","产品研发工作")
        time.sleep(2)
        formPage.Date_InChildForm_Sendkeys("工时明细","工时日期", "2020-06-29",isclear=True)
        formPage.ForeignSelection_InChildForm_Sendkeys("工时明细","产品名称","测试20")
        formPage.Selection_MonomialSelect_InChildForm_Sendkeys("工时明细","工作内容","产品测试")
        formPage.click_ChildForm_Button("保存")
        time.sleep(2)
        formPage.ChildForm_AddButton_Click('工时明细')
        formPage.Selection_RadioSelect_InChildForm_Sendkeys("工时明细", "工时类型", "产品研发工作")
        time.sleep(2)
        formPage.Date_InChildForm_Sendkeys("工时明细", "工时日期", "2020-06-30", isclear=True)
        formPage.ForeignSelection_InChildForm_Sendkeys("工时明细", "产品名称", "测试20")
        formPage.Selection_MonomialSelect_InChildForm_Sendkeys("工时明细", "工作内容", "产品测试")
        formPage.click_ChildForm_Button("保存")






    def test_03( self ):
        self.driver.get("http://runtime.qwqa.do1.work/?corp_id=wwd5af6a678822e11b#/application/business?applicationId=ce61fe66d15f4b4b9efbe7267413f307&mainColor=red&businessModelId=c037f4a94417421cb2caa2f228dc1e54")
        businessPage = BusinessPage(self.driver)
        businessPage.ListComponent_MoveTo_ListRow_MoreButton(1)
        businessPage.ListComponent_Click_ListRow_Button("打印",1)
        # businessPage.ListComponent_Click_ExpandBtn()
        # businessPage.ListComponent_QueryItem_Sendkeys("创建人", "吴健伦",type="user")
        # businessPage.ListComponent_QueryItem_Sendkeys("时间", "11:37","13:37",type="date")
        # businessPage.ListComponent_QueryItem_Sendkeys("整数",5,type="text ")
        time.sleep(10)

    def test_04( self ):
        '''资产管理应用领用流程'''
        portalPage = PortalPage(self.driver)
        # self.assertEquals(portalPage.get_loginUser_name(),'王浩')
        #打开“发起流程列表”
        portalPage.click_header_menu('流程')
        time.sleep(5)
        processPage = ProcessPage(self.driver)
        processPage.click_process_icon("领用")
        formPage = FormPage(self.driver)
        formPage.Selection_CheckboxSelect_Sendkeys("设备类别",["平板","手机"])
        formPage.Textarea_Sendkeys("备注","很大很大空间等哈看进度哈大噶还记得噶还记得噶实践活动")
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        time.sleep(10)













