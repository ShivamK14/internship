# Generated by Django 3.1.7 on 2021-04-16 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webhooks', '0002_auto_20210416_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webhook',
            name='contact_picture',
        ),
    ]
