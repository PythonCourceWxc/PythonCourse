# 闭包

def func(a, b):
    c = 10

    def inner_func():
        s = a + b + c
        print('相加之后的结果是:', s)

    return inner_func


# 调用func
ifunc = func(6, 9)  # ifunc就是inner_func   ifunc = inner_func

# 调用返出来的内部函数
ifunc()

ifunc()


