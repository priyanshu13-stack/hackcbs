from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .decorators import unauthenticated_user


# Create your views here.
@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully")
            return redirect('userlogin:ulogin')

    context = {
        "form" : form
    }
    return render(request, "userlogin/register.html", context)

@unauthenticated_user
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
    return redirect('userlogin:ulogin')


