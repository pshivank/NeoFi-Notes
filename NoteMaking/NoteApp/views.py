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
                newUser = User.objects.create_user(username = username , email = email , password = password)
                newUser.save()
                messages.info(request," Registered Successfully.....")
                return redirect('signuppage')
        else:
            messages.info(request , "Both passwords are not matching...")
            return redirect('signuppage')

    return render(request , 'signup.html')


# creating loginpage view 

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('notes')
        else:
            messages.info(request ,"Invalid Credentials ....")
            return redirect('loginpage')
        
    return render(request , 'login.html')

# logout view

def Logout(request):
    auth.logout(request)
    return redirect('loginpage')


# note page view where user can get after login 
    
def notePage(request):
    return render(request , 'note.html')


# creation of notes
def noteCreationPage(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST['title']
        content = request.POST['content']

        note = Note.objects.create( title = title , content = content , owner = user)
        note.save()
        messages.info(request,"Note created successfully...")
        return redirect('create')
    
    return render(request,'notecreation.html')



