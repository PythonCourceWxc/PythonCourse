# 声明
names = ['jack','tom','lucy','superman','ironman']  # 列表

computer_brands = []


# 增删改查

# 地址

print(id(names))
print(id(computer_brands))

# 查: 通过下标
# 元素获取使用： 下标  索引
print(names[0])
print(names[1])

# 获取最后一个元素
print(names[-1])

print(len(names))

print(names[len(names)-1])

#获取第一个元素
print(names[-5])


# 结合循环
# for i in 'hello':
# 	print(i)
print('***************')
for name in names:
	print(name)

# 查询names里面有没有保存超人
for name in names:  # name = jack   name=tom

	if name == 'superman':
		print('有超人在里面！')
		break
else:
	print('没有找到超人在里面！')


# 简便  't' in 'they'  ----> True  False

if 'superman' in names:   # 判断有没有
	print('有超人在里面！')
else:
	print('没有找到超人在里面！')





