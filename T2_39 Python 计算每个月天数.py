#!/usr/bin/python3
# author by : www.runoob.com

import calendar

monthRange = calendar.monthrange(2016, 9)
print(monthRange)

# 若只是想知道每个月的天数，可用：

# >>> calendar.mdays
[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 实例：
import calendar
print(calendar.mdays[9])