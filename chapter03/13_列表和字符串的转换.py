'''
字符串中可以使用的符号:
+
*
in
not in
is
not is
[]
'''

'''
列表支持的符号:
+  
* 
in

'''

l1 = [1, 2, 3]
l2 = [5, 6, 7]

l3 = l1+l2
print(l3)


l4 = [5, 8] * 3
print(l4)


result = 3 in [1, 2, 3, 4]
print(result)

'''
列表中的元素:
整型
字符串类型
浮点型
列表
元组
字典
对象

[[...],[...],[....],[....]]

'''
# [3] in [1, 2, 3, 4]

result = [3, 2] in [1, 2, [3, 2, 1], 4, 5]
print(result)

# [1,2,3,'aa','bb',[1,2],[6,8,9,0]] 

# [[1,2],[6,8,9,0]]  # 二维


l5 = [[1, 2], [3, 2, 1], [4, 5], [7, 3, 1]]

print(len(l5))  # 3

e = l5[2]
print(e, type(e))  # [4,5]

print(e[1])


print(l5[1][1])

print(l5[3][1])


# list(range(1, 10, 3))


print(range(1, 10, 3)) # 1,4,7
'''
类型转换:
str()  
int()
list()  将指定的内容转成列表,可迭代的内容可以放到list中。

s= 'abc'
result = list(s)  # ['a','b','c']

iterable 可迭代的  for...in里面可以循环就是可迭代的

'abcdef' ---> a b c   

for i in range(5):
	pass


'''
print(list(range(1, 10, 3)))  # []

s = 'abc'
result = list(s)

print(result)

# result = list(10)  # int obj is not iterable  
# print(result)

print(list(range(10, 1, -3)))

print(list(range(5)))

# print(int([4,5]))
print(int('45'))

x = "abc"
y = "def"
z = ["d", "e", "f"]

print(x.join(y))
print(x.join(z))