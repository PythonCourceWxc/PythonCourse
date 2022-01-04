
a,b=3,5  # a=3 b=5
print(a,b)

# a=3,b=5
# print(a,b)

a=b=c=3
print(a,b,c)


num = int(input('输入四位整数:'))  # 8654

ge = num%10

num = num//10   # 865

shi = num%10

num = num//10  # 86

bai = num%10  

num = num//10  # 8

print(num,bai,shi,ge)

# 

num = 9

if num%2==0:
	print('偶数')
else:
	print('奇数')



num1=8
num2=4

num3=0  # False   任何非0的就是True

if not(num1%num2):  # not True   --->False
	# 条件为True的时候执行的代码块
	print('----------->AAAAAAAAA')
else:
	print('***********>BBBBBBBBB')



if not True:
	print('999999999999')

