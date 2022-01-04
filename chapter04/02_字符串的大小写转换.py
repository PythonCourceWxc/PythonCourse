# 字符串的内建函数： 声明一个字符串，默认可以调用内建函数（系统准备好的一些函数）

# 第一部分： 大小写相关的
# capitalize()  title() istitle()   upper()  isupper()   lower()  islower（）

message = 'zhaorui is a beautiful girl！'

msg = message.capitalize()   # 将字符串的第一个字符串转成大写的标识形式
print(msg)


msg = message.title()  # 返回的是 每个单词的首字母大写的字符串
print(msg)

result = message.istitle() # 返回的结果是布尔类型的，True False
print(result)


msg = message.upper()  # 将字符串全部转成大写的表示形式
print(msg)

result = msg.lower()  # 将大写全部转小写
print(result)

# 案例：验证码案例

s='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0987654321'

print(len(s))  # 求字符串长度 len(str),返回值是一个整型的数值

# 四个随机数
code =''

import random

# # IndexError: string index out of range   s = 'abc'  print(s[3])
# # index: 0~len(s)-1    0~61
# 产生四位验证码
for i in range(4):

	ran = random.randint(0,len(s)-1)  # 获取随机数

	code += s[ran]   # code = code + ‘V’   ---》code='V' 不断拼接到code上

print('验证码:'+code)

# 提示用户输入验证码

user_input = input('请输入验证码:')

if user_input.lower() == code.lower():
	print('验证码输入正确！')
else:
	print('验证码错误！')