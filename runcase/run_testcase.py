'''
  Code description： TestLoader测试case,并执行得到的所有测试集，生成html文件的测试报告
  Create time：2020.8.11
  Developer：
'''
# -*- coding: utf-8 -*-
import HTMLTestRunnerCN     # 导入开源的测试报告生成HTML格式的模块
import os.path
import time
import unittest
import sys
#from common.log import Logger
#logger = Logger(logger="run_case").getlog()
sys.path.append(os.path.dirname(os.path.abspath(".")))   # 将项目主路径添加到系统的环境变量中

# ==============找到最新生成的测试报告文件===========
def new_report(report_path):
    lists = os.listdir(report_path)   # 得到项目目录下所有的文件和文件夹
    lists.sort(key=lambda fn:os.path.getmtime(report_path + '\\' + fn))  # 将得到的文件和文件夹按创建时间排序
    file_new = os.path.join(report_path,lists[-1])  # 获取最新创建的文件
    return file_new
# 测试用例路径
#case_path = os.path.abspath('E:\\api_test\\testcase')
case_path = os.path.dirname(os.path.abspath(".")) + '\\testcase'
print(case_path)
# 测试报告路径
#report_path = os.path.abspath('E:\\api_test\\testreport')
report_path = os.path.dirname(os.path.abspath(".")) + '\\testreport'
print(report_path)
def all_case():
    all_case = unittest.defaultTestLoader.discover(case_path,pattern="api_sheet1*.py",top_level_dir=None)
    print(all_case)
    return all_case
if __name__ == '__main__':
    # 获取当前时间，并格式化时间
    now_time = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    # html测试报告路径
    report_html = os.path.join(report_path,"result_"+now_time+".html")
    fp = open(report_html,'wb')     # 打开一个文件，将测试结果写入该文件中
    '''
    wb:以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，
    即原有内容会被删除。如果该文件不存在，创建新文件
    '''
    runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp,
                                           title=u'API测试报告，测试结果如下：',
                                           description=u'用例执行情况：')

    runner.run(all_case())   # 执行所有测试case
    fp.close()
    # logger.info("api接口测试用例执行完成")