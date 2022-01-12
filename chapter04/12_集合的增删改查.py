# 不重复特点:
list1 = [3, 5, 8, 9, 1, 8, 4, 2, 5, 8, 9]

# 声明集合： set

s1 = set()  # 创建空集合,只能使用set()

s2 = {1, 3, 7}   # 字典： {key:value,key:value,....}  集合 {元素1，元素2，元素3,...}

print(type(s1))
print(type(s2))


#应用： 如果将一个列表快速去重 set()
s3 = set(list1)
print(s3)   # {1,2,3,4,5,...}


# 增删改查:

# 1. 增加   s1 = set()
s1.add('hello')

s1.add('小猪佩奇')

s1.add('lucy')

print(s1)


# add()  添加一个元素
# update()  可以添加多个元素,  

t1 = ('林志玲', '言承旭')
s1.update(t1)  # {'hello','林志玲',....}

print(s1)

s1.add(t1)
print(s1)


#2. 删除  remove 如果元素存在则删除，不存在则报错keyError    pop  随机删除（一般删除第一个元素）  clear。。。
#   dicard()  类似remove()   在移除不存的元素的时候不会报错。
s1.remove('言承旭')

print(s1)

# s1.remove('道明寺')   
# print(s1)

s1.pop()

print(s1)

s1.pop()

print(s1)


s1.clear()  # 清空

print(s1)

'''
  1. 产生了10个1~20的随机数，去除里面的重复项
  2. 键盘输入一个元素，将此元素从不重复的集合中删除

'''