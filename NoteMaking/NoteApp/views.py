from django.shortcuts import render , redirect
from django.contrib.auth.models import auth , User
from django.contrib import messages
from .models import *

# Create your views here.

# creating view for SignUp Page 

def signupPage(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']

        if password == c_password:
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username has been already taken")
                return redirect('signuppage')

            elif User.objects.filter(email = email).exists():
                messages.info(request,"This email is already registered with us ")
                return redirect('signuppage')
            
            else:
                newUser = User.objects.create(username = username , email = email , password = password)
                newUser.save()
                messages.info(request," Registered Successfully.....")
                return redirect('signuppage')
        else:
            messages.info(request , "Both passwords are not matching...")
            return redirect('signuppage')

    return render(request , 'signup.html')
