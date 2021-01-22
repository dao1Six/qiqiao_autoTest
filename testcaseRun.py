# coding=utf-8
import datetime
import time
from concurrent.futures.thread import ThreadPoolExecutor

import threadpool

import threading
import time
import unittest
from public import function
import HtmlTestRunner
from util.fileUtil import FileUtil
from util.summaryReport import SummaryReport
import os

from testcase.process_app.pc_testcase.test_001 import ProcessAppTest_001
from testcase.value_app.pc_testcase.test_001 import ValueAppTest_001
from testcase.achievement_app.pc_testcase.test_001 import AchievementAppTest_001
from testcase.dataFilter_app.pc_testcase.test_001 import DataFilterAppTest_001

ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"
# 报告目录
reportpath = ProjectRootPath + "\\report\\qiqiao"
if not os.path.exists(reportpath): os.mkdir(reportpath)
testcase_path = ProjectRootPath + "\\testcase"  # 用例库目录



def add_case():
    '''加载所有的测试用例'''
    suite=unittest.TestSuite()
    loader=unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(DataFilterAppTest_001))
    suite.addTest(loader.loadTestsFromTestCase(ProcessAppTest_001))
    suite.addTest(loader.loadTestsFromTestCase(ValueAppTest_001))
    return suite



def run_case():
    '''运行测试用例'''
    runner = HtmlTestRunner.HTMLTestRunner(report_name=reportpath+ "\\xxxxx.html")
    # 执行测试用例
    runner.run(add_case())



if __name__ == "__main__":
    time1 = datetime.datetime.now()
    start_time = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
    print("开始时间："+start_time)
    run_case()
    time2 = datetime.datetime.now()
    end_time = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
    print("结束时间：" + end_time)
