#coding:utf-8

import xlrd
from xlutils import copy

class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id

        else:
            self.file_name = '../dataconfig/data.xls'
            self.sheet_id = 1

        self.data = self.get_data()
    #获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]

        return tables
    #获取单元格的行数

    def get_lines(self):

        tables = self.data
        return tables.nrows

    #获取某个单元格的内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)


    #将结果写入Excel文档中
    '''
    需要传 row col value
    '''
    def write_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy.copy(read_data)

        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    #将某一列的内容获取到1
    def get_cols_data(self,col_id):
        if col_id != None:
            cols = self.data.col_values(col_id)

        else:
            cols = self.data.col_values(0)
        return cols

    #根据对应的caseid找到对应的行号2
    def get_row_num(self,case_id):
        num = 0
        clols_data = self.get_cols_data(num)

        for clo_data in clols_data:
            if case_id in clo_data:
                return num
            num = num + 1


    # 根据行号，找到改行的内容3
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

     #根据对应的caseid找对应的内容（总的执行）
    def get_rows_data(self,case_id):
        #获取行号
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data


if __name__ == '__main__':
    opers = OperationExcel()
    opers.get_data()
    print(opers.get_cell_value(1,6))




