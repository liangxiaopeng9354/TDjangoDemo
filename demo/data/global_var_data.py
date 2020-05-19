#coding:utf-8
class global_var:

    Id = '0'
    request_name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    #前置条件
    pre_content = '5'
    header = '6'
    #case依赖
    case_depend_7 = '7'
    #数据依赖
    data_depend_8 = '8'
    field_depend_9 = '9'
    is_pin_url = '10'
    data = '11'
    excepter = '12'
    result= '13'

    #获取id
    def get_id(self):
        return global_var.Id
    #获取接口名称
    def get_case_name(self):
        return global_var.request_name
    #h获取URL
    def get_url(self):
        return global_var.url

    def get_is_run(self):
        return global_var.run

    def get_request_way(self):
        return global_var.request_way

    def get_pre_content(self):
        return global_var.pre_content

    def get_header(self):
        return global_var.header
    def get_case_gepend_7(self):
        return global_var.case_depend_7
    def get_data_depend_8(self):
        return global_var.data_depend_8
    def get_field_depend_9(self):
        return global_var.field_depend_9

    def get_is_pin_url(self):
        return global_var.is_pin_url

    def get_data(self):
        return global_var.data
    def get_excepter(self):
        return global_var.excepter

    def get_result(self):
        return global_var.result

