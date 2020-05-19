#coding:utf-8
'''
处理eink接口请求
1.处理token等数据依赖
2.处理依赖数据跟到URL后面

'''
import urllib

import requests
import sys
import json

sys.path.append("D:/Users/lxp/PycharmProjects/Tdjango")
from demo.util.commen_until import *
from demo.base.runmethod import RunMethod
from demo.data.get_data import GetData
from demo.data.dependent_data import DependentData
from demo.util.send_mail import *


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_until = CommenUntil()
        self.send_mail = SendEmail()
    #程序执行的主入口
    def go_on_run(self):
        pass_count = []
        fail_count = []
        no_run = []

        rows_count = self.data.get_case_lines()

        for i in range(1,rows_count):
            case_name = self.data.get_case_name(i)
            run = self.data.get_is_run(i)
            data = self.data.get_data_for_json(i)
            if run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_mothod(i)
                request_data = self.data.get_data_for_json(i)
                except_data = self.data.get_except_data(i)
                header = self.data.get_is_header(i)
                depend_case_id_7 = self.data.is_depend(i)
                is_pin_url = self.data.get_is_pin_url(i)
                #检测是否需要拼接URL
                if is_pin_url == 'yes':
                    request_data1 = urllib.parse.urlencode(request_data)
                    url1 = url + "?" + request_data1

                    if depend_case_id_7 != None:
                        self.depend_data = DependentData(depend_case_id_7)

                        #获取依赖的相应数据
                        depend_response_data = self.depend_data.get_data_for_key(i)
                        #获取依赖的key
                        depend_key = self.data.get_depend_field(i)
                        #将token

                        #request_data[depend_key] = depend_response_data
                        request_data2 = urllib.parse.urlencode(request_data)
                        url = url + depend_response_data+"?"+request_data2

                        res = self.run_method.run_main(method, url, request_data, header)
                        flag = self.com_until.is_contain(except_data, str(res))

                        if flag:
                             #self.data.write_value(i,'测试通过')
                            #print(case_name,"测试通过")
                            pass_count.append(i)

                        else:
                            #self.data.write_value(i, '测试失败')
                            #print(case_name,'测试失败!!!!!!!!!!!!!!!!!!')
                            print(res)
                            fail_count.append(i)

                    else:
                        res = self.run_method.run_main(method, url1, json.dumps(data), header)
                        flag = self.com_until.is_contain(except_data, str(res))

                        if flag:
                            #print(res)
                            # self.data.write_value(i,'测试通过')
                            #print(case_name, "测试通过")
                            pass_count.append(i)

                        else:
                            #print(res)
                            # self.data.write_value(i, '测试失败')
                            #print(case_name, '测试失败!!!!!!!!!!!!!!!!!!')
                            fail_count.append(i)
                            print(res)
                else:
                    if depend_case_id_7 != None:
                        self.depend_data = DependentData(depend_case_id_7)

                        #获取依赖的相应数据
                        depend_response_data = self.depend_data.get_data_for_key(i)
                        #获取依赖的key
                        depend_key = self.data.get_depend_field(i)
                        #将token

                        request_data[depend_key] = depend_response_data
                        #url = url+'?'+ depend_response_data


                        res = self.run_method.run_main(method, url, request_data, header)
                        flag = self.com_until.is_contain(except_data, str(res))

                        if flag:
                             #self.data.write_value(i,'测试通过')
                            #print(case_name,"测试通过")

                            print(res)
                        else:
                            #self.data.write_value(i, '测试失败')
                            #print(case_name,'测试失败!!!!!!!!!!!!!!!!!!')
                            fail_count.append(i)
                            print(res)

                    else:
                        res = self.run_method.run_main(method, url, json.dumps(data), header)
                        flag = self.com_until.is_contain(except_data, str(res))

                        if flag:
                            #print(res)
                            # self.data.write_value(i,'测试通过')
                            #print(case_name, "测试通过")
                            pass_count.append(i)

                        else:
                            #print(res)
                            # self.data.write_value(i, '测试失败')
                            #print(case_name, '测试失败!!!!!!!!!!!!!!!!!!')
                            fail_count.append(i)
                            print(res)

            else:
                #print(case_name,'----这个方法不被执行')
                no_run.append(i)



        self.send_mail.send_main(pass_count,fail_count,no_run)
        print('成功的条数：',len(pass_count))
        print('失败的条数：',len(fail_count))
        print('没有运行的用例条数：',len(no_run))


if __name__ == '__main__':
    run_test = RunTest()
    run_test.go_on_run()
