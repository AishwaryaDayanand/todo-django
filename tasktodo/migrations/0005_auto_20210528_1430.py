# Generated by Django 3.1 on 2021-05-28 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasktodo', '0004_delete_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.date(2021, 5, 28)),
        ),
    ]