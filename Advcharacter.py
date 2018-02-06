#切片
L = [1,2,3,4,5,6,7,8,9,10]
print(L[:3])
print(L[1:3])
print(L[1:10:2])

############################################################################################

#迭代
r = []
for i in range(10):	#默认0-9
	r.append(i)
print(r)
#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
#默认情况下，dict迭代的是key。如果要迭代value，
#可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
for num in L:
	print(num+1)
d = {'a':1,'b':2,'c':3}
for key in d:
	print(key,':',d[key])
for value in d.values():
	print(value)
for k,v in d.items():
	print(k,':',v)
	
#如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance(123,Iterable))

###############################################################################################


#列表生成式 List Comprehensions
print(list(range(1,11)))	#区间[1,11)
l = []
for x in range(1,11):
	l.append(x * x)
print(l)
#列表生成式则可以用一行语句代替循环生成上面的list：
print([x*x for x in range(1,11)])

#两层循环,比如生成全排列
print([m+n for m in 'ABC' for n in 'XYZ'])
dic = {'a':'A','b':'B','c':'C'}
print([k+ '=' + v.lower() for k,v in dic.items()])

############################################################################################

#生成器 generator
#如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中
#不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。
#在Python中，这种一边循环一边计算的机制，称为生成器：generator。
g = (x*x for x in range(10))	
#第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
print(g)
for n in g:
	print(n)
#the second way函数实现
def fib(max):
	n,a,b = 0,0,1
	while n < max :
		yield b
		a,b = b,a+b
		n = n + 1
	return 'done'
#这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，
#那么这个函数就不再是一个普通函数，而是一个generator,在每次调用next()的时候执行，
#遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
for n in fib(10):
	print(n)
#for循环得不到generator语句的返回值，如果想得到，必须捕获StopIteration
#错误，返回值包含在StopIteration的value中
g = fib(6)
while True:
	try:
		x = next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value:',e.value)
		break
#迭代器 iterator
#作用于for循环的数据类型（iterable 可迭代对象）有：
#一类是集合数据类型，如list、tuple、dict、set、str等；
#一类是generator，包括生成器和带yield的generator function。

#判断是否为可迭代对象,可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
from collections import Iterator
print(isinstance((x for x in range(10)),Iterator))
print(isinstance('abc',Iterator))
#集合数据类型如list、dict、str等是Iterable但不是Iterator，
#不过可以通过iter()函数获得一个Iterator对象。
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

