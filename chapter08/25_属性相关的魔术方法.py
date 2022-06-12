'''
跟属性相关的魔术方法：
   __getattr__
   __setattr__
'''


class Person:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        if item == 'age':
            return 20
        elif item == 'gender':
            return '男'
        else:
            return '不存在此属性{}'.format(item)

    def __setattr__(self, key, value):
        print(key, value)
        # self.key = value  # 递归操作
        if key == 'phone' and value.startswith('139'):
            object.__setattr__(self, key, value)



p = Person('老王')
print(p.name)
#
# print(p.age)
#
# print(p.gender)
#
# print(p.phone)

# p.name = '隔壁老王'
# print(p.name)
p.phone = '13910001897'
print(p.phone)
print('------')

print(p.__dict__)  # 获取p对象的自身属性，并以字典的形式返回
