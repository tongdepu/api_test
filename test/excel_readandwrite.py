import xlrd
import os
path = (os.path.abspath(".")) + '\\test.xlsx'
file = xlrd.open_workbook(path)
all_sheet = file.sheet_names()  # 获取所有的工作簿名
sheet1 = file.sheet_names()[0]  # 获取第一个工作簿名
print(all_sheet,sheet1)
sh = file.sheet_by_name('统一门户')
sh1 = file.sheet_by_index(0)
row = sh.nrows
col = sh.ncols
print(sh1,row,col)


