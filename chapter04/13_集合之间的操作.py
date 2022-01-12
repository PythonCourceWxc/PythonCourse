'''
  1. 产生10个1~20的随机数，去除里面的重复项
  2. 键盘输入一个元素，将此元素从不重复的集合中删除

'''

import random 

# list1= []

# # set1 = set()

# for i in range(10):
# 	ran = random.randint(1,20)
# 	list1.append(ran)   # [3,5,8,1,1]


# # set1.update(list1)  # {3,5,8,1}.update([3,5,8,1,1])
# set1 =set(list1)

# print(list1)
# print(set1)


# num = int(input('输入一个数字:'))


# set1.discard(num)

# print('删除之后结果:',set1)



# 方式二：
# set1= set()

# for i in range(10):
# 	ran = random.randint(1,20)
# 	set1.add(ran)

# print(set1)


# num = int(input('输入一个数字:'))

# set1.discard(num)

# print('删除之后结果:',set1)



# 其他：符号操作
# print(6 in set1)

set2 = {2, 3, 4, 5, 6}
set3 = {2, 3, 4, 5, 6, 7, 8}

print(set2 == set3)  # 判断两个集合中的内容是否相等

# 测试： print(set2 != set3) ??

# （+  * 不支持）   -  &  |

# set4 = set2+set3
# print(set4)


# set5= set2*2
# print(set5)

set4 = set3-set2   # 差集  difference()
print(set4)


set5 = set3.difference(set2)
print(set5)



# &  交集   intersection()  

set6 = set3 & set2
print(set6)

set7 = set3.intersection(set2)

print(set7)


# |  并集  union()  联合

set8 = set3 | set2

print(set8)


set9 = set3.union(set2)

print(set9)

'''
已知两个列表:
l1 = [5,1,2,9,0,3]
l2 = [7,2,5,7,9]

找出两个列表的不同元素

找出两个列表的共同元素



'''