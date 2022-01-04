# 增删改

brands = ['hp','dell','thinkpad','支持华为','lenovo','mac pro','神州']  # HASEE

# 改
print(brands)

print(brands[-1])

brands[-1]='HASEE'   # 赋值  步骤：1.找到（使用下标）  2. 通过=赋值  3.新的值覆盖原有的值

print(brands)


print('-------------------')
# HUAWEI

# for brand in brands:
# 	if '华为' in  brand:
# 		brand= 'HUAWEI'

# print(brands)


for i in range(len(brands)):
	# i是0,1,2,3，。。。 ---》 下标
	if '华为' in brands[i]:
		brands[i]='HUAWEI'
		break

print(brands)



# 删除  del  是 delete的缩写

del brands[2]

print(brands)


# 删除 只要是 hp ， mac 都要删除
print('-----------删除---------------')
# l=len(brands)

# for i in range(l):
# 	if 'hp' in brands[i] or 'mac' in brands[i]:
# 		del brands[i]
# 		# break

# print(brands)


l=len(brands)
i=0
while i<l:
	if 'hp' in brands[i] or 'mac' in brands[i]:
		del brands[i]
		l-=1  # 长度的减少

	i+=1  # 下标的增加

print(brands)


'''
  They are students
  yews


  words = ['hello','good','apple','world','digit','alpha']

  提示输入一个单词比如：hello，如果输入的单词在列表中则删除

  最后打印删除后的列表


'''

w = 'helloaa'

if 'll' in w:
	print('zai')