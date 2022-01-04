# isalpha() 是否是字母   isdigit() 是否是数字

s ='abcd'
result = s.isalpha()
print("result=",result)

s='6688'

result = s.isdigit()
print(result)

# sum = 0 
# for i in range(3): # 0,1,2
# 	num = input('请输入数字:')  # ll

# 	if num.isdigit():
# 		num = int(num)

# 		sum+=num

# print('sum=',sum)

sum = 0 
i = 1

# while i<=3:
# 	num = input('请输入数字:')

# 	if num.isdigit():
# 		num = int(num)
# 		sum+=num
# 		print('第{}个数字数字累加成功！'.format(i))
# 		i+=1
# 	else:
# 		print('不是数字！')

# print('sum=',sum)


# join() : '-'.join('abc')   将abc用-连接构成一个新的字符串

new_str = '-'.join('abc')
print(new_str)


# python 列表  list =['a','v','o','9']   数组
list1 =['a','v','o','9']
result = ''.join(list1)   # 
print(result)

result = ' '.join(list1) 
print(type(result))



# lstrip    rstrip  strip 

s ='   hello    '

# s= s.lstrip()  # 去除字符串左侧的空格
# print(s+'8')

# s = s.rstrip()  # 去除右侧的空格
# print(s+'8')

s = s.strip()
print(s+'8')



# split(‘分隔符’，次数)  分割字符串,将分割后的字符串保存到列表中

s ='hello world hello kitty'

result = s.split(' ',2)  # 表示按照空格作为分隔符，分割字符串2次
print(result)


n = s.count(' ')  # count(args)  求字符串中指定args的个数
print('个数:',n)


# s='hfdsjkhfdf;lksd;fk'
# s.count('s')

'''
总结：
大小写： lower()  upper()
查找: find()   rfind()
替换: replace()
分割: split()
连接: join()
编码： encode()  decode()的使用
个数： count()
去除空格：  strip()   lstrip()  rstrip() 
用于判断的:
startswith()   开头判断
endswith()     结尾判断
isalpha()      字母判断
isdigit()      数字判断

'''

print('用户名\t密码\t邮箱')