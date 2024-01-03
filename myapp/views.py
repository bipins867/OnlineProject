
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import  login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserInfo
from django.db.models import Q
from django.contrib.auth.hashers import make_password,check_password
from .forms import *

def registerView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username=request.POST.get('username','')
            email=request.POST.get('email','')
            password=request.POST.get('password','')
            password=make_password(password)
            user = UserInfo.objects.filter(Q(username=username) | Q(email=email)).first()
            
            if user:
                return render(request, 'register.html',{'status':"Email Already Exists!"})
            
            try:
                userInfo=UserInfo(username=username,password=password,email=email)
                userInfo.save()
                form.save()
                return redirect('login')
            except err:
                
                return render(request, 'register.html',{'status':"Something went wrong!"})

        else:
            #print('a'+str(form)+'h')
            return render(request, 'register.html',{'status':'Username alredy exists!'})
        
        
    
    return render(request, 'register.html',{'status':''})


def loginView(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            dusername = form.cleaned_data.get('username')
            dpassword = form.cleaned_data.get('password')
            
            
            
            user = authenticate(request, username=dusername, password=dpassword)
            
            
            if user:
                
                login(request,user)
                
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'status': "Incorrect Password !"})
        else:
            
            return render(request, 'login.html', {'status': 'Incorrect Username or Password !'})
        
            
            
    
    
    return render(request, 'login.html', {'status': ''})


@login_required
def dashboardView(request):
    #print(request.user.password)
    return render(request, 'dashboard.html')

@login_required
def profileView(request):
    return render(request, 'profile.html')

@login_required
def logoutView(request):
    logout(request)
    return redirect('login')


