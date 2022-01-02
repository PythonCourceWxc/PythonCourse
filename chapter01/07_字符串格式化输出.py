name='赵飞'
print('姓名是:'+name)  # str + str

age=18
# str(int) ---> (int ->str)  强制类型的转换 
print('年龄是:'+str(age))  # 'aaa'  int --->str
print('年龄是:%s' % age)  # %s --> str 简写   底层：str(age) ---> '18'
isMarry=False  # 布尔： True， False
print('结婚否？回答: %s' % isMarry)  # str(False) ---> 'False'


# %d  digit  数字
print('年龄是:%d' % age) 

# age= '18岁'  

# print('年龄是:%d' % age)  

age=18.5   # int(18.5)--->18  取整数
print('年龄是:%d' % age)  

year=2019
print('今年是：%02d' % year)  # 仍然是2019 但是%f就可设置位数


# %f float  小数点后面的位数 而且是四舍五入
salary=8899.32895
print('我的薪水是:%.2f' % salary)

'''
约起来去楼上看电影，下订单：

movie='大侦探皮卡丘'
ticket =45.9
count= 35

格式：

电影：xxxx
人数： xxx
单价: xxx
总票价:xxx  （小数点后面保留1位）

'''



movie='大侦探皮卡丘'
ticket =45.9
count= 35
total = ticket*count

# 写法1：
# message='''
# 电影：%s
# 人数： %d
# 单价: %f
# 总票价:%.1f  

# ''' % (movie,count,ticket,total)

# print(message)

# 写法2：
print('电影：%s' % movie)
print('人数： %d' % count)
print('单价: %.0f' % ticket)
print('总票价:%.1f' % total)