# print函数
# 1.用法
print('hello world!')
name = '小白'
print(name)

#2.用法：print(name,age,gender)
age =18
gender ='boy'

print(name,age,gender)  # sep默认的分割是空格

# 3.用法： print(value,value,value,...,sep=' ',end='\n')
print(name,age,gender,sep='-') # sep=‘*’  sep='$' sep='-'

# 转义字符： \n 换行
print('hello\nkitty')

print('AAA',end='')  # 'AAA\n'  ---> 'AAA'
print('BBB',end='')  # 'BBB\n'  --->  'BBB'
print('CCC',end='')  # 'CCC\n'  --->  'CCC'

# 练习:     亲爱的xxx：
          #     请点击链接激活用户：激活用户
print()

print('亲爱的xxx：\n','\t请点击链接激活用户：激活用户')

# 转义字符： 预定义的转义 ： \n 换行   \t 制表符  \'    \"   \r 回车  \\
print('乔治说：\' 想吃冰淇淋 !!\' ')
print("乔治说：\" 想吃冰淇淋 !!\" ")
#  ‘‘’’  “ ‘’ ”    ‘ “ ” ’

print(" 乔治说：'想玩恐龙！' ")


print('乔治说："想睡觉！！！"')

print('\ahahha')

print('hello\py\\thon')

print(r'hello\py\thon')  # r'' raw   原样输出字符串的内容，即使有转义字符也不会转义