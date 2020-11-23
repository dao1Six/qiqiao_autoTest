# coding=utf-8
import datetime
import time
from concurrent.futures.thread import ThreadPoolExecutor

import threadpool

import threading
import time
import unittest
from public import function

import os

# # 获取路径

from public.HTMLTestRunner_cn import HTMLTestRunner
from util.fileUtil import FileUtil
from util.summaryReport import SummaryReport

ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"
# 报告目录
reportpath = ProjectRootPath + "\\report\\qiqiao"
if not os.path.exists(reportpath): os.mkdir(reportpath)
testcase_path = ProjectRootPath + "\\testcase"  # 用例库目录


# 用例目录
def add_case_path():
    ''''''
    case_path_List = []
    testAppNameList = FileUtil().traversalDir_FirstDir(testcase_path)  # 获取测试一级目录名，返回列表
    for FirstDir in testAppNameList:
        case_path_List.append(testcase_path + "\\" + FirstDir)
    return case_path_List,testAppNameList


def add_case( case_path,rule="test_00*.py" ):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=testcase_path)
    return discover


def run_case( reportpathName,case_path ):
    print(threading.currentThread().name+"正在测试"+reportpathName)
    fp = open(reportpath + "\\%s.html" % reportpathName,"wb")
    runner = HTMLTestRunner(title="七巧测试报告",description="1.4.5版本灰度环境测试",stream=fp,verbosity=2,retry=1,save_last_try=True)
    # 执行测试用例
    runner.run(add_case(case_path))
    fp.close()
    filename = reportpath + "\\%s.html" % reportpathName
    function.send_HtmlFileEmail(filename,reportpathName + "应用测试报告")


def runThread( Threads ):
    '''多线程执行用例'''
    func_var = []
    case_path_List = add_case_path()[0]  # 用例目录
    testAppNameList = add_case_path()[1]  # app名
    # 生成多个列表
    for c,f in zip(case_path_List,testAppNameList):
        list = [f,c]
        func_var.append((list,None))
    # 定义了一个线程池，最多创建Threads个线程
    pool = threadpool.ThreadPool(Threads)
    # 创建要开启多线程的函数，以及函数相关参数和回调函数，其中回调数可以不写，default是none
    requests = threadpool.makeRequests(run_case,func_var)
    # 将所有要运行多线程的请求扔进线程池
    [pool.putRequest(req) for req in requests]
    pool.wait() #阻碍主线程运行


if __name__ == "__main__":
    time1 = datetime.datetime.now()
    start_time = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
    # runThread(5)
    time2 = datetime.datetime.now()
    end_time = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
    info = SummaryReport().summaryReportInfo()
    function.send_TextEmail("七巧测试汇总报告",'开始时间：' + start_time + '    结束时间：' + end_time + "   总耗时：" + str(time2 - time1)+"\n"+info)




