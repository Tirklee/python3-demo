# 不使用临时变量:

# -*- coding: UTF-8 -*-

# 用户输入
x = int(input('输入 x 值: '))
y = int(input('输入 y 值: '))

x = x + y
y = x - y
x = x - y

print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))