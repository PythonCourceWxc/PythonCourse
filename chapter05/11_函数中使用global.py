'''
 加入购物车
 判断用户是否登录，如果登录，成功加入购物车，否则提示请登录之后添

 成功 True   不成功  False

 def add_shoppingcart(goodsName):
    pass

 def login(username,password):
    pass

  调用
'''

islogin = False  # 用于判断用户是否登录变量  默认是没有登录的


def add_shoppingcart(goodsName):
    global islogin

    if islogin:
        if goodsName:
            # 登录的
            print('成功将{}加入到购物车中！'.format(goodsName))
        else:
            print('没有选中任何商品！')
    else:
        # 没有登录
        answer = input('用户没有登录！是否登录用户？(yes/no)')
        if answer == 'yes':
            # 登录
            username = input('输入用户名:')
            password = input('输入密码:')

            # 调用login
            islogin = login(username, password)  # 在一个函数中可以调用另一个函数
            print('islogin:',islogin)

        else:
            print('很遗憾！不能添加任何商品！')


def login(username, password):
    if username == 'lijiaqi' and password == '123456':
        # 登录成功
        # print('登录成功')
        return True
    else:
        # print('用户名或者密码有误')
        return False


# 调用函数： 添加商品到购物车中
username = input('输入用户名:')
password = input('输入密码:')

islogin = login(username, password)

add_shoppingcart('阿玛尼唇釉')
