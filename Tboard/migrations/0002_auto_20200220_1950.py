# Generated by Django 3.0.3 on 2020-02-20 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timery',
            name='timer1',
            field=models.TimeField(default=datetime.time),
        ),
        migrations.AlterField(
            model_name='timery',
            name='timer',
            field=models.DateField(),
        ),
    ]
