from django.db import models
from django.utils.text import slugify

# Create your models here.

class Horoscope_zodiac(models.Model):
    zodiac = models.CharField(max_length=15)
    description = models.TextField()
    element = models.ForeignKey('Elements_zodiac', on_delete=models.CASCADE)
    day_start = models.IntegerField()
    day_stop = models.IntegerField()

    def __str__(self):
        return f'Описание знака зодика {self.zodiac}: {self.description}'

class Elements_zodiac(models.Model):
    elem = models.CharField(max_length=15)

    def __str__(self):
        return self.elem