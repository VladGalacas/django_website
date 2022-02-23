from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
import datetime as dt
from .models import Horoscope_zodiac, Elements_zodiac


# Create your views here.


def int_horoscope(request, val_horoscope):
    if 0 < val_horoscope <= len(Horoscope_zodiac.objects.all()):
        zodiac = Horoscope_zodiac.objects.get(id=val_horoscope).zodiac
        redirect = reverse('horoscope_name', args=(zodiac,))
        return HttpResponseRedirect(redirect)
    return HttpResponseNotFound(f'<h2>Знака зодиака под номером {val_horoscope} не существует</h2>')


def str_horoscope(request, val_horoscope):
    for val in Horoscope_zodiac.objects.all():
        if val_horoscope in val.zodiac:
            return render(request, 'horoscope/sign_zodiac.html', context={
                'sign': Horoscope_zodiac.objects.all(),
                'valHoroscope': val_horoscope,
            })
    return HttpResponseNotFound(f'<h2>Знака зодиака {val_horoscope} не существует</h2>')


def index(request):
    return render(request, 'horoscope/index.html', context={
        'keys': Horoscope_zodiac.objects.all()
    })


def elements_types(request):
    elements = []
    for val in Elements_zodiac.objects.all():
        elements.append(val.elem)
    return render(request, 'horoscope/elements_type.html', context={
        'elements': elements,
    })


def zodiac_of_this_element(request, element):
    for val in Elements_zodiac.objects.all():
        if element in val.elem:
            get_elem = Elements_zodiac.objects.get(elem=element)
            zodiacs_description = Horoscope_zodiac.objects.filter(element=get_elem.id)
            break
    else:
        return HttpResponseNotFound(f'Стихии {element} не существует')
    zodiacs = []
    for value in zodiacs_description:
        zodiacs.append(value.zodiac)
    return render(request, 'horoscope/element_zodiacs.html', context={
        'element': element,
        'zodiacs': zodiacs,
    })


def zodiac_data(request, month, day):
    year = 2000
    try:
        day_insert = int(f"{dt.date(year, month, day):%j}") - 20
        if day_insert < 1:
            return render(request, 'horoscope/zodiac_date.html', context={
                'description': Horoscope_zodiac.objects.get(zodiac='capricorn').description,
                'zodiac': 'capricorn',
            })
        for val in Horoscope_zodiac.objects.all():
            start = val.day_start
            stop = val.day_stop
            if start <= day_insert <= stop:
                return render(request, 'horoscope/zodiac_date.html', context={
                    'description': val.description,
                    'zodiac': val.zodiac,
                })
    except ValueError:
        return HttpResponseNotFound('<h2>Неправильно введен месяц и/или день</h2>')
