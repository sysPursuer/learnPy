
d = {'Mickle':93,'Bob':43,34:90}
#如果关键字在d中则True否则False,两种方法
if('Thomas' in d):
	print("True\n")
else:
	print("False\n")
#get方法，默认放回None
print(d.get(33))
print(d.get(33,-1))


#修改value
d[34] = 94
print(d[34])

#删除dict中的元素
d.pop(34)
print(d)

#增加元素
d['Tom'] = 88
print(d)

#dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，
#那dict内部就完全混乱了，这个通过key计算位置的算法称为2Hash,要保证hash正确性
#作为Key的对象就不能变，所以list不能作为key