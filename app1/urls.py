from django.urls import re_path
from . import views

urlpatterns = [
    # Путь к регистрации
    re_path(r"^form", views.form, name="form"),
    # Путь к странице о нас
    re_path(r"^about", views.about, name="about"),
    # Путь к представлению к основной странице
    re_path(r"^home", views.home, name="home"),
    # Путь к представлению календарь
    re_path(r"^calendar", views.calendar, name="calendar"),
    # Путь к представлению привествия
    re_path(r"^", views.welcome, name="welcome"),
]
