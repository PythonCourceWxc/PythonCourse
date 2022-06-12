# with open('a1.txt', 'w') as wstream:
#     wstream.write('hello')

import os

r = os.path.isabs(r'E:\PyCharmProjects\PythonCourseWxc\PythonCourse\chapter06\p1\test.png')
print('----》', r)


r = os.path.isabs('p1/girl.jpg')  # 找跟file01.py同级的images里面的girl.jpg
print('----->', r)

# 获取路径：directory 目录  文件夹
# 当前文件所在文件夹路径
path = os.path.dirname(__file__)
print(path)

# 通过相对路径得到绝对路径
path = os.path.abspath('aa.txt')
print(path)

# 获取当前文件的绝对路径
path = os.path.abspath(__file__)
print(path)

path = os.getcwd()  # 类似 os.path.dirname(__file__)
print(path)

r = os.path.isfile(os.getcwd())
print(r)

r = os.path.isdir(os.getcwd())
print(r)

# os.path

path = r'E:\PyCharmProjects\PythonCourseWxc\PythonCourse\chapter06\p1\test.png'

result = os.path.split(path)

print(result)  # ('C:\\Users\\running\\Desktop\\python基础\\day13(6-14)\\代码\\day13_文件\\code\\aa', '05_os模块的方法使用.py')
print(result[1])
# filename = path[path.rfind('\\')+1:]

result = os.path.splitext(path)  # 分割文件与扩展名
print(result)
# ('C:\\Users\\running\\Desktop\\python基础\\day13(6-14)\\代码\\day13_文件\\code\\aa\\file01', '.py')

size = os.path.getsize(path)  # 获取文件的大小  单位字节
print(size)

result = os.path.join(os.getcwd(), 'file', 'a', 'a1.jpg')
print(result)
'''
os.path: 常用函数
 dirname()
 join()
 split()
 splittext()
 getsize()
 
 isabs()
 isfile()
 isdir()
 
 


'''
