# 私有化: 如果想让类的内部属性不被外界直接访问，可以在这个属性的前面加两个下划线__ ,在Python中，如果一个属性的前面出现 __,就表示这个属性只能在当前类的方法中被直接访问，不能通过对象直接访问，这个变量就被称为私有变量
# 封装: 1. 私有化属性  2.定义公有set和get方法
# __属性： 就是将属性私有化，访问范围仅仅限于类中
'''
好处：
1. 隐藏属性不被外界随意修改
2. 也可以修改：通过函数
   def setXXX(self,xxx):
       3. 筛选赋值的内容
         if xxx是否符合条件
             赋值
          else:
             不赋值
3.如果想获取具体的某一个属性
  使用get函数
    def getXXX(self):
       return self.__xxx
'''


class Student:
    # __age = 18  # 类属性

    def __init__(self, name, age):
        self.__name = name  # 长度必须6位
        self.__age = age
        self.__score = 59

    # 定义公有set和get方法
    # set是为了赋值
    def setAge(self, age):
        if age > 0 and age < 120:
            self.__age = age
        else:
            print('年龄不在规定的范围内')

    # get是为了取值
    def getAge(self):
        return self.__age

    # 修改名字的时候，长度必须6位
    def setName(self, name):
        if len(name) == 6:
            self.__name = name
        else:
            print('名字不是六位')

    def getName(self):
        return self.__name

    def __str__(self):
        return '姓名:{},年龄:{},考试分数:{}'.format(self.__name, self.__age, self.__score)


yupeng = Student('yupeng', 18)
print(yupeng)
yupeng.setAge(120)
print(yupeng)
# yupeng.name = 'xiaopeng'
yupeng.setName('xiaopeng')
print(yupeng)

# 就想拿到于鹏年龄
print(yupeng.getAge())

feifei = Student('feifei', 20)
print(feifei)

# yupeng.age = 21
# print(yupeng.__score)
# yupeng.__score = 95
# print(yupeng)
print(dir(Student))
print(dir(feifei))
