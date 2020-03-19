# 十进制到二进制：

def dec2bin(num):
    l = []
    if num < 0:
        return '-' + dec2bin(abs(num))
    while True:
        num, remainder = divmod(num, 2)
        l.append(str(remainder))
        if num == 0:
            return ''.join(l[::-1])
# 十进制到八进制：

def dec2oct(num):
    l = []
    if num < 0:
        return '-' + dec2oct(abs(num))
    while True:
        num, remainder = divmod(num, 8)
        l.append(str(remainder))
        if num == 0:
            return ''.join(l[::-1])
# 十进制到十六进制：

base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
def dec2hex(num):
    l = []
    if num < 0:
        return '-' + dec2hex(abs(num))
    while True:
        num,rem = divmod(num, 16)
        l.append(base[rem])
        if num == 0:
            return ''.join(l[::-1])

# 十进制数转化成二进制数（float）

while True:
    number=input("请输入一个正数:(输入q退出程序）")
    if number in ['q','Q']:
        break
    elif not float(number)>0:
        print("请输入一个正数（输入q退出程序）：")
    else:
        number=float(number)
        array1=[]
        array2=[]
        integer=int(number)
        floa=number-integer
        while integer!=0:
            array1.append(integer%2)
            integer=integer//2
        else:
            array1.append(0)
        array1.reverse()
        while floa>0.00001:
            array2.append(int(2*floa))
            floa=floa*2-int(floa*2)
        else:
            array2.append(0)
        array1.append(".")
        array=array1+array2
        for x in array:
            print(x,end="")
        print("\n")