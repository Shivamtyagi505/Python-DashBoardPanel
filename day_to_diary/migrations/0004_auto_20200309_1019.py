# Generated by Django 2.2.5 on 2020-03-09 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('day_to_diary', '0003_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='loaction',
            new_name='location',
        ),
    ]
