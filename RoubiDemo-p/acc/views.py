from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from acc.models import UserMoshtari
from django.contrib.auth import authenticate,login,logout


def usersignup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user= User.objects.get(username=request.POST['username'])
                return render(request,'acc/register.html',{'error':'این نام کاربری قبلا در سیستم ثبت شده است'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'],email=request.POST['email'],)
                ###UserMoshtari.phone_number=request.POST['phonenumber']
                auth.login(request,user)
                return render(request,'acc/register.html',{'error':'تبت نام با موفقیت انجام شد'})


        else:
            return render(request, 'acc/register.html', {'error': 'لطفا پسور شبیه به هم وارد کنید'})
    else:
        return render(request, 'acc/register.html')

# def usert(request):
#     if request.method == 'POST1':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password,)
#         if user is not None:
#             try:
#                 userss = UserMoshtari.objects.create_user(user=User.username, phone_number=request.POST['phonenumber'])
#                 auth.login(request, userss)
#                 return redirect('usert')
#             except User.DoesNotExist:
#                 return render(request, 'acc/register.html', {'error': 'این نام کاربری وجود ندارد'})


