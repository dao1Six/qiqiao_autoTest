
from AppPage_obj.SaySafePage.fill_data_loc import AppBaseLoc
import time
from public.selenium_page import SeleniumPage

class AppFillSafe(SeleniumPage):



    def app_title(self,page_name):
        '''
        通过名称选择打开的页面，页面可以是工作台，流程，应用
        :param page_name: 要打开的页面名称
        :return:
        '''
        app_loc = AppBaseLoc.app_meau_loc.format(meau_name=page_name)
        self.clickElemByXpath_Presence(app_loc)


    def open_app(self,app_name):
        '''
        通过应用输入应用名称，打开对应用
        :param app_name: 应用的名称
        :return:
        '''
        loc = AppBaseLoc.app_base_loc.format(appname=app_name)
        time.sleep(0.5)
        self.refreshCurrentPage()
        time.sleep(1)
        self.clickElemByXpath_Presence(loc)

    def click_title(self,title_name):
        '''
        通过菜单名称打开应用左侧菜单或者页面
        :param title_name:菜单名称或者页面名称
        :return:

        '''
        loc = AppBaseLoc.meau_base_loc.format(title=title_name)

        self.clickElemByXpath_Presence(loc)



    def click_table(self,table_name):
        '''
        通过选项卡名称，点击运行平台选项卡
        :param table_name: 选项卡名称
        :note:添加操作注释
        :return:

        '''
        loc = AppBaseLoc.tab_base_loc.format(tablename=table_name)
        self.clickElemByXpath_Presence(loc)


    def click_btn_in_title(self,btn_name):
        '''
        点击运行平台页面上方按钮
        :param btn_name:按钮名称
        :return:
        '''
        loc=AppBaseLoc.btn_base_loc.format(btnname=btn_name)
        self.clickElemByXpath_Presence(loc)

    def click_btn_in_form(self,btn_name):
        '''
        点击运行平台页面数据中的按钮
        :param btn_name: 数据表中按钮的名称
        :return:
        '''
        loc=AppBaseLoc.btn_base_loc.format(btnname=btn_name)
        self.clickElemByXpath_Presence(loc)

    def search_data_by_person(self,field_name,person_names):
        '''
        通过人员单选搜索页面数据
        :param field_name: 搜索字段的名称
        :param person_names: 要搜索的人员名称
        :return:

        '''
        loc = AppBaseLoc.search_base_loc.format(search=field_name)
        loc1 = AppBaseLoc.js_base_loc.format(personname=person_names)
        time.sleep(1)
        self.sendkeysElemByXpath_Presence(loc, person_names)
        time.sleep(1)
        self.clickElemByXpath_Presence(loc1)
        self.click_btn_in_title("搜索")




    def search_data_by_department(self,field_name,department_name):
        '''
        通过部门搜索页面数据
        :param field_name: 部门字段的名称
        :param department_name: 要搜索的部门名称
        :return:

        '''
        loc = AppBaseLoc.search_base_loc.format(search=field_name)

        loc1 = AppBaseLoc.js_base_loc.format(personname=department_name)
        self.sendkeysElemByXpath_Presence(loc, department_name)
        self.clickElemByXpath_Presence(loc1)
        self.click_btn_in_title("搜索")



    def search_data_by_city(self,field_name,city):
        '''
        通过地址选择器类型字段搜索数据
        :param field_name: 地址选择器字段名称
        :param city: 要搜搜地址名称，省、市、区，用反斜杠“/”间隔，如：河南/郑州/金水区
        :return:

        '''
        city=str(city)
        if "市" not in city and "区" not in city and "省" in city:
            addr_loc = AppBaseLoc.addr_base_loc.format(fieldname=field_name)
            self.clickElemByXpath_Presence(addr_loc)
            time.sleep(0.5)
            province_li = self.findElemsByXpath(AppBaseLoc.province_li_loc)
            index_num=0
            for i in range(0, len(province_li)):
                if city == province_li[i].text:
                    index_num = int(i) + 1
                    break
            province_loc = AppBaseLoc.province_base_loc.format(inde=index_num)
            self.clickElemByXpath_Presence(province_loc)
            self.click_btn_in_title("搜索")

        elif "/" in city:
            list_addr = city.split("/")
            addr_loc = AppBaseLoc.addr_base_loc.format(fieldname=field_name)
            time.sleep(3)
            self.clickElemByXpath_Presence(addr_loc)

            if len(list_addr)==2:
                time.sleep(1)
                province_li = self.findElemsByXpath(AppBaseLoc.province_li_loc)
                index_num=0
                for i in range(0,len(province_li)):
                    if list_addr[0]==province_li[i].text:
                        index_num=int(i)+1
                        break
                province_loc=AppBaseLoc.province_base_loc.format(inde=index_num)
                self.clickElemByXpath_Presence(province_loc)
                time.sleep(0.5)
                city_li = self.findElemsByXpath(AppBaseLoc.city_li_loc)
                city_index=0
                for j in range(0,len(city_li)):
                    if list_addr[1]==city_li[j].text:
                        city_index=int(j)+1

                city_loc = AppBaseLoc.city_base_loc.format(inde=city_index)
                self.clickElemByXpath_Presence(city_loc)
                self.click_btn_in_title("搜索")
            elif len(list_addr)==3:
                time.sleep(1)
                province_li = self.findElemsByXpath(AppBaseLoc.province_li_loc)
                index_num = 0
                for i in range(0, len(province_li)):
                    if list_addr[0] == province_li[i].text:
                        index_num = int(i)+1
                        break
                province_loc = AppBaseLoc.province_base_loc.format(inde=index_num)
                self.clickElemByXpath_Presence(province_loc)
                time.sleep(0.5)
                city_li = self.findElemsByXpath(AppBaseLoc.city_li_loc)
                city_index = 0
                for j in range(0, len(city_li)):
                    if list_addr[1] == city_li[j].text:
                        city_index = int(j) + 1
                        break

                city_loc = AppBaseLoc.city_base_loc.format(inde=city_index)
                self.clickElemByXpath_Presence(city_loc)
                time.sleep(0.5)
                district_li=self.findElemsByXpath(AppBaseLoc.district_li_loc)
                district_index=0
                for k in range(0,len(district_li)):
                    if list_addr[2]==district_li[k].text:
                        district_index=int(k)+1
                        break

                district_loc = AppBaseLoc.district_base_loc.format(inde=district_index)
                self.clickElemByXpath_Presence(district_loc)
                self.click_btn_in_title("搜索")

        else:
            print("请检输入地址格式是否和搜索字段对应,例如：省，省/市，省/市/区")

    def search_data_by_selection(self,field_name,selections):
        '''
        通过选择框搜索数据，选择框选项值以列表的形式传入
        :param field_name: 选择框字段名称
        :param selections: 要搜索的选项值，以列表的形式传入，如：["中国","美国","日本"]
        :return:
        '''
        loc=AppBaseLoc.search_base_loc.format(search=field_name)
        for i in range(0,len(selections)):
            self.sendkeysElemByXpath_Presence(loc,selections[i])
            time.sleep(1)
            loc1="//div[@title='{name}']".format(name=selections[i])
            self.clickElemByXpath_Presence(loc1)
        self.click_btn_in_title("搜索")


    def search_data_by_time(self,field_name,start_time,end_time):
        '''
        通过日期时间搜索数据
        :param field_name: 日期字段名称
        :param start_time: 搜索数据的开始时间
        :param end_time: 搜索数据的结束时间
        :return:
        '''
        start_date_loc = AppBaseLoc.date_base_loc.format(searchname=field_name, index=1)
        self.clickElemByXpath_Presence(start_date_loc)
        self.addAttributeElemsByXpath_Presence(start_date_loc,"type","text")
        time.sleep(0.5)
        self.sendkeysElemByXpath_Presence(start_date_loc,start_time)
        end_date_loc = AppBaseLoc.date_base_loc.format(searchname=field_name, index=2)
        time.sleep(0.5)
        self.clickElemByXpath_Presence(end_date_loc)
        self.addAttributeElemsByXpath_Presence(end_date_loc,"type","text")
        time.sleep(0.5)
        self.sendkeysElemByXpath_Presence(end_date_loc,end_time)
        self.clickElemByXpath_Presence(start_date_loc)
        field_loc = "//label[@for='{field}']".format(field=field_name)
        self.clickElemByXpath_Presence(field_loc)
        time.sleep(1)
        self.click_btn_in_title("搜索")

    def get_field_values(self,field_name):
        '''
        通过人员选择字段名称，获取对应字段的所有字段值
        :param field_name:获取字段的名称
        :return:返回字段值的列表
        # '''
        loc = "//div[@class='el-table__body-wrapper is-scrolling-left']"
        self.addAttributeElemsByXpath_Presence(loc, "id", "scroll")
        index_num=0
        element_lis=self.findElemsByXpath(AppBaseLoc.form_base_loc)
        for i in range(0,len(element_lis)):
            fc_loc = AppBaseLoc.thead_base_loc.format(num=i + 3)
            text_value = self.waiteElemsByXpath(fc_loc).text
            loc2 = "//div[@id='scroll']"
            element = self.waiteElemsByXpath(loc2)

            if text_value==field_name:
                index_num=i+3
                break
            else:
                self.js("arguments[0].scrollBy(80,0)", element)
                continue
        lis=[]
        total_data = self.waiteElemsByXpath("//span[@class='el-pagination__total']").text
        total_data=str(total_data)
        total_value=total_data.split(" ")
        value = total_value[1]
        for j in range(1,int(value)+1):
            value_loc = AppBaseLoc.tr_base_loc.format(j, index_num)
            result = self.waiteElemsByXpath(value_loc).text
            lis.append(result)
        return lis