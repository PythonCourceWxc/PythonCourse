class Person:
    name = '张三'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print('{}正在吃{}！。。。'.format(self.name, food))

    def run(self):
        print('{},今年{}岁，正在跑步'.format(self.name, self.age))


p = Person('李四', 20)
p.name = 'lisi'
p.eat('红烧肉')
p.run()

p1 = Person('wangwu', 22)
p1.name = '王五'
p1.eat('狮子头')
p1.run()

p2 = Person('zhaoliu', 17)
p2.run()


# eat()