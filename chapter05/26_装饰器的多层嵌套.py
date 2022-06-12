# 装饰器带参数
'''
带参数的装饰器是三层的
最外层的函数负责接收装饰器参数
里面的内容还是原装饰器的内容
'''


def outer(a):  # 第一层： 负责接收装饰器的参数
    print('------------1 start')

    def decorate(func):  # 第二层 ： 负责接收函数的
        print('------------2 start')

        def wrapper(*args, **kwargs):  # 第三层   负责接收函数的参数
            func(*args)
            print("---->铺地砖{}块".format(a))

        print('------------2 end')
        return wrapper  # 返出来的是：第三层

    print('------------1 end')
    return decorate  # 返出来的是：第二层


@outer(10)
def house(time):
    print('我{}日期拿到房子的钥匙,是毛坯房....'.format(time))


# @outer(100)
# def street():
#     print('新修街道名字是：黑泉路')


house('2019-6-12')

# street()
