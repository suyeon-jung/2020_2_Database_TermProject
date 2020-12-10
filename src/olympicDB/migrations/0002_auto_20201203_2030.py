# Generated by Django 3.1.3 on 2020-12-03 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olympicDB', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='athlete',
            old_name='country_id',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='athlete',
            old_name='sport_id',
            new_name='sport',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='olympic_id',
            new_name='olympic',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='sport_id',
            new_name='sport',
        ),
        migrations.RenameField(
            model_name='olympic',
            old_name='city_id',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='participate',
            old_name='athlete_id',
            new_name='athlete',
        ),
        migrations.RenameField(
            model_name='participate',
            old_name='game_id',
            new_name='game',
        ),
        migrations.AlterUniqueTogether(
            name='participate',
            unique_together={('athlete', 'medal_type', 'game')},
        ),
    ]
