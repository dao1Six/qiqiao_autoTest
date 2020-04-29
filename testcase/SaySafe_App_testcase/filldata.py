import time
import unittest
from public.driver import pcdriver
from qiqiao_PublicPage.login_page import LoginPage
from qiqiao_PublicPage.portal_page import PortalPage
from qiqiao_PublicPage.applicationList_page import ApplicationListPage
from AppPage_obj.SaySafePage.fill_data_page import AppFillSafe


class FillReportTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = pcdriver()
        cls.driver.maximize_window()
        loginpage = LoginPage (cls.driver)
        loginpage.user_login ('https://qy.do1.com.cn/qiqiao/runtime', "wujianlun@do1", "do1qiqiao")
        portalpage = PortalPage (cls.driver)
        portalpage.click_header_menu ("应用")
        applicationListPage = ApplicationListPage(cls.driver)
        time.sleep(2)
        applicationListPage.click_application("全员报平安2.2")
        cls.runtime = AppFillSafe(cls.driver)
        cls.runtime.click_title("报平安")


    @classmethod
    def tearDownClass(cls) -> None:
        pass


    def test_search_data_by_person(self):
        self.runtime.refreshCurrentPage()
        self.runtime.search_data_by_person("员工姓名","吴健伦")
        result=self.runtime.get_field_values("员工姓名")
        for i in range(0,len(result)):
            self.assertEqual("吴健伦",result[i])



    def test_search_data_by_department(self):
        self.runtime.refreshCurrentPage()
        self.runtime.search_data_by_department("所属部门","员工成功部")
        result=self.runtime.get_field_values("所属部门")
        for i in range(0,len(result)):
            self.assertEqual("员工成功部",result[i])


    def test_search_data_by_city(self):
        self.runtime.refreshCurrentPage()
        self.runtime.search_data_by_city("居住城市","广东省/广州市")
        result=self.runtime.get_field_values("所在城市")
        for i in range(0,len(result)):
            self.assertEqual("广东省/广州市",result[i])

    def test_search_data_by_symptom(self):
        self.runtime.refreshCurrentPage()
        self.runtime.search_data_by_selection("是否以下症状",["咳嗽"],)
        result = self.runtime.get_field_values("是否以下症状")
        for i in range(0,len(result)):
            self.assertEqual("咳嗽",result[i])


    def test_search_data_by_contact(self):
        self.runtime.refreshCurrentPage()
        self.runtime.search_data_by_selection("是否有所接触",["最近去过武汉"])
        result = self.runtime.get_field_values("是否有所接触")
        for i in range(0,len(result)):
            self.assertEqual("最近去过武汉",result[i])

    def test_search_data_by_date(self):
        self.runtime.refreshCurrentPage()
        self.runtime.search_data_by_time("提交日期","2020-04-8","2020-04-10")
        time.sleep(10)
        result = self.runtime.get_field_values("提交日期")
        for i in range(0,len(result)):
            self.assertEqual("2020-04-08",result[i])

    def test_table_normal(self):
        self.runtime.refreshCurrentPage()
        self.runtime.click_table("正常（36.1-37℃）")
        result = self.runtime.get_field_values("体温情况（腋窝测量）")
        for i in range(0, len(result)):
            self.assertEqual("正常（36.1-37℃）", result[i])

    def test_table_lowfever(self):
        self.runtime.refreshCurrentPage()
        self.runtime.click_table("低烧（37.1-38℃）")
        result = self.runtime.get_field_values("体温情况（腋窝测量）")
        for i in range(0, len(result)):
            self.assertEqual("低烧（37.1-38℃）", result[i])


    def test_table_moderatefever(self):
        self.runtime.refreshCurrentPage()
        self.runtime.click_table("中度发热（38.1-39℃）")
        result = self.runtime.get_field_values("体温情况（腋窝测量）")
        for i in range(0, len(result)):
            self.assertEqual("中度发热（38.1-39℃）", result[i])


    def test_table_hightfever(self):
        self.runtime.refreshCurrentPage()
        self.runtime.click_table("高烧（39.1-41℃）",)
        result = self.runtime.get_field_values("体温情况（腋窝测量）",)
        for i in range(0, len(result)):
            self.assertEqual("高烧（39.1-41℃）", result[i])


if __name__=="__main__":
    unittest.main()

