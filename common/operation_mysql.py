'''
  Code description：封装操作mysql数据库
  Create time：2020.9.11
  Developer：tdp
'''

import pymysql.cursors
from common.read_configfile import ReadConfig
mysql_data = ReadConfig()

class Operation_mysql(object):
    def __init__(self):
        # 建立连接
        self.connection = pymysql.connect(host=mysql_data.get_mysql("host"), port=int(mysql_data.get_mysql("port")), user=mysql_data.get_mysql("user"), password=mysql_data.get_mysql("password"), db=mysql_data.get_mysql("db"))
        # 创建游标
        self.cursor = self.connection.cursor()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def get_data(self):
        data = self.cursor.fetchone()
        #data = self.cursor.fetchall() # 查询数据
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