# coding=utf-8
from public.selenium_page import SeleniumPage


class MbReportComponent(SeleniumPage):

    chart_title = "div.dyReport div.chart_title>span.title"


    #获取所有的报表组件名称
    def GetAllChartTitle( self ):
        chart_titles = []
        chartElems = self.find_elemsByCSS_presence(self.chart_title)
        for chartElem in chartElems:
            chart_titles.append(chartElem.text)
        return chart_titles