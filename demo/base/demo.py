
'''
import requests


data={
    'username':'232323',
    'password':'232323'
}


res = requests.post(url='http://edu.bjzjmy.com:9136/rest/sxreaderapp/login',data=data)
print(res.text)

'''


import requests
import json
class RunMain():

#    def __init__(self,url,method,data=None):
#        self.res=self.run_main(url,method,data)



    def send_post(self,url,data):
            res=requests.post(url,data=data)
            '''
            print(111111111111111111111)
            print(res.headers)
            print(res.url)
            
            res2=res.json()
            return json.dumps(res2,indent=2,sort_keys=True)
            '''
            res2 = res.json()
            return  res2

    def send_get(self,url,data):
            '''
            res=requests.get(url).json()
            return json.dumps(res,indent=2,sort_keys=True)

            :param url:
            :return:
            '''
            res=requests.get(url,data)
            print(res.url)
            return res.text

    def run_main(self,url,method,data=None):
        res=None
        if method=='GET':
            res= self.send_get(url,data)

        else:
            res= self.send_post(url,data)
        return res
if __name__ == '__main__':

    url='https://sxreader.com:9006/login'
    url2='https://sxreader.com:9006/rest/sxreader/getAllTeacherTaskInfos?activity=0&condition=&indexPage=1&pageSize=12&status=unfinished&userId=60da42581d4b11eaa0046c92bf28f871'
    data={'username':'232323','password':'232323'}

    res_data = dict(
        userid=111,
        extno=""
    )

    run = RunMain(url2,'GET',res_data)
    run2 = RunMain(url, 'POST', data)
    print(run.res)
    #print(run.run_main(url2,'GET',res_data))
    #print(run.run_main(url,'POST',data))