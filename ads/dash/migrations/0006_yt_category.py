# Generated by Django 2.2.11 on 2021-05-24 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0005_auto_20210524_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='yt',
            name='category',
            field=models.TextField(default=''),
        ),
    ]