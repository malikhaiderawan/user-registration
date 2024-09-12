from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')
def admin_user(request):
    return render(request,'admin.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        #user authentication
        if User.objects.filter(username=username).exists():
            messages.error(request,'Yours Username alreasy exists please Choose another username.Thank YOU!')
            return render(request, 'register.html')
        #error handling
        if pass1!=pass2:
            messages.error(request,'Both password are not same!Please Enter the Both same Passwords.')
            return redirect('register')

        #create new user
        foz=User.objects.create_user(username,email,pass1)
        foz.first_name=fname
        foz.last_name=lname

        foz.save()
        messages.success(request,'You are successfully registered! Now Please Login!')
        return redirect('login')

    return render(request,'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Perhaps Username or Password incorrect. Or U r not registered! IF uh R not Registered please click on Register button for Registration!')
            return render(request, 'login.html')

        elif user.is_superuser:
            login(request, user)
            messages.success(request, 'YOU are logged in to Admin-Page')
            return redirect('login/admin')

        else:
            login(request, user)
            messages.success(request, 'You are successfully logged in!')
            return redirect('home')

    return render(request, 'login.html')


def Logout(request):
    logout(request)
    messages.success(request,'You have been Successfully Logged Out!')
    return redirect('home')
