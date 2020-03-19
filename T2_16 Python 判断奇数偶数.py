# Filename : test.py
# author by : www.runoob.com

# Python 判断奇数偶数
# 如果是偶数除于 2 余数为 0
# 如果余数为 1 则为奇数

num = int(input("输入一个数字: "))
if (num % 2) == 0:
    print("{0} 是偶数".format(num))
else:
    print("{0} 是奇数".format(num))

# 优化加入输入判断:
while True:
    try:
        num=int(input('输入一个整数：')) #判断输入是否为整数
    except ValueError: #不是纯数字需要重新输入
        print("输入的不是整数！")
        continue
    if num%2==0:
        print('偶数')
    else:
        print('奇数')
    break

# 简洁就是美丽。
num = eval(input('Number:\n'))
print('{} is '.format(num) + ('even number.' if num % 2 == 0 else 'odd number.'))