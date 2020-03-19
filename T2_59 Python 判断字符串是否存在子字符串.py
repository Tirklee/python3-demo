# 给定一个字符串，然后判断指定的子字符串是否存在于改字符串中。
#
# 实例

def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("不存在！")
    else:
        print("存在！")


string = "www.runoob.com"
sub_str = "runoob"
check(string, sub_str)


# 实例
string = "www.runoob.com"
sub_str ="runoob"
if sub_str in string:
    print('存在')
else:
    print('不存在')