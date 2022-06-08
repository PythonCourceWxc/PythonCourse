'''
定义一个登陆函数，参数是：username，password
函数体：
判断参数传过来的username,password是否正确，如果正确则登陆成功，否则打印登陆失败

'''


# 函数的定义
def login(username, password):
    # 相当于数据库注册的用户名和密码
    uname = 'admin123'
    pwd = '112233'

    for i in range(3):
        if username == uname and password == pwd:
            print('登陆成功！')
            break
        else:
            print('登陆失败！')
            username = input('输入用户名:')
            password = input('输入密码:')
    else:
        print('账户锁定！')


# 调用:
username = input('输入用户名:')
password = input('输入密码:')

login(username, password)
