#max函数:可以接受任意多的参数并返回最大值
l = [23,3,56,98]
print(max(l))
print(max(23,233,34))

#abs函数：参数的个数或者数据类型不对会报TypeError
#abs(12,12),abs('a')
print(abs(-23.4))

#数据类型转换，比如int()函数可以将其他数据类型转换为整数
print(int(12.34))
s = '345'
print(int(s))
s = '23.333'
print(float(s))
print(str(21.22))
print(bool(2))
print(bool(''))

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，
#相当于给这个函数起了一个“别名”
a = abs
print(a(-1))

#hex函数将整数转为16进制数
print(hex(23333))