#coding:utf-8

import xlrd


class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id

        else:
            # app接口xlsx
            self.file_name = '../dataconfig/data.xls'

            # APP的sheet_id
            #self.sheet_id = 0
            #eink的sheet_id
            self.sheet_id = 1

        self.data = self.get_data()
    #获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        print("self.sheet_id:",self.sheet_id)
        tables = data.sheets()[self.sheet_id]

        return tables
    #获取单元格的行数

    def get_lines(self):
        if __name__ == '__main__':
            tables = self.data
            return tables.nrows

    #获取某个单元格的内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

if __name__ == '__main__':
    opers = OperationExcel()
    opers.get_data()
    print(opers.get_cell_value(1,6))




