s1 = set([1,2,3,4,5,3,])
s2 = set([3,4,6])
print(s1,s2)
print(s1&s2)
print(s1|s2)

#增加删除元素
s1.add(34)
print("s1:",s1)
if(34 in s1):
	print("34 is in s1")
	s1.remove(34)
	
#与str比较
a = 'abc'
b = a.replace('a','A')
print('a:',a)
print('b:',b)
#a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，
#但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'
#当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，
#而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
#相反，replace方法创建了一个新字符串'Abc'并返回