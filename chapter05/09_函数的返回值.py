# 返回值：将函数中运算的结果通过 return 关键字 ‘扔’出来

def add(a, b):
    result = a + b

    print(result)

    return 'hello', result


# 调用函数

x, y = add(2, 6)
print(x, y)

'''
return 返回值
1. return后面可以是一个参数   接收的时候x=add(1,2)
2. return 后面也可以是多个参数， 如果是多个参数则底层会将多个参数先放在一个元组中，
   将元组作为整体返回    x= add(1,2)   x ---> (1,2,3)
3. 接收的时候也可以是多个： return 'hello','world'    x,y = ('hello','world')  ---> x='hello'  y='world'

'''

'''
 加入购物车
 判断用户是否登录，如果登录，成功加入购物车，否则提示请登录之后添
 
 成功 True   不成功  False
 
 def add_shoppingcart(goodsName):
    pass
    
 def login(username,password):
    pass
 
  调用
'''
