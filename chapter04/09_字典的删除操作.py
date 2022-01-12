# 增加  改  查 （key）删除
# 删除:
list1 = [3, 7, 9, 0]

del list1[1]

print(list1)


dict1 = {'张三': 100, '李四': 100, '王五': 89, '赵柳': 99}

del dict1['王五']

print(dict1)

# del dict1['haha']  # keyError

# 字典的内置函数：删除
# dict1.remove('李四')  不存在   报错的
# pop(key[,default]) ----> 根据key删除字典中的键值对，返回值是   只要删除成功，则返回键值对的值value
#                          pop的默认值，往往是在删除的时候没有找到对应的key，则返回default默认值

result = dict1.pop('李四', '80')
print(result)

result = dict1.pop('张小三', '字典中没有此键')
print('======>',result)

print(dict1)


print('*'*30)
# popitem():随机删除字典中键值对（一般是从末尾删除元素）  

dict1 = {'张三': 100, '李四': 100, '王五': 89, '赵柳': 99}

result = dict1.popitem()
print(result)

print(dict1)

result = dict1.popitem()
print(result)

print(dict1)


# clear() 同列表的clear()

dict1.clear()

print(dict1)

'''
删除:
del dict[key]

dict.pop(key[,default])

dict.popitem()

dict.clear()

'''


'''
其他的内置函数:
update()    []+[]  合并操作
fromkeys(seq,[default])  ---->将seq转成字典的形式 如果没有指定默认的value则用None
          new_dict = dict.fromkeys(list1）---》      {'aa': None, 'bb': None, 'cc': None}
                         ---> 如果指定default，则用default替代None这个value值
		new_dict = dict.fromkeys(list1,10)	---》	  {'aa': 10, 'bb': 10, 'cc': 10}

'''

# dict1 = dict1+dict2   报错的
# print(dict1)

dict1 = {0: 'tom', 1: 'jack', 2: 'lucy'}

dict2 = {0: 'lily', '4': 'ruby'}

result = dict1.update(dict2)
print(result)

print(dict1)

list1 = ['aa', 'bb', 'cc']
new_dict = dict.fromkeys(list1, 10)
print(new_dict)








