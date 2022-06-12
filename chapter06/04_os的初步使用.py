# 模块： os.py
import random
'''
os.path:
os.path.dirname(__file__)获取当前文件所在的文件目录（绝对路径）
os.path.join(path,'')  返回的是一个拼接后的新的路径

'''

import os

# print(os.path)
# path = os.path.dirname(__file__)  # 获取当前文件所在的文件目录（绝对路径）
# print(path)
# print(type(path))
# result = os.path.join(path, 'a1.jpg')
# print(result)
# p1\girl.jpg ---->保存在当前文件所在的目录


def get_path():
    return os.getcwd().replace('\\', '/')

with open(r'' + get_path() + '/p1/test.png', 'rb') as stream:
    container = stream.read()  # 读取文件内容
    print(stream.name)
    file = stream.name
    filename = file[file.rfind('\\')+1:]  # 截取文件名

    path = os.path.dirname(__file__)
    path1 = os.path.join(path, filename)

    with open(path1, 'wb') as wstream:
        wstream.write(container)
