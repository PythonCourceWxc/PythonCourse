# 闭包
# 在函数中提出的概念，
'''
条件：
1. 外部函数中定义了内部函数
2. 外部函数是有返回值
3. 返回的值是：内部函数名
4. 内部函数引用了外部函数的变量

格式:
def 外部函数():
    ...
    def 内部函数():
        ....
    return 内部函数


'''

def func():
    a = 100

    def inner_func():
        b = 99
        print(a, b)

    print(locals())

    return inner_func


# print(a)
# inner_func()


x = func()

print(x)  # <function func.<locals>.inner_func at 0x00000000021500D0>

# x就是内部函数，x()就表示调用函数
x()
