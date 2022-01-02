#coding:utf-8
n1 = int(input('请输入第一个数:'))
n2 = int(input('请输入第二个数:'))

# 判断n1 与 n2

result = n1 > n2     # 结果False  True
    #    8 > 12   --->False
print('n1>n2:',result)


result = n1 == n2
print('n1==n2:',result)


m1='hello'
m2='hello'

result = m1==m2

print('m1==m2:',result)

username= input('输入用户名:')

uname ='admin123'

# result = username==uname
result = username != uname   # 如果两者不相等则会返回True，相等则返回False
print('用户名的验证结果是:',result)


# is   用户对象的比较

age = 20

age1 = 20
print(id(age))
print(id(age1))

print(age is age1)

money = 2000000
salary = 2000000
print(id(money))
print(id(salary))

print(money is salary)

