# 拆包

t1 = (4, 7, 3)

# a,b =t1   # ValueError: too many values to unpack(拆包) (expected（希望，盼望） 2)
# x,y,z=(6,) #ValueError: not enough values to unpack (expected 3, got 1)

a, b, c = t1

print(a, b, c)

a = t1

print(a)


# 变量个数与元组个数不一致
t1 = (2, 5, 8, 9, 7)

a, *_, c = t1
print(a, c, _)


a, c, *_ = t1
print(a, c, _)

a, b, *c = t1
print(a, b, c)


t1 = (9, 4, 8, 6)

a, *b = t1
print(a, b)  # *b 表示未知个数0~n， 0-- []   多个元素的话 ~ [1,2,3,4,...]

print(*b)
'''
  字符串  x,y,*z = 'hello'  ---> x='h'  y='e'  z=['l','l','o']
  列表  x,y,*z =['aa',6,'hello','good','happy','lucky']  ---> x='aa'  y=6  z=['hello','good','happy','lucky']

'''

'''
 t1=(9,4,8,6)

'''

t1 = (9,)

x, *y = t1

print(x, y)  # 9,[]

# 添加元素
y.append('a')
y.append('b')
print(y)  # ['a','b']

print(*y)  # print()   print(4,8,6)  4 8 6

'''
元组：
1. 符号:(1,2,3)  tuple
2. 关键字:tuple
3. 元组的元素只能获取，不能增删改

符号:
+
*
is  not
in  not in 

系统函数：
max()
min()
sum()
len()
sorted()   ----> 排序，返回的结果就是列表
tuple()  ---->元组类型的强制转换

元组自带函数:
index() 
count()


拆装包:
x,*y =(1,2,3,4,5)
print(y)
print(*y)

'''

t2 = (4, 5) + (1, 2)

print(t2)

t3 = (3, 4) * 2

print(t3)


print(t2 is t3)

print(3 not in t3)

print(len(t2))

print(tuple(sorted(t2)))