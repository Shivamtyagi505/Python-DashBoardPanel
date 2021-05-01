# Generated by Django 2.2.5 on 2020-03-09 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day_to_diary', '0007_auto_20200309_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inputab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.TextField()),
                ('last', models.TextField()),
                ('report', models.TextField()),
                ('phone', models.IntegerField()),
                ('email', models.TextField()),
                ('address', models.TextField()),
                ('address2', models.TextField()),
                ('state', models.TextField()),
                ('state_zip', models.IntegerField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Inputa',
        ),
    ]