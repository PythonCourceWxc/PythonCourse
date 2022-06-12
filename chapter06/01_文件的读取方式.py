# 文件操作:
'''
 文件上传
 保存log

系统函数：
 open(file,mode,buffering,encodeing)

 读:
   open（path/filename,'rt'）---->返回值：stream (管道)

   container = stream.read()  ---->读取管道中内容

   注意： 如果传递的path/filename有误，则会报错：FileNotFoundError
    如果是图片则不能使用默认的读取方式,mode = 'rb'

    总结:
    read()  读取所有内容
    readline() 每次读取一行内容
    readlines() 读取所有的行保存到列表中
    readable()  判断是否可读的

'''
import os

def get_path():
    return os.getcwd().replace('\\', '/')

def file_exits():
    currentPath = get_path()
    path = currentPath + '/p1/aa.txt'
    stream = open(r'' + path, encoding='utf-8')
    result = stream.readable()  # 判断是否可以读取  True  False
    print(result)

    lines = stream.readlines()  # 保存到列表中
    print(lines)
    for i in lines:
        print(i)

file_exits()

stream = open(r'E:\PyCharmProjects\PythonCourseWxc\PythonCourse\chapter06\p1\test.png', 'rb')

container = stream.read()
# print(container)
