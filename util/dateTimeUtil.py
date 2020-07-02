# encoding = utf-8
import datetime
from datetime import timedelta

class DateTimeUtil(object):
    '''时间处理类'''


    def Get_CurrentWeek_Days(self):
        '''获取本周的日期'''
        now = datetime.datetime.now().date()
        list = []
        for i in range(7):
            day = str(now - timedelta(days=now.weekday() - i))
            list.append(day)
        return list