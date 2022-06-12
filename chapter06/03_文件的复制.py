# 文件的复制
'''
原文件： c:\p1\girl.jpg
目标文件： c:\p2\girl.jpg

with 结合open使用，可以帮助我们自动释放资源

'''
# stream = open(r'c:\p1\girl.jpg', 'rb')
import os

def get_path():
    return os.getcwd().replace('\\', '/')

with open(r'' + get_path() + '/p1/test.png', 'rb') as stream:
    container = stream.read()  # 读取文件内容

    with open(r'' + get_path() + '/p1/test2.png', 'wb') as wstream:
        wstream.write(container)

print('文件复制完成！')
