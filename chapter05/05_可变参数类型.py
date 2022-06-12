# 有参数的函数:
# 可变参数

# def add(a, b):
#     pass
# add(1,3)


# 定义方式:
# def add(*args):  # arguments 参数
#     # print(args)
#     sum = 0
#     if len(args) > 0:
#         for i in args:
#             sum += i
#         print('累加和是:sum:', sum)
#     else:
#         print('没有元素可计算，sum:', sum)
#
#
# add()  # （）空元组
# add(1)  # (1,)
# add(1, 2)  # (1,2)
# add(1, 2, 3, 4)  # （1,2,3,4）


# xxx 计算出来的累加和是:xxx

def add(name, age, *args):  # name, *args ='飞飞', 4, 6, 8
    # print(args, name)
    sum = 0
    if len(args) > 0:
        for i in args:
            sum += i
        print('%s累加和是:sum:%s' % (name, sum))
    else:
        print('没有元素可计算，sum:', sum)


# 调用
add('飞飞', 4, 6, 8)

add('阿文', 10)  # name,age, *args='阿文',10

add('学强', 9)

# a,*b =1,3,5,6,7

# 注意： 可变参数必须放在后面: name,*args



