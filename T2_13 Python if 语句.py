# 优化增加输入字符的判断以及异常输出:

while True:
    try:
        num=float(input('请输入一个数字：'))
        if num==0:
            print('输入的数字是零')
        elif num>0:
            print('输入的数字是正数')
        else:
            print('输入的数字是负数')
        break
    except ValueError:
        print('输入无效，需要输入一个数字')