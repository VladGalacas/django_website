# Generated by Django 4.0.1 on 2022-02-15 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Elements',
            new_name='Elements_zodiac',
        ),
        migrations.RenameModel(
            old_name='Horoscope',
            new_name='Horoscope_zodiac',
        ),
    ]
