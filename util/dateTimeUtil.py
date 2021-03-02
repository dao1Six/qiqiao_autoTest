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
        for i in range(now.weekday()+1):
            day = str(now - timedelta(days=now.weekday() - i))
            list.append(day)
        return list

    def Tomorrow( self ):
        '''返回明天日期'''
        now = datetime.datetime.now().date()
        tomorrow = now + timedelta(days=1)
        return str(tomorrow)

    def Today( self ):
        '''返回今天日期'''
        now = datetime.datetime.now().date()
        return str(now)

    def Yesterday( self ):
        '''返回昨天日期'''
        now = datetime.datetime.now().date()
        yesterday = now - timedelta(days=1)
        return str(yesterday)

    def LastMonth( self ):
        '''返回上个月'''
        today=datetime.date.today()
        first=today.replace(day=1)
        last_month=first - datetime.timedelta(days=1)
        valueList=str(last_month).split("-")
        return valueList[0]+"-"+valueList[1]

    def LastYear( self ):
        '''返回上一年'''
        now=datetime.datetime.now()
        last_year=int(now.year) - 1
        return str(last_year)

    def CurrentHM( self ):
        '''返回时分'''
        return datetime.datetime.now().strftime('%H:%M')





if __name__ == '__main__':
    d = DateTimeUtil()
    print(d.CurrentHM())