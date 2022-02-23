from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def get_rectangle_area(request, width: int, height: int):
    rectangle_dict = {
        'width': width,
        'height': height,
        'area': width * height,
    }
    return render(request, 'geometry/rectangle.html', context=rectangle_dict)


def get_square_area(request, width: int):
    square_dict = {
        'width': width,
        'area': width ** 2
    }
    return render(request, 'geometry/square.html', context=square_dict)


def get_circle_area(request, radius: int):
    circle_dict = {
        'radius': radius,
        'area': 3.14 * radius ** 2
    }
    return render(request, 'geometry/circle.html', context=circle_dict)


def rectangle_redirect(request, width, height):
    url_redirect = reverse('rectangle-redirect', args=(width, height))
    return HttpResponseRedirect(url_redirect)


def square_redirect(request, width):
    url_redirect = reverse('square-redirect', args=(width,))
    return HttpResponseRedirect(url_redirect)


def circle_redirect(request, radius):
    url_redirect = reverse('circle-redirect', args=(radius,))
    return HttpResponseRedirect(url_redirect)
