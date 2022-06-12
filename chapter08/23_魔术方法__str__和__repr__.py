'''
 __str__ 魔术方法
 __repr__
 作用： 都是将对象转成字符串的表示形式
 print(obj)  ----> __str__
 repr(obj)  ---->  __repr__
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + '\t' + str(self.age)

    def __repr__(self):
        return 'helloworld'

    def __call__(self, *args, **kwargs):
        print('我被调用啦')

    def __len__(self):
        return 5


p = Person('zhangsan', 20)
print(p)
p()

p1 = Person('lisi', 16)
print(p1)

# def func():
#     print('func')
#
# func()

r = repr(p1)
print('---->', r)

list1 = [1, 2, 3, 5, 6]
print(len(list1))

print(len(p1))