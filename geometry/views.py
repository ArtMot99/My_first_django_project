from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render


def get_rectangle_area(request, width: int, height: int):
    result = width * height
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {result}')


def redirect_get_rectangle_area(request, width: int, height: int):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')


def get_square_area(request, width: int):
    result = width * width
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {result}')


def redirect_get_square_area(request, width: int):
    return HttpResponseRedirect(f'/calculate_geometry/square/{width}')


def get_circle_area(request, radius: int):
    result = 3.14 * (radius**2)
    return HttpResponse(f'Площадь круга радиуса {radius} равна {result}')


def redirect_get_circle_area(request, radius: int):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')