# coding=utf-8
import os
import time
import unittest
from functools import wraps

from Enum.buttonEnum import ButtonEnum
from public.HTMLTestRunner_cn import _TestResult
from public.driver import Driver
from qiqiao_page.pc_page.applicationList_page import ApplicationListPage
from qiqiao_page.pc_page.business_page import BusinessPage
from qiqiao_page.pc_page.form_page import FormPage
from qiqiao_page.pc_page.login_page import LoginPage
from qiqiao_page.pc_page.popup_form_page import PopupFormPage
from qiqiao_page.pc_page.form_page import FormPage
from qiqiao_page.pc_page.portal_page import PortalPage
from qiqiao_page.pc_page.process_page import ProcessPage
from util.dateTimeUtil import DateTimeUtil
from util.excel_xlrd import ExcelReadUtil


class PcBugAppTest_002(unittest.TestCase):
    '''PC端过往补丁应用2'''

    ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"
    excelPath = ProjectRootPath+"\\file_data\\testcase_data\\测试数据.xlsx"

    downloadPath = ProjectRootPath + '\\file_data\\downloadData'

    def isFileExists(self,path):
        if os.path.exists(path):  # 如果文件存在
            # 删除文件，可使用以下两种方法。
            # os.remove(path)
            return True
        else:
            return False # 则返回文件不存在

    def pcLogin(self,account,password):
        '''登录pc端'''
        self.driver = Driver().pcdriver()
        self.driver.maximize_window()
        loginpage = LoginPage(self.driver)
        loginpage.user_login('https://qy.do1.com.cn/qiqiao/runtime', account, password)
        time.sleep(3)


    def test_01( self ):
        '''【补丁】——流程配置子父流程字段传递时，系统报错'''
        self.pcLogin("zhangyuejuan@auto","qiqiao123")
        portalPage = PortalPage(self.driver)
        # 打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(3)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("采购申请")
        formPage = FormPage(self.driver)
        formPage.User_MonomialUser_Sendkeys("人员","张月娟")
        formPage.Date_Sendkeys("日期",DateTimeUtil().Today())
        formPage.Text_Sendkeys("客户","吴健伦")
        formPage.Number_Sendkeys("采购金额",12333)
        formPage.Textarea_Sendkeys("采购说明","的话旮角快点哈数据库大厦的卡士达数据库")
        formPage.FileUpload_Sendkeys("合同",self.excelPath)
        time.sleep(2)
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="发起采购合同申请申请人工任务办理失败")
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="审批采购合同申请任务办理失败")
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="审批采购合同用印申请任务办理失败")
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="审批采购付款申请任务办理失败")
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage.ProcessPage_click_process_menu("我的待办")
        processPage.ProcessPage_click_process_record(1)
        formPage.Form_Button_Click("办理")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="审批采购付款申请任务办理失败")




    def test_02( self ):
        '''【补丁】——表单设置唯一校验，在流程中不生效'''
        self.pcLogin("zhangyuejuan@auto","qiqiao123")
        portalPage = PortalPage(self.driver)
        # 打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        time.sleep(3)
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_icon("唯一性校验流程")
        formPage = FormPage(self.driver)
        formPage.Text_Sendkeys("客户","440783199406116911")
        formPage.Form_Button_Click("提交")
        formPage.Form_ProcessHandle_Pop_QuerenButton_Click()
        self.assertIn('[客户]值必须唯一',formPage.Public_GetAlertMessage(),msg="【补丁】——表单设置唯一校验，在流程中不生效")



    def test_03( self ):
        '''【补丁】——PC运行平台--流程管理，发起人和发起时间不显示'''
        self.pcLogin("zhangyuejuan@auto","qiqiao123")
        portalPage = PortalPage(self.driver)
        # 打开“发起流程列表”
        portalPage.PortalPage_Click_HeaderMenu('流程')
        processPage = ProcessPage(self.driver)
        processPage.ProcessPage_click_process_menu("流程管理")
        processPage.ProcessPage_click_process_record(1)
        time.sleep(3)
        formPage = FormPage(self.driver)
        self.assertNotEqual(formPage.Form_Get_Sponsor(),"",msg="发起人信息错误")
        self.assertNotEqual(formPage.Form_Get_LaunchTime(),"发起时间错误")


    def test_04( self ):
        '''【补丁】PC运行平台-跨应用表单，触发事件，筛选条件配置：外键   id   等于  本表   外键   id，报表单id不存在'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','A')
        businessPage = BusinessPage(self.driver)
        businessPage.ListComponent_Click_ListHeader_Button('添加')
        formPage = FormPage(self.driver)
        formPage.Text_Sendkeys('单行文本1',DateTimeUtil().Today())
        formPage.ForeignSelection_Sendkeys('外键选择1',"c")
        time.sleep(2)
        formPage.Form_Button_Click("提交")
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="触发事件执行失败")
        #点击全部应用选项
        businessPage.BusinessPage_HeardItem_AllApp_Click()
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','B')
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1,3),DateTimeUtil().Today())


    def test_05( self ):
        '''【补丁】-PC运行平台-子表单组件。通过“添加一行按钮”添加数据到第10条的时候。需要点击两次才出来。并且添加后第10条的数据不可用字段必填校验不生效'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','生产运管系统')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('项目信息管理')
        businessPage.BusinessPage_LeftMenu_Click('项目信息管理3')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage = FormPage(self.driver)
        for i in range(1,15):
            formPage.ChildForm_AddOneRowButton_Click("项目团队成员")
            formPage.ChildForm_List_Text_sendkeys("项目团队成员",i,"项目编号","2255555")
            formPage.ChildForm_List_User_sendkeys("项目团队成员","员工",i,["吴健伦"])
            formPage.ChildForm_List_Text_sendkeys("项目团队成员",i,"岗位","2255555")
            formPage.ChildForm_List_Date_sendkeys("项目团队成员","进入项目时间",i,"2020-09-18")
        time.sleep(3)
        formPage.Form_Button_Click("提交")
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="【补丁】-PC运行平台-子表单组件。通过“添加一行按钮”添加数据到第10条的时候。需要点击两次才出来。并且添加后第10条的数据不可用字段必填校验不生效")



    def test_06( self ):
        '''【补丁】PC运行平台--通过触发更新事件更新单行文本，更新的值通过公式计算【如截图所示】，提交表单后会多显示“.0”'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','问题复现-刁惠云')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('触发更新事件问题复现')
        businessPage.BusinessPage_LeftMenu_Click('问题复现')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage = FormPage(self.driver)
        formPage.Number_Sendkeys("整数",10)
        formPage.Number_Sendkeys("小数",10)
        formPage.Number_Sendkeys("金额",10)
        formPage.Number_Sendkeys("百分比",10)
        formPage.Number_Sendkeys("公式大写",10)
        formPage.Form_Button_Click("提交")
        time.sleep(2)
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage.Number_Sendkeys("整数",100)
        formPage.Number_Sendkeys("小数",100)
        formPage.Number_Sendkeys("金额",100)
        formPage.Number_Sendkeys("百分比",100)
        formPage.Number_Sendkeys("公式大写",100)
        formPage.Form_Button_Click("提交")
        time.sleep(3)
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(2,13),"￥100￥301",msg="【补丁】PC运行平台--通过触发更新事件更新单行文本，更新的值通过公式计算【如截图所示】，提交表单后会多显示“.0”")


    def test_07( self ):
        '''【补丁】PC运行平台--触发更新事件中，数字字段配置更新公式（DAYSDIFF (本表字段.日期时间 ,TODAY ())），更新后数字字段显示为"--"'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','问题复现-刁惠云')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('触发更新事件问题复现')
        businessPage.BusinessPage_LeftMenu_Click('目标表')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage = FormPage(self.driver)
        formPage.Text_Sendkeys("单行文本","道一")
        formPage.Form_Button_Click("提交")
        time.sleep(2)
        businessPage.BusinessPage_LeftMenu_Click('本表')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage.Text_Sendkeys("单行文本","道一")
        formPage.DateTime_Sendkeys("日期时间",DateTimeUtil().Today()+" 00:00")
        time.sleep(2)
        formPage.Form_Button_Click("提交")
        time.sleep(2)
        businessPage.BusinessPage_LeftMenu_Click('目标表')
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1,5),"0",msg="【补丁】PC运行平台--触发更新事件中，数字字段配置更新公式（DAYSDIFF (本表字段.日期时间 ,TODAY ())），更新后数字字段显示为--")



    def test_08( self ):
        '''人员信息连带写入'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','PC端补丁收集应用')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('人员部门连带写入')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage = FormPage(self.driver)
        # formPage.User_MonomialUser_Sendkeys("人员单选","吴健伦")
        time.sleep(2)
        formPage.Form_Button_Click("提交")
        assert '成功' in businessPage.Public_GetAlertMessage()
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1,3),'吴健伦',msg='人员姓名显示不对')
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1,4),'创新技术中心->产品研发二部->产品规划组',msg='人员部门显示不对')
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1,5),'01783',msg='人员工号显示不对')
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1,6),'wujianlun',msg='人员账号显示不对')
        self.assertEqual(businessPage.ListComponent_GetTable_Td_Value(1,7),'13025805485',msg='人员手机号显示不对')


    def test_09( self ):
        '''【补丁】——PC端日期函数HOURSDIFF计算时间类型字段时，无效'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','PC端补丁收集应用')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('日期时间计算')
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage = FormPage(self.driver)
        formPage.Time_Sendkeys("时间1","23:59")
        time.sleep(2)
        formPage.Time_Sendkeys("时间2","22:59")
        time.sleep(2)
        self.assertEqual(1,formPage.Number_GetValue_Writable("时间差"),msg="【补丁】——PC端日期函数HOURSDIFF计算时间类型字段时，无效")


    def test_10( self ):
        '''【补丁】PC运行平台--看板-详情按钮-页面内操作的编辑和删除按钮点击一直在loading'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','项目管理')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('任务列表')
        businessPage.KanBanComponent_addButton_click(1)
        formPage = PopupFormPage(self.driver)
        formPage.ForeignSelection_Sendkeys("项目标题","dadasdad")
        formPage.Text_Sendkeys("任务名称","会打开等哈记得哈加达和")
        formPage.Number_Sendkeys("任务分值",99)
        formPage.DateTime_Sendkeys("任务开始时间",DateTimeUtil().Today()+" 00:00")
        formPage.DateTime_Sendkeys("任务截止时间",DateTimeUtil().Tomorrow() + " 00:00")
        formPage.Selection_SingleXiala_Sendkeys("重要程度","紧急但不重要")
        time.sleep(2)
        formPage.PopupFormPage_Button_Click("提交")
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="看板视图添加数据失败")
        self.assertEqual({'项目标题': 'dadasdad', '任务分值': '99', '任务负责人': '--', '任务开始时间': DateTimeUtil().Today()+" 00:00", '任务截止时间': DateTimeUtil().Tomorrow() + " 00:00"},businessPage.KanBanComponent_Get_RecoreTextContents(1,1),msg="看板视图显示字段值不正确")
        businessPage.KanBanComponent_MoveTo_Item_MoreButton(1,1)
        businessPage.KanBanComponent_Button_click("编辑")
        formPage.Text_Sendkeys("任务名称","2222222",isclear=True)
        formPage.PopupFormPage_Button_Click("提交")
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="看板视图编辑数据失败")
        businessPage.KanBanComponent_ItemContent_click(1,1)
        formPage.PopupFormPage_Button_Click("编辑")
        time.sleep(2)
        formPage.Text_Sendkeys("任务名称","33333",isclear=True,labelIndex=1)
        formPage.PopupFormPage_Button_Click("提交")
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="看板视图详情按钮进入编辑数据失败")
        businessPage.KanBanComponent_ItemContent_click(1,1)
        formPage.PopupFormPage_Button_Click("删除")
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="看板视图详情按钮进入删除数据失败")


    def test_11( self ):
        '''【补丁】——（优化）触发事件，使用插入事件，把sum函数计算的记过用，upper_ram函数转换为大写时，前后结果不一致'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','PC端补丁收集应用')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click('小数转换插入列表')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        businessPage.BusinessPage_LeftMenu_Click('小数和列表')
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage = FormPage(self.driver)
        formPage.Number_Sendkeys("数字1",10.12600)
        formPage.Number_Sendkeys("数字2",10.12600)
        formPage.Number_Sendkeys("数字3",10.12600)
        time.sleep(1)
        self.assertEqual(30.38,formPage.Number_GetValue_Writable("总和"),msg="小数和计算错误")
        formPage.Form_Button_Click("提交")
        self.assertIn('成功',formPage.Public_GetAlertMessage(),msg="提交失败")
        businessPage.BusinessPage_LeftMenu_Click('小数转换插入列表')
        self.assertEqual("$叁拾元叁角捌分",businessPage.ListComponent_GetTable_Td_Value(1,3),msg="列表值显示错误")
        businessPage.ListComponent_Click_ListRow_Button("详情",1)
        self.assertEqual("$叁拾元叁角捌分",formPage.Text_GetValue_readOnly("单行文本1"),msg="详情值显示错误")



    def test_12( self ):
        '''【补丁】——数据过滤高级函数，日期字段大于等于today函数时，等于逻辑不生效，只显示满足大于的数据'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','PC端补丁收集应用')
        businessPage = BusinessPage(self.driver)
        time.sleep(2)
        businessPage.BusinessPage_LeftMenu_Click('日期高级函数测试')
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage = FormPage(self.driver)
        formPage.Date_Sendkeys("日期",DateTimeUtil().Yesterday())
        formPage.Form_Button_Click("保存并继续添加")
        time.sleep(1)
        formPage.Date_Sendkeys("日期",DateTimeUtil().Today())
        formPage.Form_Button_Click("保存并继续添加")
        time.sleep(1)
        formPage.Date_Sendkeys("日期",DateTimeUtil().Tomorrow())
        formPage.Form_Button_Click("提交")
        time.sleep(1)
        self.assertEqual(DateTimeUtil().Tomorrow(),businessPage.ListComponent_GetTable_Td_Value(1,3),msg="列表值显示错误")
        self.assertEqual(2,businessPage.ListComponent_GetRecordTotal(),msg="过滤条数不正确")


    def test_13( self ):
        '''PC业务建模页面权限测试'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','PC端补丁收集应用')
        businessPage = BusinessPage(self.driver)
        self.assertTrue(businessPage.BusinessPage_LeftMenu_isExist('应用管理员权限页面'),msg="权限错误")
        self.pcLogin("diaohuiyun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','PC端补丁收集应用')
        businessPage = BusinessPage(self.driver)
        self.assertFalse(businessPage.BusinessPage_LeftMenu_isExist('应用管理员权限页面'),msg="权限错误")



    def test_14( self ):
        '''【补丁】——数字组件sum函数，计算结果数值过大（上亿），提交数据之后，结果失真（1787222333765623.69变为1787222333760000）'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','费用管理测试版')
        businessPage = BusinessPage(self.driver)
        if (businessPage.ListComponent_GetRecordTotal() > 0):
            businessPage.ListComponent_SelectAllRecord()
            businessPage.ListComponent_Click_ListHeader_Button('删除')
            businessPage.ListComponent_TooltipButton_Click('确定')
            assert '成功' in businessPage.Public_GetAlertMessage()
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage = FormPage(self.driver)
        formPage.ChildForm_AddOneRowButton_Click("费用报销明细")
        formPage.ChildForm_List_Number_sendkeys("费用报销明细","费用金额",1,1234567891230.34)
        formPage.ChildForm_AddOneRowButton_Click("费用报销明细")
        formPage.ChildForm_List_Number_sendkeys("费用报销明细","费用金额",2,1234567891230.34)
        time.sleep(2)
        self.assertEqual(2469135782460.68,formPage.Number_GetValue_Writable("费用总额"),msg="费用总额计算错误")
        formPage.Form_Button_Click("提交")
        self.assertEqual("2469135782460.68",businessPage.ListComponent_GetTable_Td_Value(1,7),msg="费用总额列表显示错误")
        businessPage.ListComponent_Click_ListRow_Button("详情",1)
        self.assertEqual("2469135782460.68",formPage.Number_GetValue_readOnly("费用总额"),msg="费用总额详情表单显示错误")




    def test_15( self ):
        '''【补丁】——PC端运行平台，列表配置自定义角色范围，选项卡显示统计数量错误'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','数据过滤测试应用')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click("测试列表选项卡统计")
        self.assertEqual(['全部(150)', '单项选择1(150)', '单项选择2(0)', '单项选择3(0)'],businessPage.ListComponent_get_tablistValule(),msg="【补丁】——PC端运行平台，列表配置自定义角色范围，选项卡显示统计数量错误'")





    def test_16( self ):
        '''【补丁】——PC端运行平台，数据联动，使用IF函数计算结果联动时，无效'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','加特可人事评价模块')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click("TC层员工评价表")
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage = FormPage(self.driver)
        formPage.MultiForm_AddButton_Click("业绩评价")
        time.sleep(2)
        formPage.MultiForm_List_sendkeysTo_Number("业绩评价",1,16,50)
        formPage.MultiForm_AddButton_Click("业绩评价")
        time.sleep(2)
        formPage.MultiForm_List_sendkeysTo_Number("业绩评价",2,16,50)
        time.sleep(2)
        self.assertEqual("极差",formPage.Text_GetValue_writable("业绩评语"),msg="【补丁】——PC端运行平台，数据联动，使用IF函数计算结果联动时，无效")



    def test_17( self ):
        '''【补丁】——外键选择组件设置可用条件为高级函数OR，对另外外键字段值进行判断时不生效'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','美安居建材云办公系统')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click("生产任务单明细")
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage = FormPage(self.driver)
        formPage.ForeignSelection_Sendkeys("生产机组","生产机组甲")
        self.assertTrue(formPage.Form_field_isVisibility("袋装重量"))


    def test_18( self ):
        '''【补丁】——外键选择组件配置关联筛选字段为外键选择时，填写数据之后，关联选项重复'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','美安居建材云办公系统')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click("品种型号配比登记表")
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage = FormPage(self.driver)
        formPage.ForeignSelection_SelectionBox_Click("砂浆品种")
        page1 =  formPage.ForeignSelection_GetValue_InDialog()
        formPage.ForeignSelection_fanye_InDialog(ButtonEnum.DOWN.value)
        page2 = formPage.ForeignSelection_GetValue_InDialog()
        formPage.ForeignSelection_fanye_InDialog(ButtonEnum.DOWN.value)
        page3 = formPage.ForeignSelection_GetValue_InDialog()
        foreignList = page1+page2+page3
        foreignSet = set(foreignList)
        self.assertEqual(len(foreignList),len(foreignSet),msg="【补丁】——外键选择组件配置关联筛选字段为外键选择时，填写数据之后，关联选项重复")
        self.assertEqual(len(foreignSet),26,msg="外键选项数目显示不对")


    def test_19( self ):
        '''【补丁】——外键选择组件配置关联筛选字段为外键选择时，填写数据之后，关联选项重复'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','美安居建材云办公系统')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click("砂浆型号登记表")
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        time.sleep(1)
        formPage = FormPage(self.driver)
        formPage.ForeignSelection_SelectionBox_Click("砂浆品种",index1=1)
        time.sleep(1)
        formPage.ForeignSelection_Option_scrollDown("砂浆品种")
        time.sleep(2)
        foreignList =  formPage.ForeignSelection_get_OptionValue("砂浆品种")
        foreignSet = set(foreignList)
        self.assertEqual(len(foreignList),len(foreignSet),msg="【补丁】——外键选择组件配置关联筛选字段为外键选择时，填写数据之后，关联选项重复")
        self.assertEqual(len(foreignSet),26,msg="外键选项数目显示不对")



    def test_20( self ):
        '''外键联动筛选'''
        self.pcLogin("wujianlun@auto","do1qiqiao")
        portalPage = PortalPage(self.driver)
        portalPage.PortalPage_Click_HeaderMenu("应用")
        applicationListPage = ApplicationListPage(self.driver)
        applicationListPage.ApplicationListPage_ClickApplicationIcon('默认分组','美安居建材云办公系统')
        businessPage = BusinessPage(self.driver)
        businessPage.BusinessPage_LeftMenu_Click("品种型号配比登记表")
        businessPage.ListComponent_Click_ListHeader_Button("添加")
        formPage = FormPage(self.driver)
        formPage.ForeignSelection_SelectionBox_Click("砂浆品种")
        formPage.ForeignSelection_SearchaInputSendkeys_InDialog("砂浆测试1")
        time.sleep(2)
        formPage.ForeignSelection_fanye_InDialog(ButtonEnum.DOWN.value)
        time.sleep(1)
        formPage.ForeignSelection_ClickOption_InDialog("砂浆测试1")
        formPage.Selection_SingleBox_Sendkeys("是否防冻","防冻")
        time.sleep(1)
        formPage.ForeignSelection_SelectionBox_Click("砂浆型号")
        foreignList = formPage.ForeignSelection_get_OptionValue("砂浆型号")
        self.assertEqual(len(foreignList),0,msg="外键联动筛选选项数目显示不对")
        formPage.Selection_SingleBox_Sendkeys("是否防冻","非防冻")
        time.sleep(1)
        formPage.ForeignSelection_SelectionBox_Click("砂浆型号")
        foreignList = formPage.ForeignSelection_get_OptionValue("砂浆型号")
        self.assertTrue(formPage.ForeignSelection_SelectOption_isExist("A0001"),msg="外键联动筛选选项值筛选不正确")
        self.assertEqual(len(foreignList),1,msg="外键联动筛选选项数目显示不对")
