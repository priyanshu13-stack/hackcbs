from django.shortcuts import render,redirect
from .forms import CreateUserForm, AuthorizationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .decorators import unauthenticated_user
from .models import authorization


# Create your views here.

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully")
            return redirect('userlogin:authorize')

    context = {
        "form" : form
    }
    return render(request, "userlogin/register.html", context)


def ulogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('app:index')
        else:
            messages.info(request, 'Username or password is incorrect!')
            return render(request, "userlogin/login.html")

    return render(request, "userlogin/login.html")


def ulogout(request):
    logout(request)
    return redirect('app:index')

def authorize(request):
    frm = AuthorizationForm()
    if request.method == "POST":
        frm = AuthorizationForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('userlogin:ulogin')
    context = {
        "frm": frm,
    }
    return render(request, "userlogin/authorize.html", context)

def connect(request):
    dic = authorization.objects.all()
    context = {
        "dic" : dic,
    }
    return render(request, 'userlogin/connect.html', context)



