# coding=utf-8
import time
import unittest

import os

# # 获取路径
# from BeautifulReport import BeautifulReport
from public import function, HTMLTestRunner_jpg
from public.HTMLTestRunner_cn import HTMLTestRunner


from report.reportRunner import Report


if __name__ == '__main__':

    ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"
    # 报告目录
    reportpath = ProjectRootPath + "\\report"
    if not os.path.exists(reportpath): os.mkdir(reportpath)


    # 用例目录
    case_path = ProjectRootPath + "\\testcase\\pom_app"
    # discover = unittest.defaultTestLoader.discover(case_path, pattern='test_00*.py')
    discover = unittest.defaultTestLoader.discover(case_path,pattern='test_00*.py')
    # discover = unittest.defaultTestLoader.discover("../testcase/dataFilter_app", pattern='test_001.py')


    fp = open(reportpath + "\\result.html", "wb")
    # runner = HTMLTestRunner_jpg.HTMLTestRunner(title="七巧测试报告",description="测试用例参考",stream=fp,verbosity=2,retry=0)
    runner = HTMLTestRunner(title="七巧测试报告", description="1.4.5版本灰度环境测试", stream=fp, verbosity=2,
                   retry=1, save_last_try=True)
    # 执行测试用例
    runner.run(discover)
    fp.close()

    #生产xml报告用这个 跟tapd对接
    # reportRunner = Report ()
    # reportRunner.run_suite_output_xml_report (discover)

    #更漂亮的报告模板就是发邮件不兼容
    # result = BeautifulReport(discover)
    # result.report(filename='result', description='测试deafult报告', report_dir=reportpath, theme='theme_default')

    filename = reportpath+"\\result.html"
    function.send_mail(filename,'七巧测试报告')








