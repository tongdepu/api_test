import pymysql.cursors
#连接MySQL数据库
connection = pymysql.connect(host='119.29.78.234', port=3306, user='root', password='dhcc@2020', db='iotdata-test', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

#通过cursor创建游标
cursor = connection.cursor()
# 执行数据查询
sql = "SELECT * FROM t_iot_portal_sys ORDER BY create_time DESC;"
cursor.execute(sql)
#查询数据库单条数据
result = cursor.fetchone()
print(result)
print(result["id"])

# 关闭数据连接
connection.close()