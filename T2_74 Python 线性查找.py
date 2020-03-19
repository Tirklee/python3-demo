# 线性查找指按一定的顺序检查数组中每一个元素，直到找到所要寻找的特定值为止。
#
#
#
# 实例


def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i;
    return -1;


# 在数组 arr 中查找字符 D
arr = ['A', 'B', 'C', 'D', 'E'];
x = 'D';
n = len(arr);
result = search(arr, n, x)
if (result == -1):
    print("元素不在数组中")
else:
    print("元素在数组中的索引为", result);




def LinearSearch(list):
    num = int(input('Number:\t'))
    counter = 0
    null = 0

    for i in list:
        if i == num:
            print('Find number {} in place {}.'.format(num, counter))
        else:
            null += 1
        counter += 1
    if null == counter:
        print('Don\'t find it.')

list = [1, 2, 5, 7, 8, 34, 567, -1, 0, -1, -3, -9, 0]
LinearSearch(list)



def LinearSearch(num=50):
    import random
    random.seed(888)
    data = []
    for i in range(15):
        data.append(random.randint(1, 100))
    data.sort()
    print(data)
    for i in range(0,len(data)):
        if data[i]==num:
            print(i)
            break
    else:
        print('查无此数')
LinearSearch()