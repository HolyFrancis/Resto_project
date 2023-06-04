from django.urls import path
from app.views import home, account

urlpatterns = [
    path('',home.index,name='home'),
    path('register',account.registerPage,name='register'),
    path('login',account.loginUser,name='login'),
]
