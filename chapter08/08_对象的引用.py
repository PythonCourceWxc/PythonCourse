import sys
'''
__del__:
  1. 对象赋值
     p = Person()
     p1 =p
     说明： p和p1共同指向同一个地址
     
  2. 删除地址的引用
     del p1  删除p1对地址的引用
     
  3. 查看对地址的引用次数：
      import sys
      sys.getrefcount(p)
      
  4.  当一块空间没有了任何引用，默认执行__del__
       ref =0 
        
'''

class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('------del---------')


p = Person('jack')
p1 = p
p2 = p
print(p1.name)
print(p2.name)

p1.name = 'tom'
print(p.name)
print(p2.name)

print(sys.getrefcount(p))   # 4

del p2
print('删除p2后打印:', p.name)

print(sys.getrefcount(p))  # 3

del p1
print('删除p1后打印:', p.name)

print(sys.getrefcount(p))  # 2

# del p
# print('删除p后打印:', p.name)   #


# 对象赋值
n = 5
n1 = n

print(n)

del n

