'''
  Code description：
  Create time：2020.8.11
  Developer：tdp
'''
# 导入
import unittest
import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# import configparser   # 引入解析配置文件模块
import os.path
from ddt import ddt,data   # 引入ddt模块
from common.read_excel import Doexcel
from common.read_configfile import ReadConfig
from common.operation_mysql import Operation_mysql
# import math
from common.write_excel import Write_excel
write = Write_excel()
sheet = ReadConfig()
sheet_data = sheet.get_sheet("sheet3")  # 需要测试哪个sheet就改成对应sheet
data_list = Doexcel().excel_data_list(os.path.dirname(os.path.abspath(".")) + '\\test_data\\test.xlsx',sheet_data)
test_data = Doexcel().get_test_data(data_list, "all")  # 执行所有行用例
#test_data = Doexcel().get_test_data(data_list, [1,2,3]) # 执行指定行用例，如执行excel中第1/2/3条用例

@ddt
class TestAPI (unittest.TestCase):   # 类必须以Test开头，继承TestCase

    def setUp(self):
        print("======开始执行测试用例======")

    def tearDown(self):
        print("======测试用例执行完毕======")

    # 测试用例
    @data(*test_data)
    def test_api(self,data_itme):     # 测试用例脚本方法必须以test开头
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        }
        config = ReadConfig()
        cookie = config.get_cookie("data")
        cookie_dict = {i.split("=")[0]: i.split("=")[-1] for i in cookie.split("; ")}
        # 发送请求，判断请求方式
        if str.lower(data_itme['method']) == 'get':     # str.lower() 将字符串中所有的大写转换成小写
            if data_itme['params'] != '' and data_itme['header'] != '':       # 如果excel表格中的params单元格不为空，则传参
                json_data = json.loads(data_itme['params']) # 将json格式数据转换为字典
                new_header = dict(headers,**json.loads(data_itme['header']))
                r = requests.get(data_itme['url'], headers=new_header, params=json_data, cookies=cookie_dict,
                             verify=False)
            elif data_itme['params'] != '' and data_itme['header'] == '':       # 如果excel表格中的params单元格不为空且header为空
                json_data = json.loads(data_itme['params']) # 将json格式数据转换为字典
                r = requests.get(data_itme['url'], headers=headers, params=json_data, cookies=cookie_dict,
                             verify=False)
            elif data_itme['params'] == '' and data_itme['header'] != '':       # 如果excel表格中的params单元格为空且header不为空
                new_header = dict(headers, **json.loads(data_itme['header']))
                r = requests.get(data_itme['url'], headers=new_header, cookies=cookie_dict,
                             verify=False)
            else:           # 为空，表示该get请求不传递任何参数
                r = requests.get(data_itme['url'], headers=headers, cookies=cookie_dict,
                                 verify=False)
                print("添加请求返回的数据为：",r.json()["code"])

        elif str.lower(data_itme['method']) == 'post':
            if data_itme['data'] != ''and data_itme['header'] != '':   # excel 中有header有data
                json_data = json.loads(data_itme['data'])
                new_header = dict(headers, **json.loads(data_itme['header']))
                r = requests.post(data_itme['url'], headers=new_header, json=json_data, cookies=cookie_dict,
                                  verify=False)
            elif data_itme['data'] != ''and data_itme['header'] == '':  # excel 中无header有data
                json_data = json.loads(data_itme['data'])
                r = requests.post(data_itme['url'], headers=headers, json=json_data, cookies=cookie_dict,
                                  verify=False)
            else:
                r = requests.post(data_itme['url'], headers=headers, cookies=cookie_dict,
                              verify=False)
        elif str.lower(data_itme['method'])== 'put':
            if data_itme['data'] != '':
                json_data = json.loads(data_itme['data'])
                print("得到的原始数据为：", json_data)
                test = Operation_mysql()
                sql = data_itme["sql"]
                test1 = test.execute_sql(sql)
                test2 = test.get_data()[0]
                json_data["id"] = test2  # 将数据库获取的id赋值给excel中的id
                print("得到的新数据为：", json_data)
                r = requests.put(data_itme['url'], headers=headers, json=json_data, cookies=cookie_dict,
                                 verify=False)
            else:
                r = requests.post(data_itme['url'], headers=headers, cookies=cookie_dict,
                                  verify=False)
        elif str.lower(data_itme['method'])== 'delete':
            if data_itme['data'] != "":
                json_data = json.loads(data_itme['data'])
                r = requests.delete(data_itme['url'], headers=headers, json=json_data, cookies=cookie_dict,
                                 verify=False)
            else:
                test3 = Operation_mysql()
                sql1 = data_itme["sql"]
                test4 = test3.execute_sql(sql1)
                test5 = test3.get_data()[0]
                print(test5)
                new_url = data_itme['url'] + str(test5)   # 拼接url
                print("拼接后的url为：",new_url)
                r = requests.delete(new_url, headers=headers, cookies=cookie_dict,
                             verify=False)
        # 获取响应体：一般是转成json格式，和响应状态码
        response_data = r.json()
        code = response_data["code"]
        print(response_data)
        # 接口断言判断:响应码判断
        config = ReadConfig()
        code_data = config.get_code("code")
        # print("获取的配置文件的code",code_data)
        try:
            assert code == int(code_data)
            print('接口测试通过')
            test_res = "pass"
        except Exception as e:
            print('返回失败，接口测试异常', format(e))
            test_res = "failed"
        finally:
            write.write_result(os.path.dirname(os.path.abspath(".")) + '\\test_data\\test.xlsx',int(data_itme['id']),str(response_data),str(test_res),2)

    if __name__ == '__main__':
         unittest.main()


