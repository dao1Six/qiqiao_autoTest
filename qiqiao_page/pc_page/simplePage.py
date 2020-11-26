from qiqiao_page.pc_page.business_components.kanbanView_components import KanBanComponent
from qiqiao_page.pc_page.business_components.list_components import ListComponent
from qiqiao_page.pc_page.public_page import PublicPage


class SimplePage(PublicPage,ListComponent,KanBanComponent):
    '''PC业务建模简单页面'''