# 可变参数 + 关键字参数
# 关键字参数：key=value

def add(a, b=10):  # 关键字参数  此时的b就是默认值
    result = a + b
    print(result)


# 调用
add(5)

add(4, 7)  # a=4,b=7   # 此时7就会覆盖b原来的默认值


def add1(a, b=10, c=4):
    print(a, b, c)
    result = a + b + c
    print(result)


add1(1)

add1(1, 5)  # 是给b赋值成功

# 给c赋值而不是给b赋值
add1(2, 6)  # 默认6是赋值给b了，
add1(2, c=6)  # 如果想将6赋值给c，则需要结合关键字的key使用


# 函数： 打印每位同学姓名和年龄
students = {'001': ('蔡徐坤', 21), '002': ('王源', 19), '003': ('王俊凯', 20), '004': ('易烊千玺', 19)}


def print_boy(name, **persons):  # persons = students
    print('{}喜欢的小鲜肉是:'.format(name))
    if isinstance(persons, dict):
        values = persons.values()
        # print(values)
        for name, age in values:
            print('{}的年龄是:{}'.format(name, age))


# 调用
print_boy('蕊蕊', **students)


# def func(**kwargs):  # key word  argument
#     print(kwargs)


# 调用
# func(a=1, b=2, c=3)  # 关键字参数
#
# func()  # {}
#
# func(a=1)  # {'a':1}
#
# func(a=1, b=2)  # {'a': 1, 'b': 2}
#
# dict1 = {'001': 'python', '002': 'java', '003': 'c语言', '004': 'go语言'}
#
# func(**dict1)

'''
练习:
1.
def func(a,*args):
    print(a,args)

调用:
func(2,3,4,5)

func(2,[1,2,3,4])

func(2,3,[1,2,3,4,5])

func(5,6,(4,5,7),9)

2. 
def func(a,b=10,c=3,**kwargs):
    print(a,b,c,kwargs)
    
func(1)

func(2,b=10)

func(3,5,7,a=1,b=2)

3.
def func(a,*args,**kwargs):
    print(a,args,kwargs)

t=(1,2,3,4)
func(1,t)

l=[2,5,8]
func(1,l,a=9,b=6)

'''