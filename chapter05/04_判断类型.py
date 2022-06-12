# 找出列表的最大值

# 自己封装一个求最大值函数

def max(iterable):
    max = iterable[0]
    for i in iterable:
        if i > max:
            max = i
    print('最大值是:', max)


# 调用： 测试是否能找出最大值
list1 = [4, 1, 4, 3, 8, 9]
max(list1)

tuple1 = (3, 6, 1, 0, 5)
max(tuple1)

# sort     reverse   max   min

print(type(tuple1))  # 查看是什么类型

# 判断是不是什么类型： isinstance(变量,类型关键字)
print(isinstance(2, int))  # 返回值是False，True

print(isinstance(tuple1, tuple))

if isinstance(tuple1, tuple):
    print('不能排序和翻转')
