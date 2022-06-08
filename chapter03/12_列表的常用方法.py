# list01.py
# 列表的函数:
'''
字符串函数：
'abc'.split('-')
['a','b','c'].split('-')错误

列表函数：只有通过列表才可以调出来的函数

添加： append  extend  insert
删除: del list[index]
      remove(e)   删除列表中第一次出现的元素e，返回值是None。
      			  如果没有找到要删除元素则报出异常
      pop()：  弹栈  移除列表中的最后一个元素,返回值是删除的那个元素
			   默认是删除最后一个，但是也可以指定index（下标）删除

	  clear()： 清除列表（里面的所有元素全部删除）
翻转:
      reverse()

排序:
      sort()

次数:
      count()



'''

hotpot_list = ['海底捞', '呷哺呷哺','张亮麻辣烫','热辣一号','宽板凳']

hotpot_list.append('张亮麻辣烫')

print(hotpot_list)

# result = hotpot_list.remove('杨国福麻辣烫')

# print(result)

# print(hotpot_list)


result = hotpot_list.pop()
print(result)
print(hotpot_list)

result = hotpot_list.pop(2)

print(hotpot_list)

# result = hotpot_list.clear()

# print(result)
# print(hotpot_list)



print(hotpot_list[::-1]) # 只是逆序拿出列表中的元素，打印出来
print(hotpot_list)


hotpot_list.reverse()  # 改变了列表的位置结构
print(hotpot_list)


# 系统提供的排序
'''
sorted(list，revers=True|False)

list.sort(revers=True|False)
类似：
 
'''

l = [4,8,1,8,9,5,7]

l.sort(reverse=True)  # 升序

print(l)


print(l.count(8))