# Generated by Django 2.2.11 on 2021-05-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0002_auto_20210522_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='yt',
            name='demand',
            field=models.IntegerField(default=0),
        ),
    ]
