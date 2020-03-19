# 给定一个字符串，然后判断改字符串的长度。

# 实例1：使用内置方法len()
str = "runoob"
print(len(str))

# 实例2：使用循环计算
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter
str = "runoob"
print(findLen(str))

# 实例3
def length(src):
    # 字符串长度
    count = 0
    all_str = src[count:]

    for x in all_str:
        count += 1

    print("字符串长度为: %s" % count)

src = "Runoob"
length(src)