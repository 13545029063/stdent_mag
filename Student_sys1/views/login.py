from django.shortcuts import render,HttpResponse,redirect
from Student_sys1.models import *
def login(request):
    return render(request,'login.html')
def logger(request):
    userName=request.POST.get("userName")
    Psw = request.POST.get("psw")
    if userName=='gyc' and Psw=='123':
        return redirect('/index')
    else:
        return HttpResponse('账户密码错误！请注册.请先登录')
def login_db(request):
    return render(request,'register_return.html')
def register(request):
    return render(request,'register.html')
def index_log(request):

    return render(request,'index.html')