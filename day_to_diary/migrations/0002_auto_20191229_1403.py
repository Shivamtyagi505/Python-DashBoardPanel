# Generated by Django 2.2.5 on 2019-12-29 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day_to_diary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
