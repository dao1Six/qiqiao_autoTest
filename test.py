import datetime
import time

time1 = datetime.datetime.now()
print(time1)
start_time = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
print('开始时间：',start_time)
time.sleep(2)
time2 = datetime.datetime.now()
end_time = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
print('结束时间：',end_time)
print(time2-time1)
