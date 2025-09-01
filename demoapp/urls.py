from django.urls import path
from demoproject.views import *
urlpatterns = [
    path('signup',signuppage,name='signup'),
    path('login',loginpage,name='login'),
    path('signup_function',signup_function,name='signupfunction'),
    path('login_function',login_function,name='loginfunction'),
    path('',homepage,name='home'),
]