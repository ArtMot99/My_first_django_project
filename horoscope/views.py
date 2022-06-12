from django.http import HttpResponse
from django.shortcuts import render


def leo(request):
    return HttpResponse('Знак зодиака лев')


def scorpio(request):
    return HttpResponse('Знак зодиака скорпион')