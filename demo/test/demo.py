
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
import urllib

class RunMain():

    def __init__(self,url,method,data=None,headers=None):
        self.res=self.run_main(url,method,data,headers)


    def send_post(self,url,data,header=None):
            res=requests.post(url,data=data,headers=headers)
            print(res.url)
            res2=res.json()
            return json.dumps(res2,indent=2,sort_keys=True)


    def send_get(self,url,data,header=None):
            '''
            res=requests.get(url).json()
            return json.dumps(res,indent=2,sort_keys=True)

            :param url:
            :return:
            '''
            res=requests.get(url,data,headers=headers)

            return res
    def run_main(self,url,method,data=None,headers=None):
        res=None
        if method=='GET':
            res= self.send_get(url,data,headers)

        else:
            res= self.send_post(url,data,headers)
        return res
if __name__ == '__main__':

    url = 'http://192.168.10.166:9001/rest/sxreaderapp/login'
    url2 = 'http://192.168.10.166:9006/rest/sxreader/getAllTeacherTaskInfos?activity=0&condition=&indexPage=1&pageSize=12&status=unfinished&userId=60da42581d4b11eaa0046c92bf28f871'
    data = {
              "password": "232323",
              "username": "232323"
            }

    url3='http://192.168.10.166:9001/rest/sxreaderapp/company/stu/getCompanyPushHistorys'
    pingjie= '12313132121'

    data2 = {

        "indexPage":"1",
        "pageSize":"10"

    }


    headers = {
                  "content-type": "application/json;charset=UTF-8",
                "Authorization" :"bd86f93bd0164c179ff38a3568fbcc33_3ecb9201973a40eeb80fdd9ad1ac0634",
        "apt-version":"3.4"
            }


    res_data = dict(
        userid=111,
        extno=""
    )

    #run2 = RunMain(url,'POST',json.dumps(data),headers)
    run3 = RunMain(url3,'GET',headers)
    #print(run3.res,'-----')
    #print(run3.run_main(url3,'GET',headers),'-----')
    query_string = urllib.parse.urlencode(data2)
    print(query_string)
    url = url3+'?'+pingjie+query_string
    res=requests.get(url,data=data2,headers=headers)
    print(res.url)
    print(res.json())

    #print(run.run_main(url2,'GET',res_data))
    #print(run.run_main(url,'POST',data))