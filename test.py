# coding=utf-8
import datetime
from time import strptime


class A():
    def ee( self ):
        ''''''

        print( datetime.datetime.today().weekday())
        print(datetime.date.today())
        print(datetime(*strptime('2011-03-08 0:27:41', '%Y-%m-%d %H:%M:%S')[0:6]).weekday() )

    def get_current_week(self):
        monday, sunday = datetime.date.today(), datetime.date.today()
        one_day = datetime.timedelta(days=1)
        while monday.weekday() != 0:
            monday -= one_day
        while sunday.weekday() != 6:
            sunday += one_day

        return monday, sunday



if __name__ == '__main__':
    A().ee()