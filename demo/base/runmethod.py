#coding:utf-8
import requests
import json
from demo.util.operation_excel import *

class RunMethod:
    def __init__(self):
        self.get_data =OperationExcel()

    def post_main(self,url,data,header=None):
        res=None

        if header != '':

            res = requests.post(url=url,data=data,headers=header)
            #print(res.url)
            res = res.json()
            #print(json.dumps(res, ensure_ascii=False))

        else:
            res = requests.post(url=url, data=data)
            #print(res.url)
            res = res.json()
            #print(json.dumps(res, ensure_ascii=False))
            #print(res.code,'0000000000000000000')
        return res

    def get_main(self,url,data=None,header=None):

        res=None
        if header != '':
            res = requests.get(url=url,data=data,headers=header)
            #print(res.url)
            res = res.json()
            #print(json.dumps(res,ensure_ascii=False))
        else:
            res = requests.get(url=url,data=data)
            #print(res.url)
            res = res.json()
            #print(json.dumps(res, ensure_ascii=False))

        return res

    def run_main(self,method,url,data,header=None):
        res = None
        if method == 'POST':
            res = self.post_main(url,data,header)

        else:

            res = self.get_main(url,data,header)
        return json.dumps(res,ensure_ascii=False)
        #return json.dumps(res,indent=2,sort_keys=True)






