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

#可变参数	两种实现方式，两种调用方式（实质上是函数内部自动组装成list或tuple）
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



#关键字参数，实质上是函数内部自动组装成dict词典
def person(name,age,**kw):
	print("name:",name,"age:",age,"other:",kw)

extra = {'city:':'Beijing','job':'Engineer'}
person('Tom',22,**extra)
person('Tom',22,city='Beijing',job='Engineer')

#命名关键字参数：对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数
#如果要限制关键字参数的名字，就可以用命名关键字参数
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def Person(name,age,*,city,job):
	print(name,age,city,job)
#Person('Jack',21,city='Shanghai')	如果没有传入参数名或者缺少参数名，会报错
#命名关键字参数可以有缺省值
Person('Jack',21,city='Shanghai',job='Programmer')

#使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
#如果缺少*，Python解释器将无法识别位置参数和命名关键字参数

