from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully")
            return redirect('userlogin:login')

    context = {
        "form" : form
    }
    return render(request, "userlogin/register.html", context)

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password =  request.POST.get('password')
        user = authenticate(request , username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('app:home')
        else:
            messages.info(request, 'Username or password is incorrect!')
            return render(request, "userlogin/login.html")

    return render(request, "userlogin/login.html")

