# coding=utf-8

import datetime
from datetime import timedelta

now = datetime.datetime.now().date()

# 今天
today = now

# 昨天
yesterday = now - timedelta(days=1)

# 明天
tomorrow = now + timedelta(days=1)

# 本周第一天和最后一天
this_week_start = now - timedelta(days=now.weekday())
print(now.weekday())

this_week_end = now + timedelta(days=6 - now.weekday())
list = []
for i in range(7):
    day = str(now - timedelta(days=now.weekday()-i))
    list.append(day)


print(list)