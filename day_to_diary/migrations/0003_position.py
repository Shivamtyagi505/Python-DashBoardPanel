# Generated by Django 2.2.5 on 2020-03-09 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day_to_diary', '0002_auto_20191229_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loaction', models.TextField()),
            ],
        ),
    ]
