# is a   base class   父类  基类
# Exception
'''
继承：
  Student，Employee，Doctor  ---》 都属于人类
  相同代码 ---》 代码冗余，可读性不高

  将相同代码提取----》Person类
    Student，Employee，Doctor  ---》 继承Person

    class Student(Person):
        pass

'''


class Person:
    def __init__(self, name):
        self.name = name
        self.age = 18

    def eat(self):
        print(self.name + "正在吃饭...")

    def run(self):
        print(self.name + '正在跑步...')


class Student(Person):

    def __init__(self, name):
        print('---------->student的init')
        # 如何调用父类__init__
        super().__init__(name)  # super()  父类对象


class Employee(Person):
    pass


class Doctor(Person):
    pass


s = Student("jack")
s.run()
e = Employee('lily')
e.run()
d = Doctor('tom')
d.run()