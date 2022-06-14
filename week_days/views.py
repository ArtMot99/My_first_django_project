from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    day_of_week = list(dict_for_day)
    if week_day > len(day_of_week):
        return HttpResponseNotFound(f'{week_day} - неверно указан день. В неделе всего 7 дней.')
    name_week_day = day_of_week[week_day - 1]
    return HttpResponseRedirect(f'/todo_week/{name_week_day}')
