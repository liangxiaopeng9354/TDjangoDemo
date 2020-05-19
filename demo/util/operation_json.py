#coding:utf-8
import json

from demo.data.get_data import *



class Operation_json():

    def __init__(self):
        self.data = self.read_data()


    def read_data(self):
        with open('../dataconfig/login.json') as fp:
            data = json.load(fp)
            return data
        '''
        fp = open(self.file_name)
        data = json.load(fp)[self.fangfa_name]
        return data
        '''

    def get_data(self,request_data):

        if request_data == None:
            return request_data
        else:
            return self.data[request_data]

if __name__ == '__main__':
    getData = GetData()
    #f_name='dataconfig/data.json'
    #ff_name = 'login'
    opera = Operation_json()
    res = getData.get_request_data(1)
    print(res)
    print(opera.get_data('login'))





