'''
  Code description：封装读取配置文件
  Create time：2020.8.13
  Developer：tdp
'''

import configparser
import os

class ReadConfig():
    def __init__(self, filepath=None):

        root_dir = os.path.dirname(os.path.abspath('.'))        # 获取项目主路径
        # print("打印",root_dir)
        configpath = os.path.join(root_dir, "configfile.ini")  # 拼接路径
        # print("得到的路径为",configpath)
        self.cf = configparser.RawConfigParser()
        self.cf.read(configpath,encoding='utf-8')
    def get_cookie(self, param):
        value = self.cf.get("cookie", param)
        return value
    def get_sheet(self,param):
        value = self.cf.get("sheet",param)
        return value
    def get_mysql(self,param):
        value = self.cf.get("mysql",param)
        return value
    def get_code(self,param):
        value = self.cf.get("code",param)
        return value


if __name__ == '__main__':
    test = ReadConfig()
    t = test.get_cookie("data")
    m = test.get_sheet("sheet1")
    print(t,m)
