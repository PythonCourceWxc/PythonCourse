# class Person:
#     def __init__(self,name):
#         self.name=name
#
#     def eat(self):
#         print('------->eat1')
#
#     def eat(self,food):
#         print('------------>eat:',food)
#
# p = Person('jack')
# p.eat('狮子头')
class Base:
    def test(self):
        print('---------Base-----------')


class A(Base):
    def test(self):
        print('--->AAAAAAAAAA')


class B(Base):
    def test(self):
        print('----------->BBBBBBBB')


class C(Base):
    def test(self):
        print('----------->CCCCCCCCC')


class D(A, B, C):
    pass


d = D()
d.test()
import inspect

print(inspect.getmro(D))

print(D.__mro__)
# c.test1()
# c.test2()

'''
 python允许多继承，
 def 子类(父类1，父类2，..):
    pass

 如果父类中有相同名称方法，搜索顺序: 

'''