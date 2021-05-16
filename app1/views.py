# Ипорт шаблонов
from django.shortcuts import render
# Импорт http надписей
from django.http import HttpResponse
# Http ошибки
from django.http import *
# Формы импорты
from .form import UserForm
# Переадресация
from django.http import HttpResponseRedirect


def welcome(request):
    # Представление на встречю
    return render(request, "app1/welcome.html")


def home(request):

    # Ипорт модулей
    from pyowm import OWM
    import datetime
    # Мой ключь
    owm = OWM('e492ec8cc006356f2d843bb65e42f709')
    # Управление погодой
    mgr = owm.weather_manager()
    # Погода в Украине
    place_weather = mgr.weather_at_place('Украина')
    w = place_weather.weather
    # Температура в цельсиях
    t = w.temperature("celsius")
    t1 = t['temp']
    t2 = t['feels_like']
    t3 = t['temp_max']
    t4 = t['temp_min']
    # Дата и время
    time = datetime.datetime.today()
    # Передача в шаблон home
    data = {'t1': t1, 't2': t2, 't3': t3, 't4': t4, "time": time}
    # Представление на главную
    return render(request, "app1/home.html", context=data)


def calendar(request):
    # Представление на календарь
    return render(request, "app1/calendar.html")


def about(request):
    # Путь на страницу about
    return render(request, "app1/about.html")


def form(request):
    # Путь на страницу регистрации
    userform = UserForm()
    # Валидация
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            surname = userform.cleaned_data["surname"]
            age = userform.cleaned_data["age"]
            born = userform.cleaned_data["born"]
            data_forms = {
                "name": name, "surname": surname, "age": age, "born": born,
            }
            # Шаблон с результатами
            return render(request, "app1/result.html", context=data_forms)
        else:
            return HttpResponse("Invalid data")
    else:

        userform = UserForm()
        return render(request, "app1/form.html", {"form": userform})
