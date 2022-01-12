# 可变 和 不可变

# 不可变： 对象所指向的内存中的值是不可以改变

# 不可变的类型： int  str  float  元组tuple   frozenset()

num = 10

s1 = 'abc'
print(id(s1))

s1 = 'abcd'
print(id(s1))


t1 = (3, 5, 6)

print(id(t1))

t1 = (3, 5)

print(id(t1))


# 可变的:对象所指向的内存中的值是可以改变 

# 可变类型: 字典dict  列表list  集合set   扩展： frozenset() 不可变

list1 = [1, 2, 3, 4, 5]
print(list1, id(list1))

list1.pop()
print(list1, id(list1))


dict1 = {1: 'aa', 2: 'bb'}
print(dict1, id(dict1))

dict1.pop(1)
print(dict1, id(dict1))


'''
  集合 是可变的还是不可变的？

'''

set1 = {3, 5, 6, 8}

print(set1, id(set1))

set1.discard(5)
print(set1, id(set1))


fset = frozenset(set1)  # {3,6,8}

print(fset, id(fset))

fset = frozenset({3, 6})
print(fset, id(fset))


