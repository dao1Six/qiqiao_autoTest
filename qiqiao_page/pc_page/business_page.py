# coding=utf-8
from functools import singledispatch

from qiqiao_page.pc_page.business_components.kanbanView_components import KanBanComponent
from qiqiao_page.pc_page.business_components.list_components import ListComponent
from qiqiao_page.pc_page.public_page import PublicPage


class BusinessPage(PublicPage,ListComponent,KanBanComponent):
    '''PC业务建模页面'''

    left_bar_menu_loc = "//span[@data-mark='left_bar_%s']" #左侧菜单元素
    breadcrumb_item_loc = "//span[@class='el-breadcrumb__inner is-link' and text()='全部应用']"

    def BusinessPage_LeftMenu_Click( self,menu):
        '''点击左侧菜单'''
        self.clickElemByXpath_visibility(self.left_bar_menu_loc.replace('%s',menu))


    def BusinessPage_HeardItem_AllApp_Click( self ):
        '''点击全部应用选项'''
        self.clickElemByXpath_visibility(self.breadcrumb_item_loc)

    def BusinessPage_LeftMenu_isExist( self,menu ):
        '''判断是否存在此菜单'''
        elem = self.find_elemByXPATH_presence(self.left_bar_menu_loc.replace('%s',menu))
        if(elem==None):
            return False
        else:
            return True




