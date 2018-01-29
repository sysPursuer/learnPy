def my_abs(x):
	if not isinstance(x,(int,float)):		#参数检查
		raise TypeError('bad operand type')
	if(x>=0):
		return x
	else:
		return -x

print(my_abs(-90))

import math

def move(x,y,step,angle=0):
	nx = x + step*math.cos(angle)
	ny = y + step*math.sin(angle)
	return nx, ny
	
x, y = move(100,100,60,math.pi / 6)
print(x,y)
t = move(100,100,60,math.pi / 6)
print(t)

def quardratic(a,b,c,x):
	return a*x*x+b*x+c
	
print(quardratic(1,2,3,4))

#可变参数	两种实现方式，两种调用方式
def calc(numbers):
	sum = 0
	for n in numbers:
		sum += n*n
	return sum
def calcu(*numbers):
	sum = 0
	for n in numbers:
		sum += n*n
	return sum
print(calc([1,3]))
nums = [1,2,3]
print(calcu(1,2,3))
print(calcu(*nums))
#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

def person(name,age,**kw):
	print("name:",name,"age:",age,"other:",kw)

extra = {'city:':'Beijing','job':'Engineer'}
person('Tom',22,**extra)