# 冒泡排序（两两比较，每轮找出一个最大值放到最后，下一轮找出第二大放在倒数第二个位置，以此类推）

# 外层循环控制的轮数，内层循环控制的两两比较。

myList = [4, 1, 7, 0]

for i in range(len(myList)-1):    
    # 每一轮的比较,注意range的变化,这里需要进行length-1-长的比较,注意-i的意义(可以减少比较已经排好序的元素)
    for j in range(0, len(myList)-1-i):
         # 交换
         if myList[j] > myList[j+1]:
             myList[j], myList[j+1] = myList[j+1], myList[j]

print(myList)


'''
随机生成10个数，使用算法进行排序(降序)

'''
import time
start = time.time()  # 时间戳
# 运算过程
end = time.time()

cha = end-start

# 时间差就是cha



