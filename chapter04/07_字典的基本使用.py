'''
案例:
用户注册功能

username
password
email
phone


'''

print('------------欢迎来到智联招聘用户注册--------------')
# 模拟数据库
database = []

while True:
	username = input('输入用户名:')
	password = input('输入密码:')
	repassword = input('输入确认密码:')
	email = input('输入邮箱:')
	phone = input('输入手机号:')

	# 定义一个字典
	user = {}

	# 将信息保存到字典中
	user['username'] = username
	if password == repassword:
		user['password'] = password
	else:
		print('两次密码不一致！重新输入.....')
		continue

	user['email'] = email
	user['phone'] = phone

	# 保存到数据库
	database.append(user)

	answer = input('是否继续注册?(y/n)')

	if answer != 'y':
		break


print(database)
for user in database:
	print(user)  #{}


