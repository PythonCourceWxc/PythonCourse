'''
魔术方法就是一个类的特殊方法，和普通方法唯一的不同时，普通方法需要调用！而魔术方法由系统自动调用
__new__;
实例化对象是Object类底层实现，其他类继承了Object的__new__才能够实现实例化对象。
没事别碰这个魔术方法，先触发__new__才会触发__init__
'''


class Person:
    def __init__(self):
        print('----------->init')

    def __new__(cls, *args, **kwargs):
        print('----------->new')
        obj = object.__new__(cls)
        return obj

    def __del__(self):
        print('------------>del')


p = Person()
print(p)
p3 = p
del p

p1 = Person()
print(p1)

p2 = Person()
print(p2)

print('---------over---------')
