'''
  Code description：封装写入excel
  Create time：2020.8.11
  Developer：tdp
'''
from xlutils.copy import copy
from xlrd import open_workbook
import os.path
import configparser

class Write_excel():
    def write_result(self, filename, row, actual_res, test_res,sheet_name):
        '''
        :param filename: 文件名
        :param row: 要写回的行数
        :param actual_res: 实际结果是第9列，测试结果是第10列 ，比如：（2，9）（2，10）
        :param test_res: 测试结果 ：pass/failed
        :param sheet_name:指定的sheet表格
        :return:
        '''
        old_workbook = open_workbook(filename)
        # 将已存在的excel拷贝进新的excel
        new_workbook = copy(old_workbook)
        # 获取sheet
        new_worksheet = new_workbook.get_sheet(sheet_name)  # 第n个表
        # 写入数据
        new_worksheet.write(row, 10, actual_res)
        new_worksheet.write(row, 11, test_res)
        # 保存
        new_workbook.save(os.path.dirname(os.path.abspath(".")) + '\\test_data\\test.xlsx')

if __name__ == '__main__':
    Write_excel()
