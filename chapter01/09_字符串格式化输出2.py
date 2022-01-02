# 字符串的格式化输出
# 方式：1. 使用占位符 %s %d %f  2. format函数

# format是一个字符串中的函数 ''.format()   此处的‘.’ 调用  [] {} ()
age=2
s='已经上'
message =  '乔治说:我今年{}岁了，{}幼儿园！'.format(age,s)
print(message)

name='乔治'
age=3
hobby = '玩恐龙！'
money=5.89

message= '{}今年{}岁，最喜欢{},有零花钱：{}'.format(name,age,hobby,money)

print(message)

print('{}今年{}岁，最喜欢{},有零花钱：{}'.format(name,age,hobby,money))

