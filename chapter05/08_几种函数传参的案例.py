'''
练习:
1.
def func(a,*args):
    print(a,args)

调用:
func(2,3,4,5)      2 (3,4,5)

func(2,[1,2,3,4])  2 ([1,2,3,4],)

func(2,3,[1,2,3,4,5])  2 (3,[1,2,3,4])

func(5,6,(4,5,7),9)  5 (6, (4, 5, 7), 9)

2.
def func(a,b=10,c=3,**kwargs):   关键字默认值
    print(a,b,c,kwargs)

func(1)  1 10  3  {}

func(2,b=10)  2 10  3 {}

func(3,5,7,a=1,b=2)  报错

func(3, c=5, b=7, x=1, y=2)  # 3 5 7 {'x': 1, 'y': 2}

3.
def func(a,*args,**kwargs):
    print(a,args,kwargs)

t=(1,2,3,4)
func(1,t)

l=[2,5,8]
func(1,l,a=9,b=6)

'''


# def func(a, *args):
#     print(a, args)
#
#
# func(2, [1, 2, 3, 4],5,'hello')
# func(5,6,(4,5,7),9)


# def func(a, b=10, c=3, **kwargs):
#     print(a, b, c, kwargs)
#
#
# func(1)  # 1 10 3 {}
#
# func(2, b=11)  # 2 11 3 {}
#
# func(3, c=5, b=7, x=1, y=2)  # 3 5 7 {'x': 1, 'y': 2}


def func(a, *args, **kwargs):
    print(a, args, kwargs)


t = (1, 2, 3, 4)
func(1, t)  # 1 ((1,2,3,4),)

l = [2, 5, 8]
func(1, l, c=9, b=6)  # 1 ([2, 5, 8],) {'c': 9, 'b': 6}

dict1 = {'1': 'a', '2': 'b', '3': 'c'}
func(1, *l, **dict1)
# func(1,2,5,8,1='a',2='b',3='c')
'''
courses = ['html','mysql','python']


'''


def func1(name, *args):
    if len(args) > 0:
        for i in args:  # ('html','mysql','python')
            print('{}学过了{}'.format(name, i))
    else:
        print('没有学任何编程知识！')


courses = ['html', 'mysql', 'python']

# 调用函数
func1('坤坤', *courses)  # 拆包


'''
无参数函数:

def func():
    pass

func()  ---->调用
  
有参数函数:
  1. 普通参数
  
  def func(name,age):
        pass
  
  func('aa',18)   ----> 形参与实参的个数要一致
  
  
  2. 可变参数:
   A. def func(*args):
          pass
          
      func()  ----> 函数调用时，实参的个数可以没有，也可以多个   *不能是关键字参数
      func(4)  func(5,'h')
  
  
  B. def  func(**kwargs):
         pass
        
     func(a=1,b=2)  ----> 函数调用时，实参的个数可以没有，也可以多个   **必须是关键字参数

  C. def func(*args,**kwargs):
         pass
    
    list1 = [1,3]
    dict1 = {'1':'a','2':'b'}
    func(*list1,**dict1)  # func(1,3,'1'='a','2'='b')
     
  D. 混用
  
  def func(name,*args,**kwargs):
        pass
        
  func('tom')   ----> 必须赋值

  3. 默认值+关键字
  
  def func(name,age=18):
        pass
        
  func('tom')  ----》 tom  18
  
  func('tom',age=20)   --->关键字赋值
  
  

'''
