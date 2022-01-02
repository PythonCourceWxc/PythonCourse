# 赋值运算符

# 1. =
name = 'admin'

# 将'admin'的值赋给 变量name 

# 1+1 = 2

name1 = name

print(id(name),name)
print(id(name1),name1)

name2=name
print(id(name2),name2)

# id()

print(name == name1)  # 

name1='admin1'

print(id(name1),name1)

print(id(name),name)

name ='admin2'

print(id(name),name)


name3 = name

print(id(name3),name3)

# 扩展后的赋值符号  +=  -=  *=  /=  ...

num = 8

num += 5   # num = num + 5   此时+ 数学加号
print(num)


num-=10  # num = num-10

print('num=',num)

a='abc'
 
a += 'ff' # 等价于： a = a +'ff'  此时'+'就是连接符  包含两个动作: 1. 连接  2.连接后的结果赋值

print(a)


# a -= 'kk'   # 不支持  
# print('a=',a)

'''
测试：
-=
*=
/= 
只是可以应用在数值，字符串不支持



'''

