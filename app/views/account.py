from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from app.forms import UserRegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



def registerPage(request):
    form= UserRegisterForm()
    
    if request.method=='POST':
       form= UserRegisterForm(request.POST)
       if form.is_valid():
           form.save()
    context={'form':form}
    return render(request, 'app/account/register.html',context)

def loginUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password is incorrect')
    context={}
    return render(request, 'app/account/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')
