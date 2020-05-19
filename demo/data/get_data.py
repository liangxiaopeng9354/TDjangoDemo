#coding:utf-8

from demo.util.operation_json import *
from demo.util.operation_excel import *
from demo.data.global_var_data import *


class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()
        self.opera_excel.get_data()



    #获取行数，这个就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()
    def get_case_name(self,row):
        col = int(global_var().get_case_name())
        case_name = self.opera_excel.get_cell_value(row,col)
        return case_name


    def get_is_run(self,row):
        col = int(global_var().get_is_run())
        run_mode = self.opera_excel.get_cell_value(row,col)
        if run_mode == 'yes':
            return True
        else:
            return False
    #获取请求方式
    def get_request_mothod(self,row):
        col = int(global_var().get_request_way())
        request_mothod = self.opera_excel.get_cell_value(row,col)
        return request_mothod
    #获取URL
    def get_request_url(self,row):
        col = int(global_var().get_url())
        url = self.opera_excel.get_cell_value(row,col)
        return url
    #获取header
    def get_is_header(self,row):
        col = int(global_var().get_header())
        header = self.opera_excel.get_cell_value(row,col)
        if header == 'yes':
            header = {
                "content-type" : "application/json;charset=UTF-8",
                "Authorization" : "37a4fd6a1a3146009c8559bef52dabdd_35c980cb2c764ded84f497de2bd73d54",
                "apt-version":"3.4"
            }
            return header
        else:
            return None

    #获取Excel中的请求数据（关键字）
    def get_request_data(self,row):
        col = int(global_var().get_data())
        data = self.opera_excel.get_cell_value(row,col)
        if data == '':
            return None
        return data

    #通过关键字拿到data的json数据
    def get_data_for_json(self,row):
        opera_json = Operation_json()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    #获取预期结果
    def get_except_data(self,row):
        col =int(global_var().get_excepter())
        except_data = self.opera_excel.get_cell_value(row,col)
        if except_data == '':
            return None
        return except_data

    #写入value
    def write_value(self,row,value):
        col = int(global_var().get_result())
        self.opera_excel.write_value(row,col,value)
    #获取依赖数据的key
    def get_depend_key(self,row):
        col = int(global_var().get_data_depend_8())
        depend_key_8 = self.opera_excel.get_cell_value(row,col)

        if depend_key_8 =='':
            return None
        else:
            return depend_key_8

    #判断是否有case依赖
    def is_depend(self,row):
        col = int(global_var().get_case_gepend_7())
        depend_case_id_7 = self.opera_excel.get_cell_value(row,col)
        if depend_case_id_7 !='':
            return depend_case_id_7
        else:
            return None

    #获取数据依赖字段
    def get_depend_field(self,row):
        col = int(global_var().get_field_depend_9())
        field_depend_9 = self.opera_excel.get_cell_value(row,col)
        if field_depend_9 !='':
            return field_depend_9
        else:
            return None
    #获取是否拼接URL
    def get_is_pin_url(self,row):
        col = int(global_var().get_is_pin_url())
        is_pin_url = self.opera_excel.get_cell_value(row,col)
        return is_pin_url





