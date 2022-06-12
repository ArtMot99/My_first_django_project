from django.http import HttpResponse
from django.shortcuts import render


def leo(request):
    return HttpResponse('Знак зодиака лев')