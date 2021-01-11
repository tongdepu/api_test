#在mysql中使用"--"代表注释，
#小程序代码如下：
import pymysql
user = input("username:")
pwd = input("password:")
config={"host":"119.29.78.234",
       "port":3306,
       "user":"root",
       "password":"dhcc@2020",
       "db":"test123"
        }
db = pymysql.connect(**config)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
sql = "select * from userinfo where username='%s' and passwd='%s'" %(user,pwd)
result=cursor.execute(sql)
cursor.close()
db.close()
if result:
    print('登录成功')
else:
    print('登录失败')




