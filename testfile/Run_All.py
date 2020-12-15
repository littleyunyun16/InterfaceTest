# -*- coding: utf-8 -*-
__author__ = 'amy'
__date__ = '2020/11/10 16:38'
# 开始执行接口自动化，项目工程部署完毕后直接运行该文件即可

# 开始执行接口自动化，项目工程部署完毕后直接运行该文件即可
import os
import common.HTMLTestRunner as HTMLTestRunner
import getpathinfo
import unittest
import testfile.readconfig as readConfig
from BeautifulReport import BeautifulReport
from common.configEmail import SendEmail
from apscheduler.schedulers.blocking import BlockingScheduler
import pythoncom
import common.log


path = getpathinfo.get_path()
report_path = os.path.join(path, 'result')
on_off = readConfig.ReadConfig().get_email('on_off')
log=common.log.logger


class AllTest:
    def __init__(self):
        self.caseListFile = os.path.join(path,'testfile', 'caselist.txt')  # 配置文件路径，该配置文件配置执行哪些测试文件
        self.caseFile = os.path.join(path, 'testCase')  # 真正的测试断言文件路径
        self.caseList = []  #用例合集
        # log.info('caseListFile', self.caseListFile)
        # log.info('caseFile', self.caseFile)

    def set_case_list(self):
        fb = open(self.caseListFile,encoding='utf-8')  # 可以用with，后续优化吧
        for value in fb.readlines():
            data = str(value)
            if data !='' and not data.startswith('#'):
                self.caseList.append(data.replace('\n', ''))
        fb.close()

# TestSuite组件将多个用例集合到一起，添加用例到列表，addTest方法将TestCase添加到TestSuite中
    def set_case_suite(self):
        self.set_case_list()  # 通过set_case_list()拿到caselist元素组
        test_suite = unittest.TestSuite()  # 该组件主要将用例组合到一起
        '''
        下面for语句主要获得TestCase,并利用
        '''
        suite_module = []
        for case in self.caseList:
            case_name = case.split('/')[-1]
            print(case_name + '.py')
            # 利用了unittest.defaultTestLoader.discover来批量加载用例
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)
            # print('suite_module:' + str(suite_module))
        if len(suite_module) > 0:
            for suite in suite_module:  # 如果存在，循环取出元素组内容，命名为suite
                for test_name in suite:  # 从discover中取出test_name，使用addTest添加到测试集
                    test_suite.addTest(test_name)
        else:
            print('else:')
            return None
        return test_suite

    def run(self):
        try:
            suit = self.set_case_suite()
            if suit is not None:
                # 调用HTMLTestRunner
                result=BeautifulReport(suit)
                result.report(filename='test_report', description='接口自动化测试报告', log_path=report_path)

            else:
                print("Have no case to test.")
        except Exception as ex:
            print(str(ex))
            # log.info(str(ex))
        finally:
            print("*********TEST END*********")
            # log.info("*********TEST END*********")

if __name__ == '__main__':
    AllTest().run()



