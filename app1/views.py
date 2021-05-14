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


class HttpErrors_class:
    # Класс http ошибок
    @classmethod
    def m304(self, request):
        return HttpResponseNotModified()

    @classmethod
    def m400(self, request):
        return HttpResponseBadRequest("<h2>Bad Request</h2>")

    @classmethod
    def m403(self, request):
        return HttpResponseForbidden("<h2>Forbidden</h2>")

    @classmethod
    def m404(request, self):
        return HttpResponseNotFound("<h2>Not Found</h2>")

    @classmethod
    def m405(self, request):
        return HttpResponseNotAllowed("<h2>Method is not allowed</h2>")

    @classmethod
    def m410(self, request):
        return HttpResponseGone("<h2>Content is no longer here</h2>")

    @classmethod
    def m500(self, request):
        return HttpResponseServerError("<h2>Something is wrong</h2>")


def welcome(request):
    # Представление на встречю
    return render(request, "app1/welcome.html")


def home(request):
    # Ипорт модуля
    from pyowm import OWM
    # Мой ключь
    owm = OWM('e492ec8cc006356f2d843bb65e42f709')
    # Управление погодой
    mgr = owm.weather_manager()
    # Погода в Украине
    place_weather = mgr.weather_at_place('Украина')
    w = place_weather.weather
    # Температура в цельсиях
    t = w.temperature("celsius")
    # Температура
    t1 = t['temp']
    # Ощущается
    t2 = t['feels_like']
    # Максимальная
    t3 = t['temp_max']
    # Минимальная
    t4 = t['temp_min']
    # Передача в шаблон home
    data = {'t1': t1, 't2': t2, 't3': t3, 't4': t4, }
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
