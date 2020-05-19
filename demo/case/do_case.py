#coding:utf-8
from demo.data.get_data import GetData


class DoCase:
    def __init__(self):
        self.data = GetData()

    def is_run(self,col):
        case_name = self.data.get_case_name(col)
        url = self.data.get_request_url(col)
        method = self.data.get_request_mothod(col)
        request_data = self.data.get_data_for_json(col)
        except_data = self.data.get_except_data(col)
        header = self.data.get_is_header(col)
        depend_case_id_7 = self.data.is_depend(col)
        is_pin_url = self.data.get_is_pin_url(col)




