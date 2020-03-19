import calendar
calendar.setfirstweekday(firstweekday=6)    # 显示出一年 12 个月份的日历
while True:
    yy = int(input('input years:'))
    # mm = int(input('input month:'))
    for i in range(12):
        print(calendar.month(yy, i + 1))
        print('*' * 20)