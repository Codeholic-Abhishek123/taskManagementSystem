# Generated by Django 4.0.4 on 2022-06-15 08:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagementApp', '0018_alter_columnattribute_date_alter_comment_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='columnattribute',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 13, 30, 39, 961362)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 15, 13, 30, 39, 962361)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='file_name',
            field=models.CharField(max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='file_name',
            field=models.CharField(max_length=122, null=True),
        ),
    ]
