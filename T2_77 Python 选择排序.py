# 选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。
# 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，
# 再从剩余未排序元素中继续寻找最小（大）元素，
# 然后放到已排序序列的末尾。
# 以此类推，直到所有元素均排序完毕。

# 实例
import sys

A = [64, 25, 12, 22, 11]

for i in range(len(A)):

    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

print("排序后的数组：")
for i in range(len(A)):
    print("%d" % A[i])


"""选择排序
Selectionsort.py"""

# 以序号为依据
def Selectionsort1():
    A = [-9, -8, 640, 25, 12, 22, 33, 23, 45, 11, -2, -5, 99, 0]
    for i in range(len(A)):
        min = i
        for j in range(i + 1, len(A)):  # 上一个值右边的数组
            if A[min] > A[j]:  # 使min为最小值，遇到比min小的值就赋值于min
                min = j

        A[i], A[min] = A[min], A[i]  # 交换最小值到左边

    print ('Selectionsort1排序后的数组：', A)

# 简单的方法更好用，简单的问题也不容易发现。第二个函数的交换位置我想了很久。
# 以数值为依据
def Selectionsort2():
    A = [-9, -8, 640, 25, 12, 22, 33, 23, 45, 11, -2, -5, 99, 0]
    counter = 0  # 记录循环次数和位置
    array = []

    for i in A:
        counter += 1
        for j in A[counter:]:  # 缩小范围
            if i > j:  # 使i为最小值
                i = j

            A.remove(i)
            A.insert(counter - 1, i)
            # 把最小值置于列表左边，避免重复比较

        array.append(i)

    print('Selectionsort2排序后的数组：', array)

Selectionsort1()
Selectionsort2()

# 可选择升序和降序。

#待排序数组arr，排序方式order>0升序，order<0降序
def selectSort(arr,order):
    rborder = len(arr)
    for i in range(0,rborder):
        p = i
        j = i+1
        while(j<rborder):
            if((arr[p]>arr[j]) and (int(order)>0)) or ((arr[p]<arr[j]) and (int(order)<0)):
                p = j
            j += 1
        arr[i], arr[p] = arr[p], arr[i]
        i += 1
    return arr

A = [64, 25, 12, 22, 11]
print(selectSort(A, -1))
print(selectSort(A, 1))