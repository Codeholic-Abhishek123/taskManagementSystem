# Generated by Django 4.0.5 on 2022-06-13 03:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagementApp', '0002_remove_task_user_id_alter_columnattribute_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project_id',
        ),
        migrations.RemoveField(
            model_name='task',
            name='tag_id',
        ),
        migrations.AlterField(
            model_name='columnattribute',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 13, 9, 25, 44, 721431)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 13, 9, 25, 44, 721431)),
        ),
    ]
