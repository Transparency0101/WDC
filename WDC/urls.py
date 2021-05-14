"""WDC URL Configuration

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
# Импорт функция представлений
from app1 import views

urlpatterns = [
    # Путь к регистрации
    path("form", views.form, name="form"),
    # Путь к странице о нас
    path("about", views.about, name="about"),
    # Путь к представлению к основной странице
    path("home", views.home, name="home"),
    # Путь к представлению календарь
    path("calendar", views.calendar, name="calendar"),
    # Путь к представлению привествия
    path("", views.welcome, name="welcome"),
    # Админка
    path('admin/', admin.site.urls),
]
