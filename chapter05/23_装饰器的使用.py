# 地址引用
a = 10  # 声明整型变量
b = a


def test():  # 声明函数
    print('------test-------')


# t = test
# test()
# t()

# def func(f):  # f=test
#     print(f)  # <function test at 0x0000000001D01E18>
#     f()  # -------test---------
#     print('------------>func')
#
#
# # 调用
# func(test)

'''
特点:
1. 函数A是作为参数出现的（函数B就接收函数A作为参数）
2. 要有闭包的特点
'''


# 定义一个装饰器
def decorate(func):
    a = 100
    print('wrapper外层打印测试')

    def wrapper():
        func()
        print('--------->刷漆')
        print('--------->铺地板', a)
        print('--------->装门')

    print('wrapper加载完成......')
    return wrapper


# 使用装饰器
@decorate
def house():
    print('我是毛坯房....')

'''
默认执行的:
1. house被装饰函数，
2. 将被装饰函数作为参数传给装饰器decorate
3. 执行decorate函数
4. 将返回值又赋值给house

'''
# print(house)

house()
# house()
# def house1():
#     house()
#     print('刷漆')
#     print('铺地板')


# 调用函数house
# house()