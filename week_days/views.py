from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


dict_for_day = {
    'monday': 'Тут должен был быть список дел на понедельник',
    'tuesday': 'Тут должен был быть список дел на вторник',
    'wednesday': 'Тут должен был быть список дел на среду',
    'thursday': 'Тут должен был быть список дел на четверг',
    'friday': 'Тут должен был быть список дел на пятницу',
    'saturday': 'Тут должен был быть список дел на субботу',
    'sunday': 'Тут должен был быть список дел на воскресенье'
}


def get_info_week_days(request, week_day: str):
    description = dict_for_day.get(week_day)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'{week_day} - такого дня недели не существует')


def get_info_week_days_by_number(request, week_day: int):
    if 1 <= week_day <= 31:
        return HttpResponse(f'Сегодня {week_day} день недели!')
    else:
        return HttpResponse(f'Неверный номер дня - {week_day}')