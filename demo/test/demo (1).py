
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

def send_post(url,data):
        res=requests.post(url,data=data).json()

        return json.dumps(res,indent=2,sort_keys=True)


def send_get(url,data):
        '''
        res=requests.get(url).json()
        return json.dumps(res,indent=2,sort_keys=True)

        :param url:
        :return:
        '''
        res=requests.get(url,data)
        print(res.text)
        return res.text

def run_main(url,method,data):
    res=None
    if method=='GET':
        res= send_get(url,data)

    else:
        print(1111111111)


    return res

#url='https://sxreader.com:9006/login'
url2='https://sxreader.com:9006/rest/sxreader/getAllTeacherTaskInfos'
data={'username':'232323','password':'232323'}
dat2={'username':'232323','password':'232323'}


print(run_main(url2,'GET',dat2))
