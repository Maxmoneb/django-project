from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def welcome(request):
    return render(request, 'welcome.html')

def login(request):
     if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if User is not None:
            auth_login(request,user)
            return redirect('welcomepage')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
     return render(request, 'login.html')

def signup(request):
    if request == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


