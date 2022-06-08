class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def setName(self, name):
        if len(name) == 6:
            self.__name = name
        else:
            print('名字必须6位')

    def getName(self):
        return self.__name

    def __str__(self):
        return '姓名:{},年龄:{}'.format(self.__name, self.__age)

    # attribute: setName  getName  __str__  __init__


s = Student('yupeng', 18)

print(s)

print(dir(Student))

print(dir(s))
# print(s.__name)  # _Student__name
print(s._Student__age)  # 其实它就是__age ,只不过系统自动改名字了。
print(s.__dir__())
print(__name__)
