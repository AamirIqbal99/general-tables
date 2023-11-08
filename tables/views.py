from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username'] # <--- because we have given name username in input methon of our home.html file
        password = request.POST['password'] # <--- because we have given password password in input methon of our home.html file

        # Now afte this we want to authenticate the above
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("I am Loggen In successfully!")
            messages.success(request, "You have Logged In Successfully!")
            return redirect('home')
        else:
            print("There was an Error while Logging In!")
            messages.success(request, "There was an error while Logging In. Please check your User Name and Password!")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def login_user(request): # <--- use this method if you are creating seperate page for logging in, also see urls.py file
    pass

def logout_user(request):
    print("I am Logged Out successfully!")
    logout(request)
    messages.success(request, "You have Logged Out Successfully!")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})