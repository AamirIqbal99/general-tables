from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import SignUpForm, AddRecordForm
from . models import Record

def home(request):
    records = Record.objects.all()
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
        return render(request, 'home.html', {'records': records})

def login_user(request): # <--- use this method if you are creating seperate page for logging in, also see urls.py file
    pass

def logout_user(request):
    print("I am Logged Out successfully!")
    logout(request)
    messages.success(request, "You have Logged Out Successfully!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate user and user login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have registered Successfully, Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # lookup the records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You have to Login to view that Record!")
        return render('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated: # <--- if user is authenticated then he must allow to delete the data
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record has been Deleted Successfully!")
        return redirect('home')
    else:
        messages.success(request, "You must be Logged In to delete that Record!")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added Successfully!")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been Updated Successfully!")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})