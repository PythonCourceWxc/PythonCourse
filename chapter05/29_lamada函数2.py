# map

list1 = [3, 4, 6, 7, 8, 9, 9, 0, 2, 5]

result = map(lambda x: x + 2, list1)
print(list(result))

# for index,i in enumerate(list1):
#     list1[index]=i+2

func = lambda x: x if x % 2 == 0 else x + 1

result = func(5)
print(result)

# 对列表中的奇数进行加1操作
result = map(lambda x: x if x % 2 == 0 else x + 1, list1)
print(list(result))

# for index, i in enumerate(list1):
#     if i % 2 != 0:
#         list1[index] = i + 1
#
# print(list1)


# reduce(): 对列表中的元素进行加减乘除运算的函数
from functools import reduce

tuple1 = (3, 5, 7, 8, 9, 1)

result = reduce(lambda x, y: x + y, tuple1)

print(result)

tuple2 = (1, 2, 3)

result = reduce(lambda x, y: x - y, tuple2, 10)
print(result)

# 动手测试减法
list1 = [12, 6, 8, 98, 34, 36, 2, 8, 0]

result = filter(lambda x: x > 10, list1)

print(list(result))

print(list1)

# def func(list1):
#     list2 = []
#     for i in list1:
#         if i > 10:
#             list2.append(i)
#     return list2


students = [
    {'name': 'tom', 'age': 20},
    {'name': 'lucy', 'age': 19},
    {'name': 'lily', 'age': 13},
    {'name': 'mark', 'age': 21},
    {'name': 'jack', 'age': 23},
    {'name': 'steven', 'age': 18},
]

# 找出所有年龄大于20岁学生

result = filter(lambda x: x['age'] > 20, students)
print(list(result))


# 按照年龄从小到大排序

students = sorted(students, key=lambda x: x['age'], reverse=True)

print(students)

'''
max()  
min()
sorted()

map(): 
reduce()
filter()  


'''