# Generated by Django 3.0.3 on 2020-04-09 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tboard', '0004_timery_date1'),
    ]

    operations = [
        migrations.AddField(
            model_name='timery',
            name='evetime',
            field=models.TextField(blank=True),
        ),
    ]