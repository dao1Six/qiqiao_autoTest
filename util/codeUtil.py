#字符编码，解码
from urllib import parse


class CodeUtil():


    #字符编码
    @classmethod
    def code_quote(cls,str):
        '''字符串转码'''
        return parse.quote (str)



    #字符解码
    @classmethod
    def code_unquote(cls,code):
        '''解码'''
        return parse.unquote (code)