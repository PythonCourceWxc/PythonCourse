'''
	已知两个列表:
	l1 = [5,1,2,9,0,3]
	l2 = [7,2,5,7,9]

	找出两个列表的不同元素

	找出两个列表的共同元素

'''

l1 = [5, 1, 2, 9, 0, 3]
l2 = [7, 2, 5, 7, 9]

s1 = set(l1)
s2 = set(l2)

# 对称差集 

result = (s1 | s2) - (s1 & s2)

print(result)

result = s1 ^ s2  # 两个列表中不一样元素  symmetric_difference()

print(result)

'''
 difference_update()

	 s1 = s1.difference(s2)
	 print(s1)
     相同
	 s1.difference_update(s2)

 intersection_update()  交集并赋值
 union_update()   并集并赋值
 symmetric_difference_update()  对称差集并赋值

'''


s1.difference_update(s2)

print(s1)


'''
 关键字: set
 作用： 去重
 

 符号： - & | ^
 
 内置函数:
  增加: add()  update()
  删除: remove() discard()  pop()  clear()
  运算： difference()  intersection()  union()  symmetric_difference()

'''