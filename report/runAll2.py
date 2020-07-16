# coding=utf-8
import threading
import time
import unittest
from public import function

import os

# # 获取路径

from public.HTMLTestRunner_cn import HTMLTestRunner
from util.fileUtil import FileUtil

ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"
# 报告目录
reportpath = ProjectRootPath + "\\report"
if not os.path.exists(reportpath): os.mkdir(reportpath)
testcase_path = ProjectRootPath + "\\testcase"

# 用例目录
def add_case_path():
    case_path_List = []
    FirstDirList = FileUtil().traversalDir_FirstDir(testcase_path)
    for FirstDir in FirstDirList:
        case_path_List.append(testcase_path+"\\"+FirstDir)
    return case_path_List,FirstDirList



def add_case(case_path, rule="test_00*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                   top_level_dir=testcase_path)
    return discover


def run_case(reportpathName,case_path):
    print('当前线程的名字是： ',threading.current_thread().name)
    fp = open(reportpath + "\\%s.html" %reportpathName, "wb")
    runner = HTMLTestRunner(title="七巧测试报告", description="1.4.5版本灰度环境测试", stream=fp, verbosity=2,retry=1, save_last_try=True)
    # 执行测试用例
    runner.run(add_case(case_path))
    fp.close()
    filename = reportpath + "\\%s.html" %reportpathName
    function.send_mail(filename)




if __name__ == "__main__":
    start_time = time.time()
    print('这是主线程：',threading.current_thread().name)
    threads = []
    case_path_List = add_case_path()[0]
    FirstDirList = add_case_path()[1]
    for c,f in zip(case_path_List,FirstDirList):
        t = threading.Thread(target=run_case,args=(f,c))
        threads.append(t)
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    print('主线程结束！' , threading.current_thread().name)
    print('一共用时：', time.time()-start_time)
