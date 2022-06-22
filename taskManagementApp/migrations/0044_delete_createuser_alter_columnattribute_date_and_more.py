# Generated by Django 4.0.4 on 2022-06-21 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagementApp', '0043_createuser_alter_columnattribute_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='createUser',
        ),
        migrations.AlterField(
            model_name='columnattribute',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 16, 32, 44, 869206)),
        ),
        migrations.AlterField(
            model_name='columnattribute',
            name='unique_random_id',
            field=models.SlugField(default='94035', max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 16, 32, 44, 871205)),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.SlugField(default='94035', max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.SlugField(default='94035', max_length=6, unique=True),
        ),
    ]
