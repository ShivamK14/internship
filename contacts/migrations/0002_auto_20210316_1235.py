# Generated by Django 3.1.5 on 2021-03-16 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='is_favorate',
        ),
        migrations.AddField(
            model_name='contact',
            name='is_favorite',
            field=models.BooleanField(default=True),
        ),
    ]
