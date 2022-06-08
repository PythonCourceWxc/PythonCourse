'''
方法：
    普通方法:
        定义格式:
             def 方法名(self,参数1，参数2):
                pass
         调用：
             都要依赖对象调用方法
             对象名.方法名(参数)
             注意： 在调用过程中会默认传递self对象，self表示的是对象本身

        方法中访问对象属性：
             self.属性名
             self.属性名= 值   ----》 改变对象属性的值

        方法中访问普通方法：
            self.方法名(参数)


   类方法：

   静态方法：

   魔术方法：

'''


class Card:
    def __init__(self, cardno, phone):
        self.money = 0
        self.cardno = cardno
        self.phone = phone

    # 动作
    def save_money(self, money):  # self表示的是对象本身
        self.money += money
        print('存钱成功')
        # 调用‘兄弟’方法show
        self.show()
        # print('{}存钱成功,当前余额是:{}'.format(self.cardno, self.money))

    def withdraw_money(self, money):
        if money < self.money:
            self.money -= money
            print('{}取钱成功，当前余额是:{}'.format(self.cardno, self.money))
        else:
            print('账户金额不足！')

    def show(self):
        print('用户的详细信息:')
        print('卡号是:{},余额:{},手机号码:{}'.format(self.cardno, self.money, self.phone))


# 创建对象
card1 = Card('739840934903', '18966778900')
card1.save_money(10000)
card1.save_money(50000)

card1.withdraw_money(5000)
card1.withdraw_money(40000)

# card1.show()
# Card.save_money()

card2 = Card('452358278349', '13899004567')
card2.save_money(80000)


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