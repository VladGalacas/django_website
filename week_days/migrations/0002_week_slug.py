# Generated by Django 4.0.1 on 2022-02-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('week_days', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
