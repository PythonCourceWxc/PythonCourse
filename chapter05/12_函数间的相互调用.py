def a():
    print('AAAAAAAAAA')


def b():
    # 调用函数a
    a()
    print('BBBBBBBBBBB')


def c():
    b()
    print('CCCCCCCCCCC')

# 调用b
# b()

c()
