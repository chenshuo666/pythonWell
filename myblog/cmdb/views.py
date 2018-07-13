from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from cmdb import models


def getLogin(request):
    # 包含用户提交的所有信息
    # 获取用户提交方法
    # print(request.method)
    error_msg = ""
    if request.method == "POST":
        # 获取用户通过POST提交过来的数据
        user = request.POST.get('form-username',None)
        pwd = request.POST.get('form-password',None)
        for q,w in request.environ.items():

            print(q,w)

        result = models.UsernameInfo.objects.filter(username=user,pwd=pwd)
        if result:
            # 去跳转到
            res=redirect('/index/home')
            res.set_cookie("user_xianshi",user)
            #res.set_signed_cookie("user_xianshi",user,salt="chenshuo")#用户数据加密
            return res
        else:
            error_msg="Username or Password Wrong!"
            return render(request,'login_blog.html',{'error_msg':error_msg})
    else:
        return render(request, 'login_blog.html', {'error_msg': error_msg})


def getHome(request):
    s=request.COOKIES.get("user_xianshi")
    if not s:
        return redirect("index/login_blog")
    return render(request,'home.html',{"current_user":s})

def getAbout(request):
    s=request.COOKIES.get("user_xianshi")
    if not s:
        return redirect("index/login_blog")
    return render(request,'about.html',{"current_user":s})

def getBlog(request):

    s=request.COOKIES.get("user_xianshi")
    if not s:
        return redirect("index/login_blog")
    return render(request,'blog.html',{"current_user":s})

def getContact(request):
    s=request.COOKIES.get("user_xianshi")
    if not s:
        return redirect("index/login_blog")
    return render(request,'contact.html',{"current_user":s})

def getPortfolio(request):
    s=request.COOKIES.get("user_xianshi")
    if not s:
        return redirect("index/login_blog")
    return render(request,'portfolio.html',{"current_user":s})

def getLogin_blog(request):
    s=request.COOKIES.get("user_xianshi")
    if not s:
        return redirect("index/login_blog")
    return render(request,'login_blog.html',{"current_user":s})

def getRegister(request):
    error_msg = ""
    if request.method == "POST":
        # 获取用户通过POST提交过来的数据
        user_input = request.POST.get('form-username', None)
        pwd_input = request.POST.get('form-password', None)
        pwd_again_input = request.POST.get('form-password-again',None)
        email_input = request.POST.get('form-email',None)
        gender_input = request.POST.get('form-gender',None)
        phone_input = request.POST.get('form-phone',None)

        if (pwd_input == pwd_again_input)&(pwd_input!=None):
            error_msg="注册成功"
            models.UsernameInfo.objects.create(username=user_input,
                                                       pwd=pwd_input,
                                                       email=email_input,
                                                       gender=gender_input,
                                                       phone=phone_input)
            return render(request, 'register.html', {'error_msg': error_msg})
        else:
            error_msg = "密码不一致"
            return render(request, 'register.html', {'error_msg': error_msg})
    else:
        return render(request, 'register.html', {'error_msg': error_msg})


