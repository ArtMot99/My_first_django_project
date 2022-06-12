from django.http import HttpResponse
from django.shortcuts import render


def monday(request):
    return HttpResponse('<h1>Список дел на понедельник<h1>')


def tuesday(request):
    return HttpResponse('<h1>Список дел на вторник<h1>')