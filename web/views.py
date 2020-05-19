from django.shortcuts import render


# Create your views here.


from django.http.response import HttpResponse
from django.shortcuts import render
import json
def Login(request):
    #return HttpResponse('test is first test')
    if request.method == 'POST':
        result={}

        username= request.POST.get('username')
        password= request.POST.get('password')
        result['username']=username
        result['password']=password

        result=json.dumps(result)
        return  HttpResponse(result,content_type='application/json;charset=utf-8')

    else:
        return render(request,'login.html')
