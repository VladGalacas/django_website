from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='weekdays_main'),
    path('<int:day>/', views.day_number),
    path('<str:day>/', views.days_timetable, name='day-redirect'),

]
