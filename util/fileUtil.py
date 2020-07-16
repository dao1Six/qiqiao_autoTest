# coding=utf-8
import os.path

class FileUtil(object):

    def traversalDir_FirstDir(self,path ):
        '''获取路径下的下一级目录名'''
        list = []
        # 判断路径是否存在
        if (os.path.exists(path)):
            # 获取该目录下的所有文件或文件夹目录
            files = os.listdir(path)
            for file in files:
                # 得到该文件下所有目录的路径
                m = os.path.join(path,file)
                # 判断该路径下是否是文件夹
                if (os.path.isdir(m)):
                    h = os.path.split(m)
                    list.append(h[1])
        return list

if __name__ == '__main__':
    FileUtil().traversalDir_FirstDir("D:\\pythonwork\\wujianlunTeam\\qiqiao_autoTest\\testcase")