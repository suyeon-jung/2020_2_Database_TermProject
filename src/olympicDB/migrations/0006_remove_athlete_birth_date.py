# Generated by Django 3.1.3 on 2020-12-05 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olympicDB', '0005_game_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='birth_date',
        ),
    ]
