# Generated by Django 4.0.4 on 2022-06-16 11:12

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagementApp', '0033_alter_columnattribute_date_alter_comment_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='columnattribute',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 16, 42, 55, 825152)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 16, 42, 55, 827150)),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.CharField(default=uuid.uuid4, max_length=122, null=True, unique=True),
        ),
    ]
