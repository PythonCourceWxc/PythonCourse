'''
 str()
 int()
 len()
 list()
 sorted()
 print()
 input()
 enumerate():函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列

'''

# l1= ['a','abc','jk','opop']

# for value in l1:
# 	print(value)

# # enumerate(l1) ---> index value 

# for index,value in enumerate(l1):
# 	print(index,value)


# for index,value in enumerate('happy'):
# 	print(index,value)


# 算法
# 冒泡排序

numbers = [8, 5, 9, 7]
# numbers = sorted(numbers)
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

# 自定义排序方法
# 选择排序( 每次找一个固定的元素，跟后面的元素依次进行比较，每次比较找出一个最小值放到最前面，依次类推 )

# 2，4,7,9,

for i in range(len(numbers)):
    # numbers[i] = 5
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            # 快速交换
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(numbers)

# 降序排列
for i in range(len(numbers)):
    # numbers[i] =5
    for j in range(i + 1, len(numbers)):
        if numbers[i] < numbers[j]:
            # 快速交换
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(numbers)
