# 冒泡排序（Bubble Sort）也是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，
# 如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，
# 也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端。

# 实例


def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i])




# 参考：

"""冒泡排序
Bubblesort.py"""

from random import randrange, shuffle

def Bubblesort():
    array = []

    while len(array) < 12:  # 范围内随机取12个数值
        array.append(randrange(-99, 101, 3))
    shuffle(array)  # 打乱数组

    print('排序前数组：{}'.format(array))

    for i in range(12):
        for j in range(11 - i):
            if array[j] > array[j + 1]:  # 遇到较小值前后交换
                array[j], array[j + 1] = array[j + 1], array[j]

    print('排序后数组：{}'.format(array))

Bubblesort()


# 可选择升序和降序。

#可选升降序的冒泡排序, order>0升序，order<0降序

def bubbleSort(arr,order):
    max = len(arr)
    for i in range(0, max):
        j = 1
        while(j<max-i):
            if((arr[j-1]>arr[j]) and (int(order)>0)) or ((arr[j-1]<arr[j]) and (int(order)<0)):
                arr[j-1], arr[j] = arr[j], arr[j - 1]
            j += 1
        i += 1
    return arr


A = [64, 25, 12, 22, 11]
print(bubbleSort(A, -1))
print(bubbleSort(A, 1))