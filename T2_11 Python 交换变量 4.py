# 异或形式：

#交换变量
x = int(input('输入 X 值：'))
y = int(input('输入 Y 值：'))
x = x ^ y
y = x ^ y
x = x ^ y
print('交换后的 X 值为：',x)
print('交换后的 Y 值为：',y)