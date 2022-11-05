from django.shortcuts import redirect,render
from django.http import HttpResponse

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('app:index', user1=request.user.username)
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func