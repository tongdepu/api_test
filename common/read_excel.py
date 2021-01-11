'''
  Code description：封装读取excel数据，并设置判断执行哪些行数据
  Create time：2020.8.11
  Developer：tdp
'''
from xlrd import open_workbook
#from common.log import Logger
#logger = Logger(logger="Doexcel").getlog()
class Doexcel():

    # 获取excel表格，并处理表格每行的数据为列表嵌套字典数据形式
    def excel_data_list(self, filename, sheetname):
        '''
        :param filename: excel文件名称
        :param sheetname: excel中表格sheet名称
        :return: data_list
        '''
        data_list = []
        wb = open_workbook(filename)  # 打开excel
        # all_sheet = wb.sheet_names()  # 得到所有的sheet
        sh = wb.sheet_by_name(sheetname)  # 定位工作表
        header = sh.row_values(0)   # 获取标题行的数据
        for i in range(1, sh.nrows):   # 跳过标题行，从第二行开始获取数据
            col_datas = dict(zip(header, sh.row_values(i)))   # 将每一行的数据，组装成字典
            data_list.append(col_datas)   # 将字典添加到列表中 ，列表嵌套字典，每个元素就是一个字典
        return data_list

    # 判断执行哪些行数据
    def get_test_data(self, data_list, case_id):
        '''
        :param data_list: 工作表的所有行数据
        :param case_id: 用例id，用来判断执行哪几条case。如果id=all ，那就执行所有用例；否则，执行列表参数中指定的用例
        :return:  返回最终要执行的测试用例
        '''
        if case_id == 'all':
            final_data = data_list
        else:
            final_data = []
            for item in data_list:
                if item['id'] in case_id:
                    final_data.append(item)
        return final_data
    #logger.info("获取excel数据完成")

if __name__ == '__main__':
    Doexcel()
    """
    data_list = Doexcel().excel_data_list('E:\\api_test\\test_data\\test.xlsx','api_case')
    final_data = Doexcel().get_test_data(data_list, [1,2,3])
    print(final_data)
    """