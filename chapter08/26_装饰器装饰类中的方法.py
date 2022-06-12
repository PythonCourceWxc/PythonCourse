'''
@property 装饰器是用来装饰类中方法的
步骤：
1. 在get方法上面添加@property装饰器,函数的名字最好更加简要，让使用者在调用或者访问的时候更加简单
2. 装饰set方法：
       @属性名.setter
       def 属性名(self,参数)：
            pass
3.使用：
  对象 = 类名(参数)
  print(对象.属性名)  -----> get方法
  对象.属性名=值   -----》 set方法
'''


class Person:
    __slots__ = ['__name', '__age', '__flag', '__password']

    def __init__(self, name, age):
        self.__name = name
        self.__password = '1234'
        self.__age = age
        self.__flag = False

    @property
    def name(self):
        if self.__flag:
            return self.__name
        else:
            return '没有权限查看用户名'

    @name.setter
    def name(self, name):
        if len(name) >= 6:
            self.__name = name
        else:
            print('名字必须要大于等于6位')

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 125 > age > 0:
            self.__age = age
        else:
            print('年龄赋值失败，必须在0~125范围内')

    def login(self, name, password):
        if self.__name == name and self.__password == password:
            print('登录成功！')
            self.__flag = True
        else:
            print('用户名或者密码有误！')


p = Person('jack', 21)
p.login('jack', '1234')

print(p.name)

p.name = 'steven'
print(p.name)

p.name = 'tom'
print(p.name)
