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