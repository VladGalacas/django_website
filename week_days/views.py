from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from .models import Week


# Create your views here.
# dict_days_timetable = {
#     'monday': "Понедельник – день после недели, то есть после воскресенья.",
#     'tuesday': 'Вторник – второй денек после воскресенья.',
#     'wednesday': 'Среда – серединка рабочей недели, ее сердце.',
#     'thursday': 'Четверг – четвертый день после воскресенья.',
#     'friday': 'Пятница – пятый день на неделе.',
#     'saturday': 'Суббота - день недели между пятницей и воскресеньем.',
#     'sunday': 'Воскресенье - день недели между субботой и понедельником.',
# }
# Week(days='sunday', works='Воскресенье - день недели между субботой и понедельником.').save()

def days_timetable(request, day: str):
    week_days = Week.objects.all()
    days_dict = {
        'week_days': week_days,
        'day': day,
    }
    for val in week_days:
        if day in val.days:
            return render(request, 'week_days/days.html', context=days_dict)

    return HttpResponseNotFound(f'<h3>Дня недели {day} не существует</h3>')


def day_number(request, day: int):
    week_days = Week.objects.all()
    if day < len(week_days):
        url_redirect = reverse('day-redirect', args=(list(week_days)[day - 1].days,))
        return HttpResponseRedirect(url_redirect)
    else:
        return HttpResponseNotFound(f'<h3>Неверный номер дня - {day}</h3>')


def index(request):
    week_days = Week.objects.all()
    days_dict = {
        'week_days': week_days,
    }
    return render(request, 'week_days/info.html', context=days_dict)
