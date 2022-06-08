import random
list1 = []
i = 0
while i < 10:
    a = random.randint(1, 20)
    if a not in list1:
        list1.append(a)
    else:
        i -= 1
    i += 1
print(list1)
print('=============================')

for i in range(len(list1)-1):
    for j in range(i+1, len(list1)):
        print('----------++++>', j)
        if list1[i] < list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
            print(list1)
    print('----------------->', i)
print(list1)
