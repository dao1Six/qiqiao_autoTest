# coding=utf-8
import time
import unittest

import os

# # 获取路径
from BeautifulReport import BeautifulReport
from public import function
from report.reportRunner import Report


if __name__ == '__main__':

    ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"
    # 报告目录
    reportpath = ProjectRootPath + "\\report"
    if not os.path.exists(reportpath): os.mkdir(reportpath)


    # 用例目录
    case_path = ProjectRootPath + "\\testcase"

    discover = unittest.defaultTestLoader.discover("../testcase", pattern='test_*.py')

    result = BeautifulReport(discover)
    result.report(filename='测试报告', description='测试deafult报告', report_dir=reportpath, theme='theme_default')

    filename = reportpath+"\\测试报告.html"

    function.send_mail(filename)


    #生产xml报告用这个
    # reportRunner = Report ()
    # reportRunner.run_suite_output_xml_report (discover)




