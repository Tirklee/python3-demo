# 给定一个时间戳，将其转换为指定格式的时间。
#
# 注意时区的设置。
#
# 当前时间
# 实例1
import time

# 获得当前时间时间戳
now = int(time.time())
# 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)

# 实例2
import datetime

# 获得当前时间
now = datetime.datetime.now()
# 转换为指定的格式
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)

# 实例3
import time

timeStamp = 1557502800
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)

# 实例4
import datetime

timeStamp = 1557502800
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)
