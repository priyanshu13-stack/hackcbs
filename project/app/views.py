from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import course
from .decorators import unauthenticated_user
# Create your views here.

# @login_required(login_url='userlogin/ulogin')
def index(request):
    return render(request, "index.html")

def course_data(request):
    data = course.objects.all()
    context ={
        "data" : data,
    }
    return render(request, "index.html", context)

