"""Django_dome1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Student_sys1.views import student,login
import re
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',login.login),
    path('logger',login.logger),
    path('index',login.index_log),
    path('login_db',login.login_db),
    path('register',login.register),
    path('student',student.students_Html),
    path('select',student.select_stu),
    path('addStudent',student.addStudent),
    path('writ_content',student.writ_content),
    path('delete_allline',student.delete_allline),
    path('manypage',student.manypage),


]
