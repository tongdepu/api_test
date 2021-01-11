import configparser

cf = configparser.ConfigParser() # 实例化

# read(filename) 读取文件
filename = cf.read(r'G:\api_test\configfile.ini',encoding='utf-8')

# sections() 得到所有的section，以列表形式返回
sec = cf.sections()
print(sec)

# 得到section下的所有option
opt = cf.options("mysql")
print(opt)

# items 得到section的所有键值对
value = cf.items("mysql")
print(value)
print(dict(value)) # 转成字典类型

# get(section,option) 得到section中的option值，返回string/int类型的结果
mysql_host = cf.get("mysql","host")
mysql_password = cf.getint("mysql","port")
print(mysql_host,mysql_password)