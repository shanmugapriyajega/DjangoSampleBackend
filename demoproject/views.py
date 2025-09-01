from django.shortcuts import render,redirect
from demoapp.models import *
# from demoproject.views import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from demoapp.serializer import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
User=get_user_model()

def homepage(request):
    return render(request,'index.html')
def shoppage(request):
    return render(request,'shop.html')
# def get_products(request):
#     products=dresstable.objects.all()
#     return render(request,'shop.html',{'products':products})
def signuppage(request):
    return render(request,"signup.html")
def loginpage(request):
    return render(request,"login.html")
def signup_function(request):
    if request.method=="POST":
        firstname=request.POST.get("first_name")
        lastname=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        address=request.POST.get("address")
        phonenum=request.POST.get("phonenum")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirm_password")
        data = {
    "first_name": firstname,
    "last_name": lastname,
    "username": username,
    "email": email,
    "address": address,
    "phonenum": phonenum,
    "password": password
}

        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                return redirect('signup')
            serializer=otherdetailsserializer(data=data)
            if serializer.is_valid():
                user=serializer.save()
                refresh_token=RefreshToken.for_user(user)
                access_token=refresh_token.access_token
                refresh=str(refresh_token)
                access=str(access_token)
                print(f"refresh : {refresh},access : {access}")
                return redirect('login')
            else:
                print(serializer.errors)
                return redirect('signup')
        else:
            # user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
            # user.save()
            return redirect('signup')
        
def login_function(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)   
            return redirect('home')  
        else:
            return redirect('login')  
    return redirect('login')
