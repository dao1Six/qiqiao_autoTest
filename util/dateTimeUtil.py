# encoding = utf-8
import datetime
from datetime import timedelta

class DateTimeUtil(object):
    '''时间处理类'''


    def Get_CurrentWeek_AllDays(self):
        '''获取本周所有的日期'''
        now = datetime.datetime.now().date()
        list = []
        for i in range(7):
            day = str(now - timedelta(days=now.weekday() - i))
            list.append(day)
        return list

    def Get_CurrentWeek_Days_UntilNow(self):
        '''获取本周至今所有的日期'''
        now = datetime.datetime.now().date()
        list = []
        for i in range(now.weekday()):
            day = str(now - timedelta(days=now.weekday() - i))
            list.append(day)
        return list

