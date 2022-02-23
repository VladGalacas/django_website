from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='horoscope_main'),
    path('type/', views.elements_types),
    path('type/<element>', views.zodiac_of_this_element, name='type_element'),
    path('<int:month>/<int:day>/', views.zodiac_data),
    path('<int:val_horoscope>/', views.int_horoscope),
    path('<str:val_horoscope>/', views.str_horoscope, name='horoscope_name'),

]
