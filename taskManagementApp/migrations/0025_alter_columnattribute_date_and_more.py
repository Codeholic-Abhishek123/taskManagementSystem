# Generated by Django 4.0.4 on 2022-06-16 10:59

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagementApp', '0024_alter_columnattribute_date_alter_comment_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='columnattribute',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 16, 29, 59, 116332)),
        ),
        migrations.AlterField(
            model_name='columnattribute',
            name='unique_random_id',
            field=models.CharField(blank=True, default=uuid.UUID('f18772af-021c-4580-9f2a-2611e32d9abd'), max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 16, 29, 59, 119329)),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.CharField(blank=True, default=uuid.UUID('27a35d65-a91d-4921-88c5-b580de6480f1'), max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.IntegerField(blank=True, default=uuid.UUID('1b5eaae7-1d69-4c15-bb73-c96faa0b2c21'), max_length=100, unique=True),
        ),
    ]
