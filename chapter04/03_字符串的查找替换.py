# 查找相关的,替换

# find()   rfind()  lfind()   index()  rindex()  lindex()   replace()

s1 = 'index lucy lucky goods'

result = 'R' in s1
print(result)


position = s1.find('R')  # 返回值是-1则代表没有找到
print(position)

position = s1.find('l')  # 如果可以找到则返回字母第一次出现的位置
print(position)

# find('要查找的字符',start,end)
p = s1.find('o',position+1,len(s1)-5)  # 也可以指定开始位置查找
print(p)


# https://www.baidu.com/img/bd_logo1.png

url = 'https://www.baidu.com/img/bd_logo1.png'

p = url.rfind('/')  # right find  从右侧检索/的位置
print(p)

filename = url[p+1:]
print(filename)

p = url.rfind('.')

kz= url[p+1:]
print(kz)

'''
index(str, beg=0, end=len(string))
跟find()方法一样，只不过如果str不在字符串中会报一个异常

p = 'hello'.index('x')

print(p)

ValueError: substring not found

'''

# 替换

s1 = 'index lucy lucky goods'

# replace(old,new,[max])
s2 = s1.replace(' ','#')
print(s2)

s2 = s1.replace(' ','',2)
print(s2)