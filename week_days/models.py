from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Week(models.Model):
    days = models.CharField(max_length=15)
    works = models.TextField(blank=True)
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f'День - {self.days}, дела - {self.works}'

    # def get_url(self):
    #     return reverse('day-redirect', args=[])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.days)
        super(Week, self).save(*args, **kwargs)

