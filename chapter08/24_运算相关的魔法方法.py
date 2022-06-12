'''
运算相关魔术方法:
__gt__   --->  >
__lt__   --->   <
__eq__   --->  equals  ==

__le__  --->  <=
__ge__  --->  >=
'''


class Cat:
    def __init__(self, nickname, age):
        self.nickcname = nickname
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

    # def __lt__(self, other):
    #     return self.age < other.age

    def __eq__(self, other):
        print('--->')
        return self.age == other.age

    def __add__(self, other):
        return self.age + other.age

    def __str__(self):
        return str(self.age)


c1 = Cat('花花', 2)
c2 = Cat('小猫1', 1)
c3 = Cat('小猫2', 4)
print(c1 > c2)
print(c1 < c2)

print(c1 == c2)

result = c1 + c2
print(result)
