from django.http import HttpResponse
from django.shortcuts import render


def get_rectangle_area(request, width: int, height: int):
    result = width * height
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {result}')


def get_square_area(request, width: int):
    result = width * width
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {result}')


def get_circle_area(request, radius: int):
    result = 3.14 * (radius**2)
    return HttpResponse(f'Площадь круга радиуса {radius} равна {result}')