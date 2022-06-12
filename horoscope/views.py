from django.http import HttpResponse
from django.shortcuts import render


def leo(request):
    return HttpResponse('Знак зодиака лев')


def scorpio(request):
    return HttpResponse('Знак зодиака скорпион')


def aries(request):
    return HttpResponse('Знак зодиака овен')


def taurus(request):
    return HttpResponse('Знак зодиака телец')