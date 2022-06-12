# 登录校验
import time


def decorate(func):
    def wrapper(*args, **kwargs):  # ()  {'clazz':'1904'}
        print('正在校验中....')
        time.sleep(2)
        print('校验完毕.....')
        # 调用原函数  args --->()
        func(*args, **kwargs)  # f1  f2  f3...

    return wrapper


@decorate
def f1(n):
    print('-------f1-------', n)


f1(5)  # 此时的f1是wrapper，


@decorate
def f2(name, age):
    print('-------f2-------', name, age)


f2('lily', 20)


#
#
@decorate
def f3(students, clazz='1905'):
    print('{}班级的学生如下:'.format(clazz))
    print('------------>f3')
    for stu in students:
        print(stu)


students = ['lily', 'tom', 'lucy']
f3(students, clazz='1904')



@decorate
def f4():
    print('------------>f4')

f4()