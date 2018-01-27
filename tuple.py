classmates = ('Michael', 'Bob', 'Tracy',[1,2])
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
classmates[3][0] = 3
print(classmates[3][0],classmates[3][1])
# cannot modify tuple:
#classmates[0] = 'Adam'
#表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
#tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，
#tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，
#就不能改成指向其他对象，但指向的这个list本身是可变的！