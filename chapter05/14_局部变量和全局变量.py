# global  变量的范围
# 局部变量  全局变量
# 声明在函数外层是全局的，所有函数都可以访问。

name = '月月'

def func():
    # 函数内部声明的变量，局部变量.  局部变量仅限于在函数内部使用
    s = 'abcd'
    s += 'X'
    print(s, name)


# print(s)  报错

def func1():
    global name  # 不修改全局变量，只是获取打印。 但是如果要发生修改全局变量，则需要在函数内部声明：global 变量名
    # print(s)
    print(name)    # 报错： 函数内部的变量可以随便修改赋值，但是全局的变量就不能随便在函数体中进行修改
    name += '会弹吉他'

    print('func1修改后的name是:',name)


def func2():
    name = '小月月'  # 局部变量与全局变量同名
    name += '弹吉他的小美女'
    print(name)

    # global name
    # print(name)


# func2()
# func1()
#
# func()

func2()

'''
函数
文件操作


异常
模块

面向对象


'''