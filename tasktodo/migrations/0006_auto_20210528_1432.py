# Generated by Django 3.1 on 2021-05-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasktodo', '0005_auto_20210528_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]