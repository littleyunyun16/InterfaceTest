'''读取excel文件并把其'''


import os
import getpathinfo
import xlrd

path=getpathinfo.get_path()

class ReadExcel():
    """读取excel文件数据"""
    def __init__(self, xls_name, sheet_name):
        self.xls_path=os.path.join(path,'case',xls_name)
        self.sheet_name=sheet_name
        self.data = xlrd.open_workbook(self.xls_path)
        self.table = self.data.sheet_by_name(sheet_name)
        self.nrows = self.table.nrows
        self.ncols = self.table.ncols

    def read_data(self):
        if self.nrows > 1:
            # 获取第一行的内容，列表格式
            keys = self.table.row_values(0)
            listApiData = []
            # 获取每一行的内容，列表格式
            for col in range(1, self.nrows):
                values = self.table.row_values(col)
                # keys，values组合转换为字典
                api_dict = dict(zip(keys, values))
                listApiData.append(api_dict)
            return listApiData
        else:
            print("表格是空数据!")
            return None

if __name__ == '__main__':
    print(ReadExcel('trade_order.xlsx', 'Sheet1').read_data())

