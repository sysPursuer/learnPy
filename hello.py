
print("hello,python\n")
if 23>=0:
	print('Yes'," Bigger than zero\n")
	print('it\'s ok\n')

age = input("please input your age:")
age = int(age)
if(age >= 18):
	print("your age is ",age,"\n")
	print("Adult\n")
elif(age >= 6):
	print("your age is ",age,"\n")
	print("teenager\n")

age = 0
for x in range(100):
	age += x
print(age)