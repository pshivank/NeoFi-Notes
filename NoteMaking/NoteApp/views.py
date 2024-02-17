from django.shortcuts import render , redirect , get_object_or_404
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


# get note view 

def getnotePage(request):
    obj = None
    error_message = None

    if request.method == 'POST':
        try:
            id_to_fetch = request.POST.get('id_to_fetch')
            obj = get_object_or_404(Note, id=id_to_fetch)

        except Note.DoesNotExist:
            error_message = f"Object with ID {id_to_fetch} does not exist."
        
    return render(request,'getnote.html' , {'obj':obj , 'error_message':error_message})





