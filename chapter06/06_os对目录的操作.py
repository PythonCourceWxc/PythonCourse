# os.path里面函数
# os中函数：
import os

dir = os.getcwd()
print(dir)

all = os.listdir(r'E:\PyCharmProjects\PythonCourseWxc\PythonCourse\chapter06\p1')  # 返回指定目录下的所有的文件和文件夹,保存到列表中
print(all)

# 创建文件夹
if not os.path.exists(r'E:\PyCharmProjects\PythonCourseWxc\PythonCourse\chapter06\p2'):
    f = os.mkdir(r'E:\PyCharmProjects\PythonCourseWxc\PythonCourse\chapter06\p2')
    print(f)

# f = os.rmdir(r'c:\p3')  # 只能删除空的文件夹  OSError: [WinError 145] 目录不是空的。: 'c:\\p3'
# print(f)

# f = os.removedirs(r'c:\p3')
# print(f)

# os.remove(r'c:\p3\p4\aa.txt')

# 删除p4文件夹
# path = r'c:\p3\p4'
#
# filelist = os.listdir(path)   #['a1.doc', 'aa.txt', 'girl.jpg']
#
# for file in filelist:
#     path1 = os.path.join(path,file)
#     os.remove(path1)
# else:
#     os.rmdir(path)
#
# print('删除成功！')

# 切换目录

path = os.getcwd()
print(path)

f = os.chdir(r'E:\PyCharmProjects\PythonCourseWxc\PythonCourse\chapter06\p1')
print(f)

path = os.getcwd()
print(path)

'''
os模块下方法:
os.getcwd()  获取当前目录
os.listdir()  浏览文件夹
os.mkdir()  创建文件夹
os.rmdir()  删除空的文件夹
os.remove()  删除文件
os.chdir()  切换目录

'''
