'''
应用场景:
1. 猜大小  ---》反复的猜
2. 消消乐  ---》 反复充值
3. 用户登录 ----》 登录多次
    用户名
    密码

循环结构:
	for 变量名 in 集合:
		语句 

怎么用？

'''
# 使用系统给定range()完成范围指定
print(range(8))   # range(0,8)   包含0 但是不包含8  0,1,2,3,4,5,6,7

# 打印三次
for i in range(2):
	print('hello ---->',i)

print('---- game over -----')



'''
 循环：吃5个馒头

'''
name='赵飞'
# 方式1：
# for i in range(5):  # 0,1,2,3,4
# 	# i = 0
# 	print('{}很饿，正在吃第{}馒头'.format(name,i+1))

#方式2:
# for i in range(1,6):  # 1,2,3,4,5
# 	print('{}很饿，正在吃第{}馒头'.format(name,i))

# print('{}说:终于吃饱啦！'.format(name))


# range(n)  ---> 0~n-1
# range(m,n) ----> m ~ n-1


'''
吃馒头：在第三个馒头上抹了一点’鹤顶红‘

'''
# print('*'*30)
# name = '张无忌'

# for i in range(1,6):
# 	# 判断i的值是多少，i==3 别吃
# 	if i==3:  # i=1,2,4,5
# 		print("{}赶快扔掉这个馒头，有剧毒：'鹤顶红'!!!".format(name))
# 	else:	
# 		print('{}很饿，正在吃第{}馒头'.format(name,i))

# print('{}说:终于吃饱啦！'.format(name))


'''
for .... else

else：适用于for执行完或者没有循环数据时，需要做的事情

for i in 范围：
    有数据执行的语句
else:
	没有数据执行的语句

pass  空语句
只要有缩进而缩进的内容还不确定的时候，此时为了保证语法的正确性，就可以使用pass占位。
不会报出语法错误。

'''
# num = int(input('请输入需要的馒头数量:'))

# for i in range(num): # 2
# 	print('{}很饿，正在吃第{}馒头'.format(name,i+1))
# else:
# 	print('还没有给我馒头，{}饿哭啦.....'.format(name))

# print('---------------')


# if 10<7:
# 	print('10是大的')
# else:
# 	pass

# print('-----判断结束-----')

# 用户的账号密码登录而且只能登录三次，如果三次未成功账户锁定
# break 关键字
# for i in range(3):
# 	username = input('请输入用户名:')
# 	password = input('请输入密码:')
# 	# 验证用户名和密码
# 	if username =='songsong' and password == '123456':
# 		print('欢迎！用户:{}'.format(username))
# 		print('-------轻松购物吧---------') 
# 		break
# 	else:
# 		print('用户名或者密码有误！')
# else:
# 	print('账户被锁定，需要重新激活！')  # 三次输入错误的时候

 # 登录成功

         # 0,1,2
for i in range(3):
	if i==4:
		print('这家店是黑店，馒头有毒！等着关门吧！')
		print('--------->进入消费者协会大门')
		break  # 跳出循环结构
		print('abcd')  # 即使有语句也不会执行，干脆别写！
	else:
		print('这家店的馒头真香啊！要多吃几个呀！')

else:
	print('---->这家店太棒啦，下次再来！')
'''

 range的范围正常执行完毕，而没有异常break跳出。就可以执行else，
 只要有break执行了就不会执行else


 range(n)  ~ range(0,n)
 range(m,n) ~ range(start,end)
 range(m,n,step) ~ range(start,end,step)
 step: 步长

			
 for i in range(5):
 	print(i)

0,1,2,3,4


for i in range(5):
	pass
else:
	pass

break: 跳出
'''


