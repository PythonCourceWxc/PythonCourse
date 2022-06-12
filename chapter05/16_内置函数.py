# 内部函数
'''
特点:
1. 可以访问外部函数的变量
2. 内部函数可以修改外部函数的可变类型的变量比如：list1
3. 内部函数修改全局的不可变变量时，需要在内部函数声明global 变量名
   内部函数修改外部函数的不可变的变量时，需要在内部函数中声明: nonlocal 变量名
4. locals() 查看本地变量有哪些，以字典的形式输出
   globals() 查看全局变量有哪些，以字典的形式输出（注意里面会有一些系统的键值对）


'''


def func():
    # 声明变量
    n = 100  # 局部变量
    list1 = [3, 6, 9, 4]  # 局部变量

    # 声明内部函数
    def inner_func():
        nonlocal n
        # 对list1里面的元素进行加5操作
        for index, i in enumerate(list1):
            # 0  3
            list1[index] = i + n

        list1.sort()

        # 修改n变量
        n += 101

    # 调用一下内部的函数
    inner_func()

    print('打印老大n:', n)

    print('打印老二list1:', list1)


# 调用func
func()
