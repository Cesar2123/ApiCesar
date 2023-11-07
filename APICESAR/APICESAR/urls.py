"""APICESAR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from api.views import Home
from api.views import About
from api.views import Login
from api.views import Signin
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(),name='index'),
    path('about/', About.as_view(),name='about'),
    path('login/', views.inicio_ses,name='login'),
    path('signin/', Signin.as_view(),name='signin'),
    path('form/', views.form_verificacion,name='form')
]
