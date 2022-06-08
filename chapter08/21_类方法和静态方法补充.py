'''
类方法，静态方法：
工具方法
类方法:
    定义格式:
        @classmethod
        def 类方法名(cls,参数):
            pass
    使用：
        类名.方法名()
        也可以通过：
        对象.方法名() (了解)
静态方法：类似类方法
   定义格式：
       @staticmethod
       def 方法名():
            pass
   使用:
      类名.方法名()
'''


class Utils:
    # 类属性
    version = '1.0'



    # 类方法
    @classmethod
    def conn_db(cls):  # cls其实就是类对象本身
        print('classmethod---->', cls)
        print('加载数据库驱动程序，当前版本号是:', cls.version)
        print('数据库建立连接成功！')

        # cls.select_data()

    @staticmethod
    def select_data():  # 参数：不依赖对象self，也不依赖类cls
        print('查询数据库的数据，当前版本号是:', Utils.version)
        Utils.conn_db()


# Utils.conn_db()   # 类方法的调用
# print('Utils:', Utils)
# # 类方法能否被对象调用？ 能访问
#
# u = Utils()
# u.conn_db()  # 对象调用conn_db(cls)  --->cls仍然是<class '__main__.Utils'>
# print('u===:', u)

# 类方法方法中能否访问对象属性？


# 静态方法的调用：
Utils.select_data()

# 静态方法能否被对象调用？ 能访问
u = Utils()
u.select_data()

# 类方法中能否调用静态方法？  静态方法中能否调用类方法？  都可以
print('-----------------------------------')
# Utils.conn_db()

# 类方法，静态方法中能调用普通方法？
