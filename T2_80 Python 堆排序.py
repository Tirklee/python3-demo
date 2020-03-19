# 堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
# 堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：
# 即子结点的键值或索引总是小于（或者大于）它的父节点。
# 堆排序可以说是一种利用堆的概念来排序的选择排序。
#
# 实例


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("排序后")
for i in range(n):
    print("%d" % arr[i])

# 改进参考代码：
#
# 1、迭代堆化
#
# 2、迭代的两种写法

def heapify(arr):
    n = len(arr)
    for i in reversed(range(n // 2)):
        shiftDown(arr,n,i)

def shiftDown(arr, n, k):
    while 2 * k + 1 < n:
        j = 2 * k + 1
        if j + 1 < n and arr[j + 1] < arr[j]:
            j += 1
        if arr[k] <= arr[j]:
            break
        arr[k], arr[j] = arr[j], arr[k]
        k = j

def shiftDown2(arr, n, k):
    smallest, l, r = k, 2 * k + 1, 2 * k + 2
    while l < n:
        if arr[l] < arr[smallest]:
            smallest = l
        if r < n and arr[r] < arr[smallest]:
            smallest = r
        if smallest == k:
            break
        else:
            arr[k], arr[smallest] = arr[smallest], arr[k]
            k = smallest
            l, r = 2 * k + 1, 2 * k + 2

def heapSort(arr):
    n=len(arr)
    heapify(arr)
    print("堆化：",arr)
    for i in range(n-1):
        arr[n-i-1],arr[0] = arr[0],arr[n-i-1]
        # print("交换最小值后：",arr)
        shiftDown(arr,n-i-1,0)
        # print("调整后：",arr)


arr = [3,2,1,9,7,8]
heapSort(arr)
print("排序后：",arr)