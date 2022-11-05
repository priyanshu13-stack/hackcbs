from django.urls import path
from .import views

urlpatterns = [
    path('ulogin', views.ulogin, name ='ulogin'),
    path('ulogout', views.ulogout, name ='ulogout'),
    path('register/', views.register, name ='register'),
]