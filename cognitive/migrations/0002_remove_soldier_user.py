# Generated by Django 4.2 on 2023-05-21 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cognitive', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soldier',
            name='user',
        ),
    ]
