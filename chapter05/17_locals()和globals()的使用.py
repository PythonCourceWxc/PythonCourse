a = 100  # 全局变量
print(globals())

# 定义函数
def func():
    # 声明变量
    b = 99
    # 声明函数
    def inner_func():
        global a
        nonlocal b
        c = 88
        # 尝试修改
        c += 12
        b += 1
        a += 10
        # 尝试打印
        print(locals())
        print(a, b, c)
    # 调用内部函数
    inner_func()
    # 使用locals()内置函数进行查看。可以看到在当前函数中声明的内容有哪些
    # locals()是一个字典。key：value
    print(locals())


# 调用函数
func()
