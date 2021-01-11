"""
import pymysql
# 建立连接
connection = pymysql.connect(host='119.29.78.234', port=3306, user='root', password='dhcc@2020', db='test123')
cursor = connection.cursor()       # 创建游标
cursor.execute("SELECT * FROM userinfo")   #使用execute()方法执行SQL语句
data = cursor.fetchall()  #使用fetall()获取全部数据
print(data)
cursor.close()   #关闭游标和数据库的连接
connection.close()
"""
'''数据库增删改操作'''
# mysql插入数据
import pymysql
db_config = {
      "host":"119.29.78.234",
       "port":3306,
       "user":"root",
       "password":"dhcc@2020",
       "db":"test123"
}
db = pymysql.connect(**db_config)
cursor = db.cursor()
sql = "INSERT INTO userinfo(username,passwd) VALUES('克莱','123')"
#sql = "UPDATE userinfo SET username = '奥尼尔' WHERE username = '科比'"  # 修改数据
#sql = "DELETE FROM username WHERE username ='奥尼尔'"                    # 删除数据
try:
    cursor.execute(sql)
    db.commit()
except Exception as e :   # 执行异常回滚
    db.rollback()
cursor.close()
db.close()
#或者在execute提供需要插入的数据
import pymysql
db_config = {
      "host":"119.29.78.234",
       "port":3306,
       "user":"root",
       "password":"dhcc@2020",
       "db":"test123"
}
db = pymysql.connect(**db_config)
cursor = db.cursor()
sql = "INSERT INTO userinfo(username,passwd) VALUES(%s,%s)"
try:
    cursor.execute(sql,("克莱","123"))
    db.commit()
except Exception as e :
    db.rollback()
cursor.close()
db.close()
#批量插入数据
import pymysql
db_config = {
      "host":"119.29.78.234",
       "port":3306,
       "user":"root",
       "password":"dhcc@2020",
       "db":"test123"
}
db = pymysql.connect(**db_config)
cursor = db.cursor()
sql = "INSERT INTO userinfo(username,passwd) VALUES(%s,%s)"
try:
    cursor.executemany(sql,[("韦德","123"),("字母哥","123")])
    db.commit()
except Exception as e :
    db.rollback()
cursor.close()
db.close()

"""
# 查询数据
import pymysql
db_config = {
      "host":"119.29.78.234",
       "port":3306,
       "user":"root",
       "password":"dhcc@2020",
       "db":"test123"
}
db = pymysql.connect(**db_config)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
sql = "SELECT * FROM userinfo"
cursor.execute(sql)
res = cursor.fetchall()   # 第一次查询表中的所有数据
print(res)
res = cursor.fetchall()    # 第二次查询无数据
print(res)
cursor.close()
db.close()
"""

import pymysql.cursors

class Operation_mysql(object):
    def __init__(self):
        # 建立连接
        db_config = {
            "host": "119.29.78.234",
            "port": 3306,
            "user": "root",
            "password": "dhcc@2020",
            "db": "test123"
        }
        self.connection = pymysql.connect(**db_config)
        # 创建游标
        self.cursor = self.connection.cursor()

    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:  # 执行异常回滚
            db.rollback()

    def get_data(self):
        data = self.cursor.fetchone()
        #data = self.cursor.fetchall() # 查询所有数据
        return data

    def close_mysql(self):
        # 关闭游标
        self.cursor.close()
        # 关闭数据库连接
        self.connection.close()
if __name__ == "__main__":
    Operation_mysql()
    """
    test = Operation_mysql()
    sql = "SELECT * FROM t_iot_portal_sys ORDER BY create_time DESC;"
    test1 = test.execute_sql(sql)
    test2 = test.get_data()[0]
    print(test2)
    """




