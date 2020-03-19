# 给定一个字符串，然后移除制定位置的字符：
#
# 实例
test_str = "Runoob"

# 输出原始字符串
print("原始字符串为 : " + test_str)

# 移除第三个字符 n
new_str = ""

for i in range(0, len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]

print("字符串移除后为 : " + new_str)


test_str = "Runoob"
new_str = test_str.replace(test_str[3], "", 1)
print(new_str)

str = 'Runoob'
'''
@param str 原字符串
@paramnum 要移除的位置
@return 移除后的字符串
'''
def ff(str,num):
    return str[:num] + str[num+1:];
print(ff(str,2));
print(ff(str,4));
