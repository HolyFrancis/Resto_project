from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from app.forms import UserRegisterForm


def registerPage(request):
    form= UserRegisterForm()
    
    if request.method=='POST':
       form= UserRegisterForm(request.POST)
       if form.is_valid():
           form.save() 
    context={'form':form}
    return render(request, 'app/accounts/register.html',context)
    