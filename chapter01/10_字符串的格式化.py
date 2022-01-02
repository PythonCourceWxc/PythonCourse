person ='大圣哥'
address = '北京市海淀区中关村智诚科技大厦4层'
phone= '15858588888'
num=5
# '+' 符号 拼接   字符串  + 字符串  ---》ok  ，字符串 + int ----》TypeError
# print('订单的收件人是:'+person+'收货地址是:'+address+'联系方式:'+phone+',商品数量是:'+ num)

print('订单的收件人是:%s,收货地址是:%s,联系方式:%s,商品数量是:%s' % (person,address,phone,num))


'''
1. 
个人信息简介：

名字
年龄
班级

我的名字：xxx ，今年n岁了，现在在xxx班级

2. 

个人信息简介：
我的名字：xxx 
今年n岁
现在在xxx班级

'''


name='admin'
age=18
clazz = 'python1905'

msg = '''
个人信息简介：
我的名字：%s 
今年%s岁
现在在%s班级

''' % (name,age,clazz)

print(msg)

