from django.contrib import admin
from .models import Week


# Register your models here.
@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    list_display = ['days', 'works', 'weekday_or_weekend']
    list_editable = ['works']
    # ordering = ['id']

    @admin.display(ordering='id')
    def weekday_or_weekend(self, d: Week):
        if d.id < 6:
            return 'Будни'
        else:
            return 'Выходной'

