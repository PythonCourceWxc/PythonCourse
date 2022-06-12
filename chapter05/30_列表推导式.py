'''
列表推导式:
格式： [表达式 for i in list|set|tuple|dict [if 条件]]
格式： [表达式1 if 条件 else 表达式2 for i in list|set|tuple|dict]
格式:  [表达式1 for x in list|set|tuple|dict for y in list|set|tuple|dict]
'''

list1 = [8, 9, 0]
list2 = [x + 1 for x in list1 if x % 2 == 0]
print(list2)

'''
list2 =[]
for x in list1:
    if x%2==0:
        list2.append(x+1)
    else:
        list2.append(x+2)
    
'''

list3 = [x + 1 if x % 2 == 0 else x + 2 for x in list1]
print(list3)  # [3, 5, 7, 9, 9, 11, 5]

list0 = [1, 2, 3]

list4 = [(x, y) for x in list0 for y in list1]
print(list4)
'''
l =[]
 for x in list0:
    for y in list1:
        t = (x,y)
        l.append(t)

'''
