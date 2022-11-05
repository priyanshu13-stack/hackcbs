from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='userlogin/ulogin')
def index(request):
    return render(request, "home.html")
