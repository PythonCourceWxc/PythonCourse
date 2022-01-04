'''

  words = ['hello','good','apple','world','digit','alpha']

  提示输入一个单词比如：hello，如果输入的单词在列表中则删除

  最后打印删除后的列表

'''

words = ['hello','good','gooo','world','digot','alpha']

w = input('请输入一个单词：')

# 方式1：
# if w in words:
# 	print('存在次单词')

#    'abc'  in ['abc','hello','aaaa',..] 内容有没有在列表中存在   
 #    'go'  in  'good'  判断字符串w有没有出现在word 
# for word in words:  
# 	if w == word:     # ==   'go'=='good'           in 
# 		print('存在此单词！')
# 		break


# for word in words:
# 	if w in word:
# 		del word
# 		break

# print(words)

words = ['hello','goods','gooo','world','digot','alphago']

w = input('请输入一个单词：')

i = 0  # 表示下标

l = len(words)  # 5

while i<l: #  i<5
	if w in words[i]:
		del words[i]
		l-=1
		# i-=1
		continue
		
	i+=1

print(words)



