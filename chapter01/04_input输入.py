#输入：input()

# name = input()

# print(name)


# name = input('请输入名字:')  # 阻塞式 

# print(name)


'''
练习:
游戏：捕鱼达人

输入参与游戏者用户名:
输入密码：

充值： 500



'''



print('''
*********************
      捕鱼达人
*********************
	''')

username = input('输入参与游戏者用户名:')
password = input('输入密码：')

print('%s请充值才能加入游戏!' % username)


coins = input('请充值:')   # input键盘输入的都是字符串类型  即使输入的是500，他也会添加‘500’
# print(type(coins))  # '500'
coins = int(coins)   

print('%s充值成功！当前游戏币是:%d' %(username,coins))

'''
 游戏： 英雄联盟
 角色： xxx
 拥有的装备：xxx 
 购买装备： xxx  
 付款金额： xxx

 xxxx 拥有xxxx装备，花了xxx钱
'''



