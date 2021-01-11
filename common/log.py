'''
  Code description：封装日志类，定义日志文件输出格式和日志输出级别
  Create time：2020.8.07
  Developer：
'''
# -*- coding: utf-8 -*-
import logging
import time
import os.path

class Logger(object):
    def __init__(self, logger, CmdLevel=logging.INFO, FileLevel=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)  # 设置日志默认级别为DEBUG
        fmt = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')  # 设置日志输出格式
        currTime = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  # 格式化当前时间
        #log_path = os.path.dirname(os.path.abspath('E:\\api_test\\testcase')) + '/log/'  # 设置日志文件保存路径
        log_path = os.path.dirname(os.path.abspath('.')) + '/log/'      # 相对路径写法
        print('得到的日志路径为：', log_path)
        log_name = log_path + currTime + '.log'  # 设置日志文件名称

        # 设置由文件输出
        fh = logging.FileHandler(log_name, encoding='utf-8')  # 采用utf-8字符集格式防止出现中文乱码
        fh.setFormatter(fmt)
        fh.setLevel(FileLevel)  # 日志级别为INFO
        self.logger.addHandler(fh)  # 添加handler

    def getlog(self):
        return self.logger