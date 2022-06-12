# 开发：登录验证
import time

islogin = False  # 默认是没有登录的


# 定义一个登录函数
def login():
    useranme = input('输入用户名:')
    password = input('输入密码:')
    if useranme == 'admin' and password == '123456':
        return True
    else:
        return False


# 定义一个装饰器，进行付款验证
def login_required(func):  # func = pay
    def wrapper(*args, **kwargs):
        global islogin
        print('-----------付款------------')
        # 验证用户是否登录
        if islogin:
            func(*args, **kwargs)  # pay(8000)
        else:
            # 跳转到登录页面
            print('用户没有登录，不能付款!')
            islogin = login()
            print('result:', islogin)

    return wrapper


@login_required
def pay(money):
    print('正在付款,付款金额是:{}元'.format(money))
    print('付款中....')
    time.sleep(2)
    print('付款完成!')


# 调用  pay =  wrapper(10000)
pay(10000)

pay(8000)
