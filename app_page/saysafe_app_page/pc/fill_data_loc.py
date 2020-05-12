class AppBaseLoc(object):
    '''
    App应用页面基础css
    '''
    app_meau_loc="//a[text()='应用']"
    app_base_loc="//p[@title='{appname}']/../div"  #打开应用基础css
    meau_base_loc = "//span[@title='{title}']" #左侧菜单栏基础css
    #tab_base_loc = "//div[text()='{tablename}']" #选项卡基础css
    tab_base_loc = "//div[contains(text(),'{tablename}')]"  # 选项卡基础css
    search_base_loc = "//label[@for='{search}']/following-sibling::div[1]/div/div/div/input" #搜索数据基础css
    btn_base_loc = "//button/span[text()='{btnname}']"  #按钮基础css
    js_base_loc="//div[@title='{personname}']"
    addr_base_loc = "//label[@for='{fieldname}']/following-sibling::div/div/span/span"

    province_li_loc = "//ul[@role='menu'][1]/li"
    province_base_loc="//ul[@role='menu'][1]/li[{inde}]/span"

    city_li_loc="//ul[@role='menu'][2]/li"
    city_base_loc="//ul[@role='menu'][2]/li[{inde}]/span"

    district_li_loc="//ul[@role='menu'][3]/li"
    district_base_loc="//ul[@role='menu'][3]/li[{inde}]/span"

    date_base_loc="//label[@for='{searchname}']/following-sibling::div/div/div/input[{index}]"

    form_base_loc="//*[@id='app']/section/section/div/div[2]/div/div/div[1]/div/div[1]/div/div[3]/div/div[4]/div[1]/table/thead/tr/th"
    thead_base_loc="//*[@id='app']/section/section/div/div[2]/div/div/div[1]/div/div[1]/div/div[3]/div/div[2]/table/thead/tr/th[{num}]/div/span"
    tr_base_loc="//*[@id='app']/section/section/div/div[2]/div/div/div[1]/div/div[1]/div/div[3]/div/div[3]/table/tbody/tr[{0}]/td[{1}]/div/a/span"