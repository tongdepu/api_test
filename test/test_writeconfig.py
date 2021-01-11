import configparser

conf = configparser.ConfigParser()
conf.read(r'G:\api_test\configfile.ini',encoding='utf-8')

conf.set("code", "code", "6666")  # 修改指定section 的option
conf.set("code", "age", "123")  # 增加指定section 的option
conf.has_section("code")
conf.has_option("code","age")
#conf.remove_section("test")
#conf.remove_option("test","haha")
if 'test' not in conf.sections():
    conf.add_section("test")  # 增加section
    conf.set("test", "haha", "123")  # 给新增的section 写入option
file = open(r'G:\api_test\configfile.ini', 'w',encoding='utf-8')
conf.write(file)
file.close()

