from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name = "index"),
    path('course', views.course_data, name = "course"),

]