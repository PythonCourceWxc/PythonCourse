# 写文件
'''
stream = open(r'c:\p1\aa.txt', 'w')
mode 是’w‘ 表示就是写操作  每次都会将原来的内容清空，

方法:
     write(内容)   然后写当前的内容
    writelines(Iterable)  没有换行效果
    stream.writelines(['赌神高进\n', '赌侠小刀\n', '赌圣周星星\n'])  ---》自己加

如果mode='a'


'''

import os
def get_path():
    return os.getcwd().replace('\\', '/')
stream = open(r'' + get_path() + '/p1/aa.txt', 'a', encoding='utf-8')

# s = '''
# 你好！
#     欢迎来到澳门博彩赌场，赠送给你一个金币！
#                 赌王: 高进
#
# '''

result = stream.write('hello')
# print(result)

stream.write('龙五')

stream.writelines(['赌神高进\n', '赌侠小刀\n', '赌圣周星星\n'])

stream.write('僵尸先生')

stream.close()  # 释放资源

# stream.write('龙五2号')


