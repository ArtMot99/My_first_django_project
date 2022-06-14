from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def get_rectangle_area(request, width: int, height: int):
    result = width * height
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {result}')


def redirect_get_rectangle_area(request, width: int, height: int):
    get_url = reverse('rectangle', args=(width, height))
    return HttpResponseRedirect(get_url)


def get_square_area(request, width: int):
    result = width * width
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {result}')


def redirect_get_square_area(request, width: int):
    get_url = reverse('square', args=(width, ))
    return HttpResponseRedirect(get_url)


def get_circle_area(request, radius: int):
    result = 3.14 * (radius**2)
    return HttpResponse(f'Площадь круга радиуса {radius} равна {result}')


def redirect_get_circle_area(request, radius: int):
    get_url = reverse('circle', args=(radius, ))
    return HttpResponseRedirect(get_url)
