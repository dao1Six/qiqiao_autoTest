# encoding = utf-8
import os

from bs4 import BeautifulSoup
from public import function
from util.fileUtil import FileUtil


class SummaryReport(object):
    '''汇总报告'''

    ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"
    # 报告目录
    reportpath = ProjectRootPath + "\\report\\qiqiao"
    testcase_path = ProjectRootPath + "\\testcase"  # 用例库目录
    testAppNameList = FileUtil().traversalDir_FirstDir(testcase_path)  # 获取测试一级目录名，返回列表


    def summaryReportInfo( self ):
        '''汇总报告信息'''
        files = os.listdir(self.reportpath)  # 得到文件夹下的所有文件名称
        pathList = []
        for file in files:
            pathList.append(self.reportpath+"\\"+file)
        all = 0
        skiped = 0
        errored = 0
        failed =0
        passed = 0
        errorApp = []
        for fileName,filePath in zip(self.testAppNameList,pathList):
            htmlfile = open(filePath,'rb')
            htmlcontent = htmlfile.read()
            bs = BeautifulSoup(htmlcontent,"html.parser")
            curAppall = int(bs.find('a',attrs={"class" :"all detail_button"}).get_text()[3:-1])
            all = all+curAppall
            curAppskiped = int(bs.find('a',attrs={"class" :"skiped detail_button"}).get_text()[3:-1])
            skiped = skiped+curAppskiped
            curApperrored = int(bs.find('a',attrs={"class" :"errored detail_button"}).get_text()[3:-1])
            errored = errored+curApperrored
            curAppfailed = int(bs.find('a',attrs={"class" :"failed detail_button"}).get_text()[3:-1])
            failed = failed+curAppfailed
            curApppassed = int(bs.find('a',attrs={"class": "passed detail_button"}).get_text()[3:-1])
            passed = passed+curApppassed
            if(curApperrored>0 or curAppfailed>0):
                errorApp.append(fileName)
        passedPercent = str('{:.2%}'.format(passed/all))
        return ("本次覆盖: "+str(len(files))+"个应用。\n"
                                       "总条数为"+str(all)+"\n"
                +"通过: "+str(passed)+"条"+"\n"
                +"失败: "+str(failed)+"条"+"\n"
                +"错误: "+str(errored)+"条"+"\n"
        +"跳过: "+str(skiped)+"条"+"\n"
                +"通过率为: "+passedPercent+"\n"
                +"以下应用测试在过程中有用例执行错误或失败的情况: \n"+';\n'.join(errorApp))


if __name__ == '__main__':
    info = SummaryReport().summaryReportInfo()
    function.send_TextEmail("七巧测试汇总报告",info)




