# 函数：带参数的
'''
定义：
 def 函数名(参数,参数,..):
    函数体
调用:
    pass
'''

# 求随机数的函数，产生的个数？？？？
# alt+enter  快速提醒/提示
import random

def generate_random(number):  # 形参：形式上参数   number=5
    for i in range(number):
        ran = random.randint(1, 20)
        print(ran)


# print(generate_random)

# 调用
generate_random(5)  # 实参：实际的参数 具体的值
generate_random(8)


# 求加法的函数
def add(a, b):  # 参数2个 形参
    result = a + b
    print("和:", result)


# 调用
add(2, 3)  # 实参 2个
add(1, 1)

'''
定义一个登陆函数，参数是：username，password
函数体：
判断参数传过来的username,password是否正确，如果正确则登陆成功，否则打印登陆失败

'''
