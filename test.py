# coding=utf-8

import datetime
from datetime import timedelta

now = datetime.datetime.now().date()

# 今天
today = now

# 昨天
yesterday = now - timedelta(days=1)

# 明天
tomorrow = now + timedelta(days=2)

print(str(tomorrow))