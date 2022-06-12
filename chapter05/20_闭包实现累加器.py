# 闭包的应用
# 闭包：
'''
1. 保存返回返回闭包时的状态（外层函数变量）


'''


# 闭包
#
# def func(a, b):
#     c = 10
#
#     def inner_func():
#         s = a + b + c
#         print('相加之后的结果是:', s)
#
#     return inner_func
#
#
# # 调用func
# ifunc = func(6, 9)  # ifunc就是inner_func   ifunc = inner_func
# ifunc1 = func(2, 8)
# ifunc2 = func(1, 9)
#
# print(ifunc)
# print(ifunc1)
# print(ifunc2)
#
# ifunc1()
# ifunc()
# ifunc2()


# 计数器
def generate_count():
    container = [0]

    def add_one():

        container[0] = container[0] + 1  # [2]
        print('当前是第{}次访问'.format(container[0]))

    return add_one


# 内部函数就是一个计数器
counter = generate_count()   # counter = add_one

counter()  # 第一次的访问
counter()  # ....
counter()


'''

在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，
并且把里面的函数返回，我们把这种情况叫闭包

内部函数对外部函数作用域里变量的引用
内部函数对外部函数作用域里变量的引用（非全局变量），则称内部函数为闭包。


访问外部函数的可变类型局部变量可不加nonlocal
访问外部函数的不可变类型局部变量要加 nonlocal


闭包有什么缺点呢？
闭包的缺点1，作用域没有那么直观
闭包的缺点2，因为变量不会被垃圾回收所以有一定的内存占用问题。

闭包作用：1.可以使用同级的作用域
闭包作用：2.读取其他元素的内部变量
闭包作用：3.延长作用域


闭包总结
1.闭包似优化了变量，原来需要类对象完成的工作，闭包也可以完成.
2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存.
3.闭包的好处，使代码变得简洁，便于阅读代码。
4.闭包是理解装饰器的基础

'''