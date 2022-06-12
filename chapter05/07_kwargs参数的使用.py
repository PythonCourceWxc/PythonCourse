'''
使用函数的时候:
def aa(**kwargs):
    pass

aa(a=1, b='hello', c='tom')    --->将关键字装包成字典

'''


def aa(**kwargs):
    print(kwargs)


aa(a=1, b='hello', c='tom')  # 装包：{'a': 1, 'b': 'hello', 'c': 'tom'}

# 如果在开发的时候，已知一个字典

dict1 = {'a': 1, 'b': 'hello', 'c': 'tom'}

aa(**dict1)  # a=1, b='hello', c='tom'    拆包的过程


def bb(a, b, *c, **d):
    print(a, b, c, d)


bb(1, 2)  # 1 2 () {}

bb(1, 2, 3, 4)  # 1 2 (3,4) {}

bb(1, 2, x=100, y=200)  # 1 2 () {'x':100,'y':200}

bb(1, 2, 3, x=100)  # 1 2 (3,) {'x':100}

bb(1, 2, x=100, y=200, z=100) # 1 2 () {'x': 100, 'y': 200, 'z': 100}
