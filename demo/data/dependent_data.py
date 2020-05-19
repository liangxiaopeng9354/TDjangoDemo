#解决所有数据依赖的一个类

#coding:utf-8
from demo.util.operation_excel import OperationExcel
from demo.base.runmethod import RunMethod
from demo.data.get_data import GetData
from jsonpath_rw import jsonpath,parse
import json

class DependentData:
    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.run_method = RunMethod()
        self.data = GetData()

    #根据case_id获取case_id的整行数据
    def get_case_line_data(self,case_id):
        rows_data = self.opera_excel.get_rows_data(case_id)
        return rows_data

    #执行依赖测试，获取结果
    def run_dependent(self):
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        case_name = self.data.get_case_name(row_num)
        url = self.data.get_request_url(row_num)
        method = self.data.get_request_mothod(row_num)
        header = self.data.get_is_header(row_num)
        res = self.run_method.run_main(method,url,json.dumps(request_data),header)
        return res

    #根据依赖的key去获取执行测试的case的相应
    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        json_exe = parse(depend_data)
        globals = {
            'false': 0,
            'true':0
        }
        data = eval(response_data,globals)
        madle = json_exe.find(data)
        return [math.value for math in madle][0]
        #
        # globals = {
        #     'false': 0
        # }
        #
        # # -----------
        # data = eval(response_data, globals)
        #
        # print(type(data))
        # qqq = json.dumps(data)
        # print(qqq)
        # print(type(qqq))
        # print(data["data"]["token"])

if __name__ == '__main__':
    data = {
    "code":200,
    "data":{
        "event":{
            "avatarBoxUrl":"",
            "avatarUrl":"http://edu.bjzjmy.com:9134/rest/upload/onlineshow/20180903/99770bb1a5b244df8f253ae7c4e4e0a5/99770bb1a5b244df8f253ae7c4e4e0a5_base64Name.jpg",
            "currentDate":1589464712553,
            "enterTime":"",
            "firstLanding":False,
            "fullname":"232323",
            "gender":1,
            "groupId":"39c5155c0a7a11e89292fa163e29292b",
            "groups":[
                {
                    "groupName":"七年级一班",
                    "id":"39c5155c0a7a11e89292fa163e29292b",
                    "url":"683ce4fcd73c4cff904769aa362450ed"
                }
            ],
            "isValid":0,
            "schoolId":"1086985",
            "schoolLogoUrl":"",
            "schoolName":"美育中学",
            "subject":"",
            "token":"60da42581d4b11eaa0046c92bf28f871_b64b1416d215432dbd2aeb89e8f6a61e",
            "userId":"60da42581d4b11eaa0046c92bf28f871",
            "userManagement":1,
            "username":"232323",
            "webAuthorities":[
                "ROLE_Student"
            ],
            "xd":0
        },
        "isLogin":1
    },
    "message":"SUCCESS"
}
    res = "data.event.token"
    json_exe = parse(res)
    madle = json_exe.find(data)
    print(type(data))
    print ([math.value for math in madle][0])




