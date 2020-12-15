# 读取usercase.xlsx中的用例，用unittest来进行断言校验



import os
import unittest
import json
import ddt
import getpathinfo
import urllib.parse
from common.configHttp import RunMain
from testfile.readExcel import ReadExcel
from testfile.writeExcel import WriteExcel


return_xls = ReadExcel('ReturnOrder.xlsx', 'Sheet1').read_data() # 由文件readExcel来获取用例
path=getpathinfo.get_path()
target_file=os.path.join(path,'result','excelReport','ReturnOrder.xlsx')



@ddt.ddt
class testReturnOrder(unittest.TestCase):

    def setUp(self):
        print("测试开始前准备")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    @ddt.data(*return_xls)
    def test01case(self,data):
        rowNum = int(data['id'].split("_")[-1])
        print(rowNum)
        print("******* 正在执行用例 ->{0} *********".format(data['id']))
        print("请求方式: {0}，请求URL: {1}".format(data['method'], data['url']))
        print("请求参数: {0}".format(data['params']))
        re = RunMain().run_main(data['method'], data['url'], eval(data['params']))
        result = json.loads(re)
        print("页面返回信息：%s" % re)
        if re !=None:
           WriteExcel(target_file).write_data(rowNum, re)
        readData_success=data['success']
        if readData_success==result['success']:
            OK_data="PASS"
            print("用例测试结果:  {0}---->{1}".format(data['id'], OK_data))
            WriteExcel(target_file).write_data(rowNum+1,OK_data)
        if readData_success!=result['success']:
            NOT_data = "FAIL"
            print("用例测试结果:  {0}---->{1}".format(data['id'], NOT_data))
            WriteExcel(target_file).write_data(rowNum+1,NOT_data)
        self.assertTrue(result['success'],"返回实际结果是->:%s" %result['success'] )


if __name__ == '__main__':
    unittest.main()
